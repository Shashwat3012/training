package Multithreading;

import java.util.concurrent.*;

public class MultithreadingDemo {

    // === Volatile keyword demo ===
    volatile boolean isRunning = true;

    // === Instance variable shared among threads ===
    int unsafeCounter = 0;
    int safeCounter = 0;

    // === Thread-safe increment using synchronized method ===
    public synchronized void incrementSafely() {
        safeCounter++;
    }

    // === Synchronized block demo ===
    public void incrementWithBlock() {
        synchronized (this) {
            safeCounter++;
        }
    }

    // === Simple Runnable with local and instance variables ===
    class CounterTask implements Runnable {
        public void run() {
            int localCounter = 0; // thread-safe

            for (int i = 0; i < 10000; i++) {
                localCounter++;         // safe
                unsafeCounter++;        // not thread-safe
                incrementSafely();      // safe
                incrementWithBlock();   // also safe
            }

            System.out.println(Thread.currentThread().getName() + " finished. Local count: " + localCounter);
        }
    }

    // === Volatile keyword usage thread ===
    class VolatileWorker extends Thread {
        public void run() {
            System.out.println("VolatileWorker started");
            while (isRunning) {
                // wait until flag is flipped
            }
            System.out.println("VolatileWorker stopped");
        }
    }

    // === Demonstrating ThreadPoolExecutor ===
    class PoolTask implements Runnable {
        String name;

        PoolTask(String name) {
            this.name = name;
        }

        public void run() {
            System.out.println("Executing: " + name + " by " + Thread.currentThread().getName());
            try { Thread.sleep(100); } catch (InterruptedException ignored) {}
            System.out.println("Completed: " + name);
        }
    }

    public static void main(String[] args) throws InterruptedException {
    	MultithreadingDemo demo = new MultithreadingDemo();

        // === Volatile demo ===
        VolatileWorker vw = demo.new VolatileWorker();
        vw.start();
        Thread.sleep(300);
        demo.isRunning = false;
        vw.join();
        System.out.println();

        // === Multithreading (unsafe vs safe vars) ===
        Thread t1 = new Thread(demo.new CounterTask(), "T1");
        Thread t2 = new Thread(demo.new CounterTask(), "T2");
        t1.start();
        t2.start();
        t1.join();
        t2.join();
        System.out.println();
        
        System.out.println("Unsafe Counter (not thread-safe): " + demo.unsafeCounter);
        System.out.println("Safe Counter (synchronized): " + demo.safeCounter);
        System.out.println();
        
        // === ThreadPoolExecutor ===
        ExecutorService executor = Executors.newFixedThreadPool(3);
        for (int i = 1; i <= 5; i++) {
            executor.submit(demo.new PoolTask("Task " + i));
        }
        executor.shutdown();
        executor.awaitTermination(2, TimeUnit.SECONDS);
    }
}
