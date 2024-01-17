import math


def boxes_for_gauss(sigma, n):
    # ideal filter width
    wi = math.sqrt((12 * sigma * sigma / n) + 1)

    wl = int(math.floor(wi))
    if wl % 2 == 0:
        wl -= 1
    wu = wl + 2

    mi = (12 * sigma * sigma - n * wl * wl - 4 * n * wl - 3 * n) / (-4 * wl - 4)
    m = int(round(mi))

    boxes = [((wl if i < m else wu) - 1) // 2 for i in range(n)]
    return boxes


def horizontal_blur(in_pixels, out_pixels, w, h, r):
    iarr = 1.0 / (r + r + 1)

    for i in range(h):
        ti = i * w
        li = ti
        ri = ti + r
        fv = in_pixels[ti]
        lv = in_pixels[ti + w - 1]
        val = (r + 1) * fv
        for j in range(r):
            val += in_pixels[ti + j]
        for j in range(r + 1):
            val += in_pixels[ri] - fv
            out_pixels[ti] = round(val * iarr)
            ri += 1
            ti += 1
        for j in range(r + 1, w - r):
            val += in_pixels[ri] - in_pixels[li]
            out_pixels[ti] = round(val * iarr)
            li += 1
            ri += 1
            ti += 1
        for j in range(w - r, w):
            val += lv - in_pixels[li]
            out_pixels[ti] = round(val * iarr)
            li += 1
            ti += 1


def total_blur(in_pixels, out_pixels, w, h, r):
    iarr = 1.0 / (r + r + 1)

    for i in range(w):
        ti = i
        li = ti
        ri = ti + r * w
        fv = in_pixels[ti]
        lv = in_pixels[ti + w * (h - 1)]
        val = (r + 1) * fv
        for j in range(r):
            val += in_pixels[ti + j * w]
        for j in range(r + 1):
            val += in_pixels[ri] - fv
            out_pixels[ti] = round(val * iarr)
            ri += w
            ti += w
        for j in range(r + 1, h - r):
            val += in_pixels[ri] - in_pixels[li]
            out_pixels[ti] = round(val * iarr)
            li += w
            ri += w
            ti += w
        for j in range(h - r, h):
            val += lv - in_pixels[li]
            out_pixels[ti] = round(val * iarr)
            li += w
            ti += w


def box_blur(in_pixels, out_pixels, w, h, r):
    horizontal_blur(in_pixels, out_pixels, w, h, r)
    total_blur(out_pixels, in_pixels, w, h, r)


def fast_gaussian_blur(in_pixels, out_pixels, w, h, sigma):
    boxes = boxes_for_gauss(sigma, 3)
    box_blur(in_pixels, out_pixels, w, h, boxes[0])
    box_blur(in_pixels, out_pixels, w, h, boxes[1])
    box_blur(in_pixels, out_pixels, w, h, boxes[2])


def blur_image(im, sigma):
    width, height = im.size

    pixels = list(im.getdata())
    red_pixels = [pixel[0] for pixel in pixels]
    green_pixels = [pixel[1] for pixel in pixels]
    blue_pixels = [pixel[2] for pixel in pixels]
    new_red_pixels = [0] * (width * height)
    new_green_pixels = [0] * (width * height)
    new_blue_pixels = [0] * (width * height)

    fast_gaussian_blur(blue_pixels, new_blue_pixels, width, height, sigma)
    fast_gaussian_blur(red_pixels, new_red_pixels, width, height, sigma)
    fast_gaussian_blur(green_pixels, new_green_pixels, width, height, sigma)

    new_pixels = [(new_red_pixels[i], new_green_pixels[i], new_blue_pixels[i]) for i in range(len(new_red_pixels))]
    im.putdata(new_pixels)
    return im
