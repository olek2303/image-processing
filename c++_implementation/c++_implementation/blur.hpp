#ifndef BLUR_HPP
#define BLUR_HPP



#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cmath>
#include <chrono>

#ifndef image_hpp
#define image_hpp
#include "image.hpp"
#endif // !image_hpp

void boxes_for_gauss(int boxes[], float sigma, int n);
void horizontal_blur(float* in, float* out, int w, int h, int r);
void total_blur(float* in, float* out, int w, int h, int r);
void box_blur(float*& in, float*& out, int w, int h, int r);
void fast_gaussian_blur(float*& in, float*& out, int w, int h, float sigma);
void blur_image(Image im, float sigma);

#endif // !BLUR_HPP