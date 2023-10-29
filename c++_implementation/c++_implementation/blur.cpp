
#include "blur.hpp"

void boxes_for_gauss(int boxes[], float sigma, int n)
{
    // ideal filter width
    float wi = std::sqrt((12 * sigma * sigma / n) + 1);
    int wl = std::floor(wi);
    if (wl % 2 == 0) wl--;
    int wu = wl + 2;

    float mi = (12 * sigma * sigma - n * wl * wl - 4 * n * wl - 3 * n) / (-4 * wl - 4);
    int m = std::round(mi);

    for (int i = 0; i < n; i++)
        boxes[i] = ((i < m ? wl : wu) - 1) / 2;
}

void horizontal_blur(float* in, float* out, int w, int h, int r)
{
    float iarr = 1.f / (r + r + 1);
//#pragma omp parallel for
    for (int i = 0; i < h; i++)
    {
        int ti = i * w, li = ti, ri = ti + r;
        float fv = in[ti];
        float lv = in[ti + w - 1];
        float val = (r + 1) * fv;

        for (int j = 0; j < r; j++)
            val += in[ti + j];
        for (int j = 0; j <= r; j++) {
            val += in[ri++] - fv; out[ti++] = val * iarr;
        }
        for (int j = r + 1; j < w - r; j++) {
            val += in[ri++] - in[li++]; out[ti++] = val * iarr;
        }
        for (int j = w - r; j < w; j++) {
            val += lv - in[li++]; out[ti++] = val * iarr; 
        }
    }
}

void total_blur(float* in, float* out, int w, int h, int r)
{
    float iarr = 1.f / (r + r + 1);
//#pragma omp parallel for
    for (int i = 0; i < w; i++)
    {
        int ti = i, li = ti, ri = ti + r * w;
        float fv = in[ti]; 
        float lv = in[ti + w * (h - 1)]; 
        float val = (r + 1) * fv;
        for (int j = 0; j < r; j++) 
            val += in[ti + j * w];
        for (int j = 0; j <= r; j++) { 
            val += in[ri] - fv; out[ti] = val * iarr; ri += w; ti += w; 
        }
        for (int j = r + 1; j < h - r; j++) { 
            val += in[ri] - in[li]; out[ti] = val * iarr; li += w; ri += w; ti += w; 
        }
        for (int j = h - r; j < h; j++) {
            val += lv - in[li]; out[ti] = val * iarr; li += w; ti += w; 
        }
    }
}

void box_blur(float*& in, float*& out, int w, int h, int r)
{
    std::swap(in, out);
    horizontal_blur(out, in, w, h, r);
    total_blur(in, out, w, h, r);
}

void fast_gaussian_blur(float*& in, float*& out, int w, int h, float sigma)
//in obraz wczytywany, out zapisywany, w width, h height, sigma promieñ rozmycia
{
    int boxes[3];
    boxes_for_gauss(boxes, sigma, 3);
    box_blur(in, out, w, h, boxes[0]);
    box_blur(out, in, w, h, boxes[1]);
    box_blur(in, out, w, h, boxes[2]);
}

void blur_image(Image im, float sigma) {
    // copy data
    int size = im.width * im.height;

    // output channels r,g,b
    float* newb = new float[size];
    float* newg = new float[size];
    float* newr = new float[size];

    // input channels r,g,b
    float* oldb = new float[size];
    float* oldg = new float[size];
    float* oldr = new float[size];

    // channels copy r,g,b
    for (int i = 0; i < size; ++i)
    {
        oldb[i] = im.imageData[im.channels * i + 0] / 255.f;
        oldg[i] = im.imageData[im.channels * i + 1] / 255.f;
        oldr[i] = im.imageData[im.channels * i + 2] / 255.f;
    }


    fast_gaussian_blur(oldb, newb, im.width, im.height, sigma);
    fast_gaussian_blur(oldg, newg, im.width, im.height, sigma);
    fast_gaussian_blur(oldr, newr, im.width, im.height, sigma);

    for (int i = 0; i < size; ++i)
    {
        im.imageData[im.channels * i + 0] = (unsigned char)min(255.f, max(0.f, 255.f * newb[i]));
        im.imageData[im.channels * i + 1] = (unsigned char)min(255.f, max(0.f, 255.f * newg[i]));
        im.imageData[im.channels * i + 2] = (unsigned char)min(255.f, max(0.f, 255.f * newr[i]));
    }

    delete[] newr;
    delete[] newb;
    delete[] newg;
    delete[] oldr;
    delete[] oldb;
    delete[] oldg;

}
