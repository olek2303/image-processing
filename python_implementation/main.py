import os
from image import ImageRead
from blur import blur_image
from merge import mergeImages
from delete import delete_area
import time


class Timer:
    def __init__(self):
        self.start_ = 0

    def start(self):
        self.start_ = time.time()

    def stop(self):
        duration = time.time() - self.start_
        print(f"Elapsed Time: {duration} s")


def main():
    choice = 0
    tim = Timer()
    im = None

    while choice != '4':
        print("\nMenu:")
        print("1. Blur Image")
        print("2. Merge Image")
        print("3. Delete Areas of Image")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice in ['1', '2', '3']:
            while True:
                filepath = input("Enter the full path of the file: ")
                if os.path.exists(filepath):
                    im = ImageRead(filepath)
                    im.loadImage()
                    break
                else:
                    print("File does not exist. Please enter a valid path.")

        if choice == '1' and im is not None:
            while True:
                try:
                    sigma = float(input("Enter the radius of the blur: "))
                    if sigma > 0:
                        break
                    else:
                        print("Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            tim.start()
            im.img = blur_image(im.img, sigma)
            tim.stop()
            im.saveImage("blur")
        elif choice == '2' and im is not None:
            inName2 = input("Enter the full path of the second image: ")
            im1 = ImageRead(inName2)
            im1.loadImage()
            alpha = input("Enter alpha value: ")
            tim.start()
            merged = mergeImages(im.img, im1.img, float(alpha))
            tim.stop()

            # Zamiast używać metody saveImage, użyj metody save() z PIL
            merged_output_path = "merged_output.jpg"  # Możesz zmodyfikować nazwę pliku według potrzeb
            merged.save(merged_output_path)
            print(f"Image saved as {merged_output_path}")
        elif choice == '3' and im is not None:
            while True:
                try:
                    x = int(input("Insert x coordinate (x, y) of the area to delete: "))
                    if x > 0:
                        break
                    else:
                        print("X coordinate must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for X coordinate.")

            while True:
                try:
                    y = int(input("Insert y coordinate (x, y) of the area to delete: "))
                    if y > 0:
                        break
                    else:
                        print("Y coordinate must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for Y coordinate.")

            while True:
                try:
                    area_width = int(input("Insert width of the area: "))
                    if area_width > 0:
                        break
                    else:
                        print("Width must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for width.")

            while True:
                try:
                    area_height = int(input("Insert height of the area: "))
                    if area_height > 0:
                        break
                    else:
                        print("Height must be greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for height.")

            tim.start()
            im.img = delete_area(im.img, x, y, area_width, area_height)
            tim.stop()
            im.saveImage("deleted")
        elif choice == '4':
            print("Exiting program.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == '__main__':
    main()
