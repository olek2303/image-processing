from image import ImageRead
from PIL import Image

def blend_colors(rgb1, rgb2, alpha):
    r1, g1, b1 = (rgb1 >> 16) & 0xFF, (rgb1 >> 8) & 0xFF, rgb1 & 0xFF
    r2, g2, b2 = (rgb2 >> 16) & 0xFF, (rgb2 >> 8) & 0xFF, rgb2 & 0xFF

    blendedR = int((r1 * (1.0 - alpha)) + (r2 * alpha))
    blendedG = int((g1 * (1.0 - alpha)) + (g2 * alpha))
    blendedB = int((b1 * (1.0 - alpha)) + (b2 * alpha))

    return (blendedR << 16) | (blendedG << 8) | blendedB

def mergeImages(im1, im2, alpha):
    mergedW = max(im1.img.width, im2.img.width)
    mergedH = max(im1.img.height, im2.img.height)

    merged = Image.new("RGB", (mergedW, mergedH))

    size1 = im1.img.width * im1.img.height * 3
    size2 = im2.img.width * im2.img.height * 3

    if size1 > size2: 
        merged = im1.img
        for y in range(im2.img.height):
            for x in range(im2.img.width):
                rgb1 = merged.getpixel((x, y))
                rgb2 = im2.img.getpixel((x, y))
                blended_rgb = blend_colors(rgb1, rgb2, alpha)
                merged.img.putpixel((x, y), blended_rgb)
    else:
        merged = im2.img
        for y in range(im1.img.height):
            for x in range(im1.img.width):
                rgb1 = merged.getpixel((x, y))
                rgb2 = im1.img.getpixel((x, y))
                blended_rgb = blend_colors(rgb1, rgb2, alpha)
                merged.img.putpixel((x, y), blended_rgb)
        
    return merged;
