package img.processing;

import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import java.awt.image.DataBufferInt;
import java.awt.image.Raster;
import java.awt.image.DataBufferByte;
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

    private static void horizontalBlur(byte[] in, byte[] out, int w, int h, int r) {
        float iarr = 1.f / (r + r + 1);
        for (int i = 0; i < h; i++) {
            int ti = i * w, li = ti, ri = ti + r;
            float fv = in[ti];
            float lv = in[ti + w - 1];
            float val = (r + 1) * fv;

            for (int j = 0; j < r; j++)
                val += in[ti + j];
            for (int j = 0; j <= r; j++) {
                val += in[ri++] - fv;
                out[ti++] = (byte) (val * iarr);
            }
            for (int j = r + 1; j < w - r; j++) {
                val += in[ri++] - in[li++];
                out[ti++] = (byte) (val * iarr);
            }
            for (int j = w - r; j < w; j++) {
                val += lv - in[li++];
                out[ti++] = (byte) (val * iarr);
            }
        }
    }

    private static void totalBlur(byte[] in, byte[] out, int w, int h, int r) {
        float iarr = 1.f / (r + r + 1);
        for (int i = 0; i < w; i++) {
            int ti = i, li = ti, ri = ti + r * w;
            byte fv = in[ti];
            byte lv = in[ti + w * (h - 1)];
            float val = (r + 1) * fv;
            for (int j = 0; j < r; j++)
                val += in[ti + j * w];

            for (int j = 0; j <= r; j++) {
                val += in[ri] - fv;
                out[ti] = (byte) (val * iarr);
                ri += w;
                ti += w;
            }
            for (int j = r + 1; j < h - r; j++) {
                val += in[ri] - in[li];
                out[ti] = (byte) (val * iarr);
                li += w;
                ri += w;
                ti += w;
            }
            for (int j = h - r; j < h; j++) {
                val += lv - in[li];
                out[ti] = (byte) (val * iarr);
                li += w;
                ti += w;
            }
        }
    }

    private static void boxBlur(byte[] in, byte[] out, int w, int h, int r) {
        // swap in and out
        byte[] temp = in;
        in = out;
        out = temp;
        temp = null;

        horizontalBlur(in, out, w, h, r);
        totalBlur(in, out, w, h, r);
    }

    private static void fastGuassianBlur(byte[] in, byte[] out, int w, int h, double sigma) {
        int[] boxes = new int[3];
        boxesForGauss(boxes, sigma, 3);
        boxBlur(in, out, w, h, boxes[0]);
        boxBlur(out, in, w, h, boxes[1]);
        boxBlur(in, out, w, h, boxes[2]);

    }

    public static BufferedImage blurImage(BufferedImage im, double sigma) {
        int width = im.getWidth();
        int height = im.getHeight();
        // image data

        byte[] pixels = ((DataBufferByte) im.getData().getDataBuffer()).getData();

        // input RGB channels
        byte[] oldr = new byte[width * height];
        byte[] oldg = new byte[width * height];
        byte[] oldb = new byte[width * height];

        // output RGB channels
        byte[] newr = new byte[width * height];
        byte[] newg = new byte[width * height];
        byte[] newb = new byte[width * height];

        for (int i = 0; i < pixels.length; i += 3) {
            int index = i / 3;
            oldb[index] = (byte) ((pixels[i] & 0xFF) / 255.0f);
            oldg[index] = (byte) ((pixels[i + 1] & 0xFF) / 255.0f);
            oldr[index] = (byte) ((pixels[i + 2] & 0xFF) / 255.0f);
        }
        int flag = 0;
        for (int j = 0; j < oldb.length; j++) {
            if (oldb[j] != 0)
                flag = 1;

        }
        if (flag == 1)
            System.err.println("Git");

        fastGuassianBlur(oldb, newb, width, height, sigma);
        fastGuassianBlur(oldg, newg, width, height, sigma);
        fastGuassianBlur(oldr, newr, width, height, sigma);

        for (int i = 0; i < pixels.length; i += 3) {
            pixels[i] = newb[i / 3];
            pixels[i + 1] = newg[i / 3];
            pixels[i + 2] = newr[i / 3];
        }

        DataBufferByte dataBuffer = (DataBufferByte) im.getRaster().getDataBuffer();

        // Skopiuj zmodyfikowane piksele do danych obrazu
        System.arraycopy(pixels, 0, dataBuffer.getData(), 0, pixels.length);

        // Przerysuj obraz (jeśli potrzebne)
        im.setData(im.getRaster());

        return im;
    }
}
