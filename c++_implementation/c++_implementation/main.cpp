#define _CRT_SECURE_NO_WARNINGS

#include "blur.hpp"
#include "image.hpp"
#include "merge.hpp"


using namespace std;
using namespace std::chrono;

int main(int argc, char* argv[])
{

    cout << "Options:" << endl;
    cout << "1. Blurring" << endl;
    cout << "2. Merging" << endl;

    cout << endl;
    cout << "Choose option..." << endl;
    int i = NULL;
    cin >> i;

	if(i == 1) {
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
	}
	else if (i == 2) {
		Image im1("test2.jpg");
		Image im2("test.jpg");
		double alpha = 0.4;

		auto start1 = high_resolution_clock::now();
		Image merged = mergeImages(im1, im2, alpha);
		auto stop1 = high_resolution_clock::now();

		auto duration1 = duration_cast<microseconds>(stop1 - start1);
		cout << "Time taken by function: " << duration1.count() << " microseconds" << endl;
		merged.save_image("mergedImage.jpg");
	}
	else {
		cout << "Wrong number!" << endl;
	}

    return 0;
}
