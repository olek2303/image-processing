package img.processing;

public class Delete {
    public static int[] deleteArea(int[] imageData, int width, int height, int x, int y, int areaWidth, int areaHeight,
            int channels) {
        // Checking if area is possible to delete
        if (x < 0 || y < 0 || x + areaWidth > width || y + areaHeight > height) {
            System.err.println("The area extends beyond the image size.");
            return imageData;
        }

        int[] newImageData = imageData.clone();

        // Deleting area
        for (int i = y; i < y + areaHeight; i++) {
            for (int j = x; j < x + areaWidth; j++) {
                int index = (i * width + j) * channels;
                for (int c = 0; c < channels; c++) {
                    newImageData[index + c] = 255;
                }
            }
        }

        return newImageData;
    }
}