package programmingtheiot.gda.system;

import java.lang.management.ManagementFactory;
import java.lang.management.MemoryMXBean;
import java.lang.management.MemoryUsage;

public class SystemMemUtilTask extends BaseSystemUtilTask {
    private MemoryMXBean memoryBean;
    
    public SystemMemUtilTask() {
        this.memoryBean = ManagementFactory.getMemoryMXBean();
    }
    
    @Override
    public float getTelemetryValue() {
        MemoryUsage heapMemoryUsage = memoryBean.getHeapMemoryUsage();
        MemoryUsage nonHeapMemoryUsage = memoryBean.getNonHeapMemoryUsage();
        
        long usedMemory = heapMemoryUsage.getUsed() + nonHeapMemoryUsage.getUsed();
        long maxMemory = heapMemoryUsage.getMax() + nonHeapMemoryUsage.getMax();
        
        if (maxMemory > 0) {
            double memoryUsage = (usedMemory / (double) maxMemory) * 100.0;
            return (float) Math.min(memoryUsage, 100.0);
        }
        return 0.0f;
    }
}