package img.processing;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class ImgLoad {

    public static BufferedImage loadImage(String filePath) {
        try {
            return ImageIO.read(new File(filePath));
        } catch (IOException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static void saveImage(BufferedImage image, String filePath, String formatName) {
        try {
            ImageIO.write(image, formatName, new File(filePath));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    
}