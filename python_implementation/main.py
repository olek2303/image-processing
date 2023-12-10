from image import ImageRead
from blur import blur_image
from merge import mergeImages
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
    while choice != 4:
        print("\nMenu:")
        print("1. Blur Image")
        print("2. Merge Image")
        print("3. Delete Areas of Image")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if 0 < int(choice) < 4:
            inputName = input("Enter a file name with extension: ")
            im = ImageRead(inputName)
            im.loadImage()

        if choice == '1':
            sigma = input("Enter the radius of the blur: ")
            tim.start()
            im.img = blur_image(im.img, float(sigma))
            tim.stop()
            im.saveImage("blur")
            continue
        elif choice == '2':
            inName2 = input("Enter first image with extension: ")
            im1 = ImageRead(inName2)
            im1.loadImage()
            alpha = input("Enter alpha value: ")
            tim.start()
            merged = mergeImages(im, im1, alpha)
            tim.stop()
            merged.saveImage("merged")
            continue
        elif choice == '3':
            continue
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == '__main__':
    main()
