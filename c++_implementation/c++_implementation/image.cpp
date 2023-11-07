#include "image.hpp"

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

Image::Image(int _width, int _height, int _channels) {
    width = _width;
    height = _height;
    channels = _channels;
    imageData = new unsigned char[width * height * _channels]();
}

Image::Image(string _fileName) {
    unsigned char* _loadedImage = stbi_load(_fileName.c_str(), &width, &height, &channels, 0);
    while (!_loadedImage)
    {
        cerr << "Error while loading the file. (Check the file name!)" << std::endl;
        cout << "Enter the file name: ";
        cin >> fileName;
        _loadedImage = stbi_load(fileName.c_str(), &width, &height, &channels, 0);
    }
    if (channels != 3)
    {
        std::cout << "Input images must be RGB images." << std::endl;
        exit(1);
    }
    cout << "Loaded image: " << fileName << endl << width << " x " << height << " (channels: " << channels << ")" << endl;
    fileName = _fileName;
    imageData = _loadedImage;
}

void Image::save_image(string fileName) {
    string extension = "jpg"; //default extension is .jpg

    size_t dotPosition = fileName.find_last_of('.');
    if (dotPosition != string::npos) {
        extension = fileName.substr(dotPosition + 1);
    }

    if (extension == "png")
        stbi_write_png(fileName.c_str(), width, height, channels, imageData, channels * width);
    else if(extension == "jpg")
        stbi_write_jpg(fileName.c_str(), width, height, channels, imageData, 100);
    else {
        cout << "Extension not supported. Image saved as a default .jpg file.";
        stbi_write_jpg(fileName.c_str(), width, height, channels, imageData, 100);
    }


    stbi_image_free(imageData);
}


