from PIL import Image

def delete_area(im, x, y, area_width, area_height, channels = 3):
    width, height = im.img.size
    if x < 0 or y < 0 or x + area_width > width or y + area_height > height:
        print("The area extends beyond the image size.")
        return None
    
    deleted = im.img.copy()

    # Deleting area
    white_pixel = (255, 255, 255, 255)
    for i in range(y, y + area_height):
        for j in range(x, x + area_width):
            for c in range(channels):
                deleted.putpixel((j, i), white_pixel)

    return deleted