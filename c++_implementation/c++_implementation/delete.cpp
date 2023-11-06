// Connected with the delete.h file.
#include "delete.hpp"

void delete_area(Image& im, int x, int y, int width, int height)
{
    //  Function delete area specified by the user. (x,y) are trated as a point to delete. 
    //  : param x : x parameter of point(x,y)
    //  : param y : y parameter of point(x,y)
    //  : param width : width chosen to delete
    //  : param height : height chosen to delete
    //  : return : null -> void function

  //Checking if area is possible to delete
    if (x < 0 || y < 0 || x + width > im.width || y + height > im.height)
    {
        std::cerr << "The area extends beyond the image size." << std::endl;
        return;
    }

    // Deleting area
    for (int i = y; i < y + height; i++)
    {
        for (int j = x; j < x + width; j++)
        {
            int index = (i * im.width + j) * im.channels;
            for (int c = 0; c < im.channels; c++)
            {
                im.imageData[index + c] = 255;
            }
        }
    }
}