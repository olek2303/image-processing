#include "merge.hpp"

Image mergeImages(Image im1, Image im2, double alpha) {
    Image blended("test1.jpg");
    for (int i = 0; i < blended.width * blended.height * 3; i++) {
        blended.imageData[i] = static_cast<unsigned char>(
            alpha * im1.imageData[i] + (1.0 - alpha) * im2.imageData[i]
            );
    }
    return blended;
}
