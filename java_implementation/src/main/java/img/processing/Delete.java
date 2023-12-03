package img.processing;
import java.awt.image.BufferedImage;

public class Delete {
    public static BufferedImage deleteArea(BufferedImage im, int width, int height, int x, int y, int areaWidth, int areaHeight,
            int channels) {
        // Checking if area is possible to delete
        BufferedImage deleted = im;
        if (x < 0 || y < 0 || x + areaWidth > width || y + areaHeight > height) {
            System.err.println("The area extends beyond the image size.");
            return null;
        }
        int whitePixel = (255 << 24) | (255 << 16) | (255 << 8) | 255;
        

        // Deleting area
        for (int i = y; i < y + areaHeight; i++) {
            for (int j = x; j < x + areaWidth; j++) {
                for (int c = 0; c < channels; c++) {
                    deleted.setRGB(x + j, y + i, whitePixel);
                }
            }
        }
        

        return deleted;
    }
}