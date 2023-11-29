from PIL import Image
from math import sqrt, floor

def boxes_for_gauss(sigma, n):
    wi = sqrt((12 * sigma * sigma / n) + 1)

    wl = floor(wi)
    if wl % 2 == 0:
        wl -= 1
    wu = wl + 2
    mi = (12 * sigma * sigma - n * wl * wl - 4 * n * wl - 3 * n) / (-4 * wl - 4)
    m = round(mi)

    return [wl, m, wu]

def horizontal_blur(inData, outData, w, h, r):
        iarr = 1.0 / (r + r + 1)

        for i in range(h):
            ti = i * w
            li = ti
            ri = ti + r
            fv = inData[ti]
            lv = inData[ti + w - 1]
            val = (r + 1) * fv
            for j in range(r):
                val += inData[ti + j]

            for j in range(r):
                val += inData[ri] - fv
                outData[ti] = round(val * iarr)
                ti += 1
                ri += 1

            for j in range(r + 1, w - r):
                val += inData[ri] - inData[li]
                outData[ti] = round(val * iarr)
                ri += 1
                li += 1
                ti += 1
            for j in range(w - r, w):
                val += lv - inData[li]
                outData[ti] = round(val * iarr)
                li += 1
                ti += 1

def total_blur(inData, outData, w, h, r):
        iarr = 1.0 / (r + r + 1)

        for i in range(w):
            ti, li, ri = i, i, i + r * w
            fv, lv = inData[ti], inData[ti + w * (h - 1)]
            val = (r + 1) * fv

            for j in range(r):
                val += inData[ti + j * w]

            for j in range(r + 1):
                val += inData[ri] - fv
                outData[ti] = round(val * iarr)
                ri += w
                ti += w

            for j in range(r + 1, h - r):
                val += inData[ri] - inData[li]
                outData[ti] = round(val * iarr)
                li += w
                ri += w
                ti += w

            for j in range(h - r, h):
                val += lv - inData[li]
                outData[ti] = round(val * iarr)
                li += w
                ti += w


def boxBlur(inData, outData, w, h, sigma):
    horizontal_blur(inData, outData, w, h, sigma)
    total_blur(outData, inData, w, h, sigma)

def fast_guassian_blur(inData, outData, w, h, sigma):
    boxes = boxes_for_gauss(sigma, 3)
    boxBlur(inData, outData, w, h, boxes[0])
    boxBlur(inData, outData, w, h, boxes[1])
    boxBlur(inData, outData, w, h, boxes[2])

def blur_image(im, sigma):
    oldr, oldg, oldb = im.img.split()

    newr = Image.new('L', (im.width, im.heigth))  # 'L' oznacza tryb obrazu grayscale
    newg = Image.new('L', (im.width, im.heigth))
    newb = Image.new('L', (im.width, im.heigth))

    listNR = list(newr.getdata())
    listNB = list(newb.getdata())
    listNG = list(newg.getdata())
    print("Type of ", type(newr.getdata()[1]))

    fast_guassian_blur(list(oldr.getdata()), listNR, im.width, im.heigth, sigma)
    fast_guassian_blur(list(oldb.getdata()), listNB, im.width, im.heigth, sigma)
    fast_guassian_blur(list(oldg.getdata()), listNG, im.width, im.heigth, sigma)

    newr.putdata(listNR)
    newb.putdata(listNB)
    newg.putdata(listNG)

    new_image = Image.merge('RGB', (newr, newg, newb))

    return new_image
