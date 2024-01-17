import os
from PIL import Image


class ImageRead:
    def __init__(self, filepath="Default.jpg"):
        self.filepath = filepath

    def loadImage(self):
        try:
            self.img = Image.open(self.filepath)
            self.width, self.height = self.img.size
            self.pixelData = list(self.img.getdata())
            print(f"Loaded Image: {self.width} x {self.height} with path {self.filepath}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def saveImage(self, operation):
        try:
            outputName = operation + "_" + os.path.basename(self.filepath)
            self.img.save(outputName)
        except Exception as e:
            print(f"An error occurred: {e}")
