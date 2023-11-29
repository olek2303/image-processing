from PIL import Image

class ImageRead:
    def __init__(self, filename):
        self.filename = filename
        self.imagePath = "./" + filename

    def loadImage(self):
        try:
            self.img = Image.open(self.imagePath)
            self.width, self.heigth = self.img.size
            self.pixelData = list(self.img.getdata())
            print(f"Loaded Image: {self.width} x {self.heigth} with name {self.filename}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def saveImage(self, operation):
        try:
            outputName = "./" + operation + "_" + self.filename
            self.img.save(outputName)
        except Exception as e:   
            print(f"An error occurred: {e}")