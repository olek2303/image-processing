from image import ImageRead
from blur import blur_image

if __name__ == '__main__':
    inputName = input("Enter a file name with extension: ")
    im = ImageRead(inputName)
    im.loadImage()
    blur_im = blur_image(im, 2.0)
    blur_im.save("./blured.jpg")


