package programmingtheiot.gda.system;

public class EnhancedSystemPerformanceManager {
    private EnhancedSystemCpuUtilTask cpuUtilTask;
    private EnhancedSystemMemUtilTask memUtilTask;
    private boolean isActive = false;
    private Thread monitorThread;
    private long pollRate = 5000;
    
    public EnhancedSystemPerformanceManager() {
        this.cpuUtilTask = new EnhancedSystemCpuUtilTask();
        this.memUtilTask = new EnhancedSystemMemUtilTask();
    }
    
    public EnhancedSystemPerformanceManager(long pollRate) {
        this();
        this.pollRate = pollRate;
    }
    
    public void startManager() {
        if (!isActive) {
            isActive = true;
            monitorThread = new Thread(this::runMonitoring);
            monitorThread.setDaemon(true);
            monitorThread.start();
            System.out.println("Enhanced GDA SystemPerformanceManager started");
        }
    }
    
    public void stopManager() {
        if (isActive) {
            isActive = false;
            if (monitorThread != null) {
                try {
                    monitorThread.join(2000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
            System.out.println("Enhanced GDA SystemPerformanceManager stopped");
        }
    }
    
    private void runMonitoring() {
        int iteration = 0;
        while (isActive) {
            try {
                iteration++;
                float cpuUtil = cpuUtilTask.getTelemetryValue();
                float memUtil = memUtilTask.getTelemetryValue();
                
                System.out.println("Enhanced Iteration " + iteration + ":");
                System.out.println("  CPU: " + String.format("%.1f", cpuUtil) + "%");
                System.out.println("  Memory: " + String.format("%.1f", memUtil) + "%");
                System.out.println("  " + "-".repeat(40));
                
                Thread.sleep(pollRate);
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
                try {
                    Thread.sleep(pollRate);
                } catch (InterruptedException ie) {
                    break;
                }
            }
        }
    }
}