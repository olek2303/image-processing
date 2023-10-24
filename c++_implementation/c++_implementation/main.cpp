#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;

int main() {
    cv::Mat inputImage = cv::imread("input.jpeg");

    if (inputImage.empty()) {
        std::cerr << "Could not open or find the image." << std::endl;
        return -1;
    }

    cv::Mat blurredImage;
    cv::GaussianBlur(inputImage, blurredImage, cv::Size(5, 5), 0); // Gaussian Blur

    cv::imshow("Original Image", inputImage);
    cv::imshow("Blurred Image", blurredImage);

    cv::waitKey(0);
    return 0;
}