package img.processing;

import java.awt.image.BufferedImage;
import java.util.Scanner;

public class App {

    public static void main(String[] args) {

        int i = 0;
        Scanner scanner = new Scanner(System.in);
        while (i != 4) {

            System.out.println("Options\n");
            System.out.println("1. Blurring\n");
            System.out.println("2. Merging\n");
            System.out.println("3. Deleting\n");
            System.out.println("4. Quit\n");

            System.out.println("Choose an option from 1-4");

            i = scanner.nextInt();

            switch (i) {
                case 1:
                    System.out.println(
                            "Enter the file name with extension (or full path if file is in the other directory)\n");

                    String fileName = scanner.next();

                    BufferedImage im = ImgLoad.loadImage(fileName);

                    System.out.println("Insert blur radius (from 0 to 10): ");

                    double sigma = scanner.nextDouble();
                    while (sigma < 0 || sigma > 10) {
                        System.out.println("Wrong blur radius!\n");
                        System.out.println("Insert blur radius (from 0 to 10): ");
                        sigma = scanner.nextDouble();
                    }

                    BufferedImage blured = ImgBlur.blurImage(im, sigma);
                    ImgLoad.saveImage(blured, "./images/blured.jpg", "jpg");
                    break;

                default:
                    break;
            }

        }

        // // Example usage
        // String inputFilePath = "./images/test.jpg";
        // String outputFilePath = "./images/blured.jpg";

        // // Load image
        // BufferedImage loadedImage = ImgLoad.loadImage(inputFilePath);

        // if (loadedImage != null) {
        // // Save image
        // ImgLoad.saveImage(blured, outputFilePath, "jpg");
        // }

        scanner.close();
    }

}
