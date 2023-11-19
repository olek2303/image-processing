package img.processing;

public class Timer {
    long start;

    public void start() {
        start = System.nanoTime();
    }

    public void stop() {
        long stop = System.nanoTime();
        long elapsed = (long) ((stop - start) * 0.001);
        System.out.println("Elapsed time: " + elapsed + " ms \n");
    }

}
