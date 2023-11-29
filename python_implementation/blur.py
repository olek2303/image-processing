from PIL import Image
from math import sqrt, floor
from image import ImageRead


def boxes_for_gauss(sigma, n):
    # ideal filter width
    wi = sqrt((12 * sigma ** 2 / n) + 1)
    wl = floor(wi)
    if wl % 2 == 0:
        wl -= 1
    wu = wl + 2

    mi = (12 * sigma ** 2 - n * wl ** 2 - 4 * n * wl - 3 * n) / (-4 * wl - 4)
    m = round(mi)

    boxes = [((wl if i < m else wu) - 1) // 2 for i in range(n)]

    return boxes


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


def box_blur(inData, outData, w, h, sigma):
    inData, outData = outData, inData
    horizontal_blur(outData, inData, w, h, sigma)
    total_blur(outData, inData, w, h, sigma)


def fast_guassian_blur(inData, outData, w, h, sigma):
    boxes = boxes_for_gauss(sigma, 3)
    box_blur(inData, outData, w, h, boxes[0])
    box_blur(outData, inData, w, h, boxes[1])
    box_blur(inData, outData, w, h, boxes[2])


def blur_image(im, sigma):
    oldr, oldg, oldb = im.img.split()

    newr = Image.new('L', (im.width, im.heigth))
    newg = Image.new('L', (im.width, im.heigth))
    newb = Image.new('L', (im.width, im.heigth))

    listOR = list(oldr.getdata())
    listOG = list(oldg.getdata())
    listOB = list(oldb.getdata())

    listNR = list(newr.getdata())
    listNB = list(newb.getdata())
    listNG = list(newg.getdata())


    fast_guassian_blur(listOB, listNB, im.width, im.heigth, sigma)
    fast_guassian_blur(listOG, listNG, im.width, im.heigth, sigma)
    fast_guassian_blur(listOR, listNR, im.width, im.heigth, sigma)

    newr.putdata(listNR)
    newb.putdata(listNB)
    newg.putdata(listNG)


    new_image = ImageRead()
    new_image.img = Image.merge('RGB', (newr, newg, newb))
    new_image.filename = im.filename


    return new_image
