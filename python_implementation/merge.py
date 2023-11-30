from image import ImageRead
from PIL import Image

def mergeImages(im1, im2, alpha):
    mergedW = max(im1.img.width, im2.img.width)
    mergedH = max(im1.img.height, im2.img.height)

    merged = ImageRead()
    merged.filename = "images.jpg"
    merged.img = Image.new("RGB", (mergedW, mergedH))

    size1 = im1.img.width * im1.img.height 
    size2 = im2.img.width * im2.img.height 

    if size1 > size2:
        for y in range(im1.img.height):
            for x in range(im1.img.width):
                merged.img.putpixel((x, y), tuple(im1.img.getpixel((x, y))))
    else:
        for y in range(im2.img.height):
            for x in range(im2.img.width):
                merged.img.putpixel((x, y), tuple(im2.img.getpixel((x, y))))

    for y in range(mergedH):
        for x in range(mergedW):
            p1 = im1.img.getpixel((x, y))
            p2 = im2.img.getpixel((x, y))
            p1 = tuple(map(int, p1))
            p2 = tuple(map(int, p2))
            merged_pixel_value = tuple (
                int(p1_channel * (1.0 - float(alpha)) + p2_channel * float(alpha))
                for p1_channel, p2_channel in zip(p1, p2)
            )
            merged.img.putpixel((x, y), merged_pixel_value)
                
    return merged;
