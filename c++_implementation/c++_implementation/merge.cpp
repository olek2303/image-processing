#include "merge.hpp"


Image mergeImages(Image im1, Image im2, double alpha) {
   

    int mergedW = std::max(im1.width, im2.width);
    int mergedH = std::max(im1.height, im2.height);
    Image* merged = new Image(mergedW, mergedH, 3);

    int size1 = im1.width * im1.height * 3;
    int size2 = im2.width * im2.height * 3;


    if(size1 > size2) {
        // Copy first image to output image
        for (int y = 0; y < im1.height; y++) {
            for (int x = 0; x < im1.width; x++) {
                int srcIndex = (y * im1.width + x) * 3;
                int destIndex = (y * mergedW + x) * 3;
                for (int c = 0; c < 3; c++) {
                    merged->imageData[destIndex + c] = im1.imageData[srcIndex + c];
                }
            }
        }
        // Merge images with proper resolution
        for (int y = 0; y < im2.height; y++) {
            for (int x = 0; x < im2.width; x++) {
                int srcIndex = (y * im2.width + x) * 3;
                int destIndex = (y * mergedW + x) * 3;
                for (int c = 0; c < 3; c++) {
                    merged->imageData[destIndex + c] = ((im1.imageData[destIndex + c] * (1.0 - alpha)) + (im2.imageData[srcIndex + c] * alpha));
                }
            }
        }
    }

    else {
        // Kopiuj zawartoœæ pierwszego obrazu do obrazu wynikowego
        for (int y = 0; y < im2.height; y++) {
            for (int x = 0; x < im2.width; x++) {
                int srcIndex = (y * im2.width + x) * 3;
                int destIndex = (y * mergedW + x) * 3;
                for (int c = 0; c < 3; c++) {
                    merged->imageData[destIndex + c] = im2.imageData[srcIndex + c];
                }
            }
        }
        for (int y = 0; y < im1.height; y++) {
            for (int x = 0; x < im1.width; x++) {
                int srcIndex = (y * im1.width + x) * 3;
                int destIndex = (y * mergedW + x) * 3;
                for (int c = 0; c < 3; c++) {
                    merged->imageData[destIndex + c] = ((im2.imageData[destIndex + c] * (1.0 - alpha)) + (im1.imageData[srcIndex + c] * alpha));
                }
            }
        }
    }
    
    return *merged;
}
