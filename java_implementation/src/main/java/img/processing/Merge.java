package img.processing;

import java.awt.image.BufferedImage;

public class Merge {
    // private method blendColors was made by AI
    private static int blendColors(int rgb1, int rgb2, double alpha) {
        int r1 = (rgb1 >> 16) & 0xFF;
        int g1 = (rgb1 >> 8) & 0xFF;
        int b1 = rgb1 & 0xFF;

        int r2 = (rgb2 >> 16) & 0xFF;
        int g2 = (rgb2 >> 8) & 0xFF;
        int b2 = rgb2 & 0xFF;

        int blendedR = (int) ((r1 * (1.0 - alpha)) + (r2 * alpha));
        int blendedG = (int) ((g1 * (1.0 - alpha)) + (g2 * alpha));
        int blendedB = (int) ((b1 * (1.0 - alpha)) + (b2 * alpha));

        return (blendedR << 16) | (blendedG << 8) | blendedB;
    }

    public static BufferedImage mergeImages(BufferedImage im1, BufferedImage im2, double alpha) {
        int mergedW = Math.max(im1.getWidth(), im2.getWidth());
        int mergedH = Math.max(im1.getHeight(), im2.getHeight());

        BufferedImage merged = new BufferedImage(mergedW, mergedH, 3);

        int size1 = im1.getWidth() * im1.getHeight() * 3;
        int size2 = im2.getWidth() * im2.getHeight() * 3;

        if (size1 > size2) {
            // Copy first image to output image
            for (int y = 0; y < im1.getHeight(); y++) {
                for (int x = 0; x < im1.getWidth(); x++) {
                    int rgb = im1.getRGB(x, y);
                    merged.setRGB(x, y, rgb);
                }
            }
            for (int y = 0; y < im2.getHeight(); y++) {
                for (int x = 0; x < im2.getWidth(); x++) {
                    int rgb1 = merged.getRGB(x, y);
                    int rgb2 = im2.getRGB(x, y);
                    int blendedRGB = blendColors(rgb1, rgb2, alpha);
                    merged.setRGB(x, y, blendedRGB);
                }
            }
        } else {
            for (int y = 0; y < im2.getHeight(); y++) {
                for (int x = 0; x < im2.getWidth(); x++) {
                    int rgb = im2.getRGB(x, y);
                    merged.setRGB(x, y, rgb);
                }
            }
            for (int y = 0; y < im1.getHeight(); y++) {
                for (int x = 0; x < im1.getWidth(); x++) {
                    int rgb1 = merged.getRGB(x, y);
                    int rgb2 = im1.getRGB(x, y);
                    int blendedRGB = blendColors(rgb1, rgb2, alpha);
                    merged.setRGB(x, y, blendedRGB);
                }
            }
        }

        return merged;
    }
}
