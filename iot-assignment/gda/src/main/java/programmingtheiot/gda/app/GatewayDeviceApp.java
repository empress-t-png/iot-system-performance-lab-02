package programmingtheiot.gda.app;

import programmingtheiot.gda.system.SystemPerformanceManager;

public class GatewayDeviceApp {
    private SystemPerformanceManager sysPerfManager;
    
    public GatewayDeviceApp() {
        System.out.println("Initializing GDA...");
        this.sysPerfManager = new SystemPerformanceManager(5000);
    }
    
    public void startApp() {
        System.out.println("Starting GDA...");
        this.sysPerfManager.startManager();
    }
    
    public void stopApp() {
        System.out.println("Stopping GDA...");
        this.sysPerfManager.stopManager();
    }
    
    public static void main(String[] args) {
        GatewayDeviceApp app = new GatewayDeviceApp();
        try {
            app.startApp();
            Thread.sleep(30000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            app.stopApp();
            System.out.println("GDA stopped.");
        }
    }
}