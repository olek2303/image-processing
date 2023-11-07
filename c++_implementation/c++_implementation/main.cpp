#define _CRT_SECURE_NO_WARNINGS

#include "blur.hpp"
#include "image.hpp"
#include "merge.hpp"
#include "delete.hpp"
#include "timer.hpp"

using namespace std;

string ask_file_name() {
    cout << "Enter the file name with extension (or full path if file is in the other directory): " << endl;
    string fileName;
    cin >> fileName;
    return fileName;
}

int main(int argc, char* argv[])
{
    int i = 0;
    Timer timerT;

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
            Image im(ask_file_name());
            cout << "Insert blur radius (from 0 to 10): ";
            float blurSigma; // moc rozmycia
            cin >> blurSigma;
            while (blurSigma < 0 || blurSigma > 10) {
                cout << "Wrong blur radius!";
                cout << "Insert blur radius (from 0 to 10): ";
                cin >> blurSigma;
            }

            timerT.start();
            blur_image(im, blurSigma);
            timerT.stop();
            
            string output = im.fileName + "_blur.jpg";
            im.save_image(output);
        }
        else if (i == 2)
        {
            Image im1(ask_file_name());
            Image im2(ask_file_name());
            
            cout << "Enter alpha value for marging(from 0.0 to 1.0):  ";
            double alpha;
            cin >> alpha;
            while (alpha < 0.0 || alpha > 1.0) {
                cout << "Wrong alpha value!" << endl;
                cout << "Enter alpha value for marging(from 0.0 to 1.0):  ";
                cin >> alpha;
            }


            timerT.start();
            Image merged = mergeImages(im1, im2, alpha);
            timerT.stop();

            merged.save_image(im1.fileName + im2.fileName + "_merged.jpg");
        }
        else if (i == 3)
        {
            Image im3(ask_file_name());
            int x, y, width, height;
            cout << "Enter the x value - upper left corner of the area to be removed: ";
            cin >> x;
            cout << "Enter the y value - upper left corner of the area to be removed: ";
            cin >> y;
            cout << "Enter the width of the area which is going to be removed: ";
            cin >> width;
            cout << "Enter the height of the area which is going to be removed: ";
            cin >> height;
            timerT.start();
            delete_area(im3, x, y, width, height);
            timerT.stop();

            im3.save_image(im3.fileName + "_delete.jpg");
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
