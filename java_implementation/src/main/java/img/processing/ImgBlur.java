package img.processing;

import java.awt.image.BufferedImage;
import static java.lang.Math.sqrt;
import static java.lang.Math.floor;
import static java.lang.Math.round;

public class ImgBlur {
    private static void boxesForGauss(int boxes[], double sigma, int n) {
        // ideal filter width
        double wi = sqrt((12 * sigma * sigma / n) + 1);

        int wl = (int) floor(wi);
        if (wl % 2 == 0)
            wl--;
        int wu = wl + 2;

        double mi = (12 * sigma * sigma - n * wl * wl - 4 * n * wl - 3 * n) / (-4 * wl - 4);
        int m = (int) round(mi);

        for (int i = 0; i < n; i++)
            boxes[i] = ((i < m ? wl : wu) - 1) / 2;
    }

    private static void horizontalBlur(int[] in, int[] out, int w, int h, int r) {
        float iarr = 1.f / (r + r + 1);

        for (int i = 0; i < h; i++) {
            int ti = i * w, li = ti, ri = ti + r, fv = in[ti], lv = in[ti + w - 1], val = (r + 1) * fv;
            for (int j = 0; j < r; j++)
                val += in[ti + j];
            for (int j = 0; j <= r; j++) {
                val += in[ri++] - fv;
                out[ti++] = round(val * iarr);
            }
            for (int j = r + 1; j < w - r; j++) {
                val += in[ri++] - in[li++];
                out[ti++] = round(val * iarr);
            }
            for (int j = w - r; j < w; j++) {
                val += lv - in[li++];
                out[ti++] = round(val * iarr);
            }
        }
    }

    private static void totalBlur(int[] in, int[] out, int w, int h, int r) {
        float iarr = 1.f / (r + r + 1);

        for (int i = 0; i < w; i++) {
            int ti = i, li = ti, ri = ti + r * w, fv = in[ti], lv = in[ti + w * (h - 1)], val = (r + 1) * fv;
            for (int j = 0; j < r; j++) {
                val += in[ti + j * w];
            }
            for (int j = 0; j <= r; j++) {
                val += in[ri] - fv;
                out[ti] = round(val * iarr);
                ri += w;
                ti += w;
            }
            for (int j = r + 1; j < h - r; j++) {
                val += in[ri] - in[li];
                out[ti] = round(val * iarr);
                li += w;
                ri += w;
                ti += w;
            }
            for (int j = h - r; j < h; j++) {
                val += lv - in[li];
                out[ti] = round(val * iarr);
                li += w;
                ti += w;
            }
        }
    }

    private static void boxBlur(int[] in, int[] out, int w, int h, int r) {
        horizontalBlur(in, out, w, h, r);
        totalBlur(out, in, w, h, r);
    }

    private static void fastGuassianBlur(int[] in, int[] out, int w, int h, double sigma) {
        int[] boxes = new int[3];
        boxesForGauss(boxes, sigma, 3);
        boxBlur(in, out, w, h, boxes[0]);
        boxBlur(in, out, w, h, boxes[1]);
        boxBlur(in, out, w, h, boxes[2]);

    }

    public static BufferedImage blurImage(BufferedImage im, double sigma) {
        int width = im.getWidth();
        int height = im.getHeight();

        int[] pixels = new int[width * height];
        im.getRGB(0, 0, width, height, pixels, 0, width);

        int[] redPixels = new int[width * height];
        int[] greenPixels = new int[width * height];
        int[] bluePixels = new int[width * height];
        int[] newRedPixels = new int[width * height];
        int[] newGreenPixels = new int[width * height];
        int[] newBluePixels = new int[width * height];

        for (int i = 0; i < pixels.length; i++) {
            int pixel = pixels[i];

            int red = (pixel >> 16) & 0xff;
            int green = (pixel >> 8) & 0xff;
            int blue = pixel & 0xff;

            redPixels[i] = red;
            greenPixels[i] = green;
            bluePixels[i] = blue;
        }
        
        fastGuassianBlur(bluePixels, newBluePixels, width, height, sigma);
        fastGuassianBlur(redPixels, newRedPixels, width, height, sigma);
        fastGuassianBlur(greenPixels, newGreenPixels, width, height, sigma);

        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int index = y * width + x;
                int rgb = (newRedPixels[index] << 16) | (newGreenPixels[index] << 8) | newBluePixels[index];
                im.setRGB(x, y, rgb);
            }
        }

        return im;
    }
}
