#include "image.hpp"

#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"

#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

Image::Image(string fileName) {
    unsigned char* _loadedImage = stbi_load(fileName.c_str(), &width, &height, &channels, 0);
    if (!_loadedImage)
    {
        cerr << "Error while loading the file. (Check the file name!)" << std::endl;
        exit(2);
    }
    if (channels < 3)
    {
        std::cout << "Input images must be RGB images." << std::endl;
        exit(1);
    }
    cout << "Loaded image: " << fileName << endl << width << " x " << height << " (" << channels << ")" << endl;
    imageData = _loadedImage;
}

void Image::save_image(string fileName) {
    string extension = "jpg"; //default extension is .jpg

    size_t i = fileName.rfind('.', fileName.length());
    if (i != string::npos) {
        extension = fileName.substr(i + 1, fileName.length() - i);
    }

    if (extension == "png")
        stbi_write_png(fileName.c_str(), width, height, channels, imageData, channels * width);
    else {
        cout << "Extension not supported. Image saved as a default .jpg file.";
        stbi_write_jpg(fileName.c_str(), width, height, channels, imageData, 100);
    }


    stbi_image_free(imageData);
}