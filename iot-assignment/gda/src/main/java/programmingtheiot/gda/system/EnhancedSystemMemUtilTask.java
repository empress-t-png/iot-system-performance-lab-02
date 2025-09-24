package programmingtheiot.gda.system;

import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;
import java.lang.reflect.Method;

public class EnhancedSystemMemUtilTask extends BaseSystemUtilTask {
    private OperatingSystemMXBean osBean;
    private Method physicalMemoryMethod;
    
    public EnhancedSystemMemUtilTask() {
        this.osBean = ManagementFactory.getOperatingSystemMXBean();
        
        // Try to get physical memory usage if available
        try {
            Class<?> clazz = Class.forName("com.sun.management.OperatingSystemMXBean");
            if (clazz.isInstance(osBean)) {
                physicalMemoryMethod = clazz.getMethod("getTotalPhysicalMemorySize");
            }
        } catch (Exception e) {
            physicalMemoryMethod = null;
        }
    }
    
    @Override
    public float getTelemetryValue() {
        // Try to get physical memory usage first
        if (physicalMemoryMethod != null) {
            try {
                long totalMemory = (Long) physicalMemoryMethod.invoke(osBean);
                long freeMemory = (Long) osBean.getClass()
                    .getMethod("getFreePhysicalMemorySize")
                    .invoke(osBean);
                
                if (totalMemory > 0) {
                    double memoryUsage = ((totalMemory - freeMemory) / (double) totalMemory) * 100.0;
                    return (float) Math.min(memoryUsage, 100.0);
                }
            } catch (Exception e) {
                // Fall back to heap memory usage
            }
        }
        
        // Fallback: use JVM heap memory (less accurate for system-wide memory)
        Runtime runtime = Runtime.getRuntime();
        long totalMemory = runtime.totalMemory();
        long freeMemory = runtime.freeMemory();
        long usedMemory = totalMemory - freeMemory;
        
        if (totalMemory > 0) {
            double memoryUsage = (usedMemory / (double) totalMemory) * 100.0;
            return (float) Math.min(memoryUsage, 100.0);
        }
        
        return 0.0f;
    }
}