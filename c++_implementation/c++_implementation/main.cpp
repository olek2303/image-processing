#define _CRT_SECURE_NO_WARNINGS

#include "blur.hpp"
#include "image.hpp"



using namespace std;
using namespace std::chrono;

int main(int argc, char* argv[])
{

    // Image loading
    string fileName = "test.jpg"; //dorobiæ wczytywanie
   
    Image im(fileName);
    float blurSigma = 5; // moc rozmycia

    auto start = high_resolution_clock::now();

    blur_image(im, blurSigma);

    auto stop = high_resolution_clock::now();


    auto duration = duration_cast<microseconds>(stop - start);

    cout << "Time taken by function: " << duration.count() << " microseconds" << endl;

    im.save_image("blurImage.jpg");
    
   


    return 0;
}
