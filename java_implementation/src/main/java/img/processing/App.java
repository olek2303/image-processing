package img.processing;

import java.awt.image.BufferedImage;

public class App {
    public static void main(String[] args) {
        // Example usage
        String inputFilePath = "./images/test.jpg";
        String outputFilePath = "./images/blured.jpg";

        // Load image
        BufferedImage loadedImage = ImgLoad.loadImage(inputFilePath);

        BufferedImage blured = ImgBlur.blurImage(loadedImage, 5);

        if (loadedImage != null) {
            // Save image
            ImgLoad.saveImage(blured, outputFilePath, "jpg");
        }

    }

}
