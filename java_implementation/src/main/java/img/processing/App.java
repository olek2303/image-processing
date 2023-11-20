package img.processing;

import java.awt.image.BufferedImage;
import java.util.Scanner;

import javax.swing.Timer;

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
            TimeClock t = new TimeClock();

            if (i == 4) {
                System.out.println("Exiting the program...\n");
                break;
            }

            // Loading image
            System.out.println(
                    "Enter the file name with extension (or full path if file is in the other directory)\n");

            String fileName = scanner.next();
            BufferedImage im = ImgLoad.loadImage(fileName);
            while (im == null) {
                System.out.println(
                        "Error while opening a file. Enter the file name again:\n");
                fileName = scanner.next();
                im = ImgLoad.loadImage(fileName);
            }

            switch (i) {
                case 1:
                    System.out.println("Insert blur radius (from 0 to 10): ");
                    double sigma = scanner.nextDouble();
                    while (sigma < 0 || sigma > 10) {
                        System.out.println("Wrong blur radius!\n");
                        System.out.println("Insert blur radius (from 0 to 10): ");
                        sigma = scanner.nextDouble();
                    }

                    t.start();
                    BufferedImage blured = ImgBlur.blurImage(im, sigma);
                    t.stop();

                    String outFileName = fileName + "_blured.jpg";
                    ImgLoad.saveImage(blured, outFileName, "jpg");
                    break;
                case 2:
                    System.out.println(
                            "Enter the second file name with extension (or full path if file is in the other directory)\n");

                    fileName = scanner.next();
                    BufferedImage im2 = ImgLoad.loadImage(fileName);
                    while (im == null) {
                        System.out.println(
                                "Error while opening a file. Enter the file name again:\n");
                        fileName = scanner.next();
                        im = ImgLoad.loadImage(fileName);
                    }
                    System.out.println("Insert alpha value <0,1>:");
                    double alpha = scanner.nextDouble();
                    while (alpha < 0 || alpha > 1) {
                        System.out.println("Wrong number. Try again: ");
                        alpha = scanner.nextDouble();
                    }
                    t.start();
                    BufferedImage merged = Merge.mergeImages(im, im2, alpha);
                    t.stop();
                    String outFileName2 = fileName + "_merged.jpg";
                    ImgLoad.saveImage(merged, outFileName2, "jpg");
                    break;
                case 3:
                    String outFileName3 = fileName + "_deleted.jpg";

                    break;
                case 4:
                    System.out.println("Exiting the program...\n");
                    break;
                default:
                    break;
            }

        }

        scanner.close();
    }

}
