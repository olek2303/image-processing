#ifndef IMAGE_HPP
#define IMAGE_HPP

#define _CRT_SECURE_NO_WARNINGS

#include <string>
#include <iostream>


using namespace std;
class Image {
public:
	int width;
	int height;
	int channels;
	string fileName;
	unsigned char* imageData;
	Image(string fileName);
	Image(int _width, int _height, int _channels);
	void save_image(string fileName);
};

#endif //IMAGE_HPP