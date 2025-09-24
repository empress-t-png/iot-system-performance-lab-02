package programmingtheiot.gda.app;

import programmingtheiot.gda.system.EnhancedSystemPerformanceManager;

public class EnhancedGatewayDeviceApp {
    private EnhancedSystemPerformanceManager sysPerfManager;
    
    public EnhancedGatewayDeviceApp() {
        System.out.println("Initializing Enhanced GDA...");
        this.sysPerfManager = new EnhancedSystemPerformanceManager(5000);
    }
    
    public void startApp() {
        System.out.println("Starting Enhanced GDA...");
        this.sysPerfManager.startManager();
    }
    
    public void stopApp() {
        System.out.println("Stopping Enhanced GDA...");
        this.sysPerfManager.stopManager();
    }
    
    public static void main(String[] args) {
        EnhancedGatewayDeviceApp app = new EnhancedGatewayDeviceApp();
        try {
            app.startApp();
            Thread.sleep(30000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            app.stopApp();
            System.out.println("Enhanced GDA stopped.");
        }
    }
}