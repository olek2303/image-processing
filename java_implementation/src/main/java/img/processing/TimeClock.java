package img.processing;

public class TimeClock {
    long ti;

    public TimeClock() {
        ti = 0;
    }

    public void start() {
        ti = System.nanoTime();
    }

    public void stop() {
        long stop = System.nanoTime();
        long elapsed = (long) ((stop - ti) * 0.001);
        System.out.println("Elapsed time: " + elapsed + " ms \n");
    }

}
