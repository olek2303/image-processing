package img.processing;
import java.awt.image.BufferedImage;

public class App 
{
    public static void main(String[] args) {
        // Example usage
        String inputFilePath = "./images/test.jpg";
        String outputFilePath = "./images/test1.jpg";

        // Load image
        BufferedImage loadedImage = ImgLoad.loadImage(inputFilePath);

        if (loadedImage != null) {
            // Save image
            ImgLoad.saveImage(loadedImage, outputFilePath, "jpg");
        }
    }
}
