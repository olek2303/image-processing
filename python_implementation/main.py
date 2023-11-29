from image import ImageRead

if __name__ == '__main__':
    inputName = input("Enter a file name with extension: ")
    im = ImageRead(inputName)
    im.loadImage()

