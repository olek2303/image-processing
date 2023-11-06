#define _CRT_SECURE_NO_WARNINGS

#include "blur.hpp"
#include "image.hpp"
#include "merge.hpp"
#include "delete.hpp"

using namespace std;
using namespace std::chrono;

int main(int argc, char* argv[])
{
    int i = 0;

    while (i != 4)
    {
        cout << "Options:" << endl;
        cout << "1. Blurring" << endl;
        cout << "2. Merging" << endl;
        cout << "3. Deleting" << endl;
        cout << "4. Quit" << endl;

        cout << "Choose an option from 1-4" << endl;
        cin >> i;

        if (i == 1)
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
        }
        else if (i == 2)
        {
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
        else if (i == 3)
        {
            Image im3("test.jpg");
            int x, y, width, height;
            cout << "Enter the x value - upper left corner of the area to be removed: ";
            cin >> x;
            cout << "Enter the y value - upper left corner of the area to be removed: ";
            cin >> y;
            cout << "Enter the width of the area which is going to be removed: ";
            cin >> width;
            cout << "Enter the height of the area which is going to be removed: ";
            cin >> height;
            auto start2 = high_resolution_clock::now();
            delete_area(im3, x, y, width, height);
            im3.save_image("deleted_area_image.jpg");
            auto stop2 = high_resolution_clock::now();
            auto duration2 = duration_cast<microseconds>(stop2 - start2);
            cout << "Time taken by function: " << duration2.count() << " microseconds" << endl;
        }
        else if (i == 4)
        {
            cout << "The program has finished his work." << endl;
        }
        else
            cout << "You have chosen the wrong number. Please try again." << endl;
        continue;
    }

    return 0;
}
