package programmingtheiot.gda.system;

import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
import java.lang.reflect.Method;

public class EnhancedSystemCpuUtilTask extends BaseSystemUtilTask {
    private OperatingSystemMXBean osBean;
    private Method systemCpuLoadMethod;
    
    public EnhancedSystemCpuUtilTask() {
        this.osBean = ManagementFactory.getOperatingSystemMXBean();
        
        // Try to get more accurate CPU usage if available
        try {
            Class<?> clazz = Class.forName("com.sun.management.OperatingSystemMXBean");
            if (clazz.isInstance(osBean)) {
                systemCpuLoadMethod = clazz.getMethod("getSystemCpuLoad");
            }
        } catch (Exception e) {
            systemCpuLoadMethod = null;
        }
    }
    
    @Override
    public float getTelemetryValue() {
        // Try to get more accurate CPU usage first
        if (systemCpuLoadMethod != null) {
            try {
                double cpuUsage = (Double) systemCpuLoadMethod.invoke(osBean);
                return (float) (cpuUsage * 100.0);
            } catch (Exception e) {
                // Fall back to system load average
            }
        }
        
        // Fallback: use system load average
        double systemLoad = osBean.getSystemLoadAverage();
        if (systemLoad >= 0) {
            int availableProcessors = osBean.getAvailableProcessors();
            double loadPercentage = (systemLoad / availableProcessors) * 100.0;
            return (float) Math.min(loadPercentage, 100.0);
        }
        
        return 0.0f;
    }
}