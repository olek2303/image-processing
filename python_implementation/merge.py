from PIL import Image


def mergeImages(im1, im2, alpha):
    mergedW = max(im1.width, im2.width)
    mergedH = max(im1.height, im2.height)

    merged = Image.new("RGB", (mergedW, mergedH))

    for y in range(mergedH):
        for x in range(mergedW):
            p1 = im1.getpixel((x * im1.width // mergedW, y * im1.height // mergedH))
            p2 = im2.getpixel((x * im2.width // mergedW, y * im2.height // mergedH))

            p1 = tuple(map(int, p1))
            p2 = tuple(map(int, p2))

            merged_pixel_value = tuple(
                int(p1_channel * (1.0 - float(alpha)) + p2_channel * float(alpha))
                for p1_channel, p2_channel in zip(p1, p2)
            )

            merged.putpixel((x, y), merged_pixel_value)

    return merged

