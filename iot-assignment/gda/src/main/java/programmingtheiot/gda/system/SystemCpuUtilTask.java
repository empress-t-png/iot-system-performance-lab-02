package programmingtheiot.gda.system;

import java.lang.management.ManagementFactory;
import java.lang.management.OperatingSystemMXBean;

public class SystemCpuUtilTask extends BaseSystemUtilTask {
    private OperatingSystemMXBean osBean;
    
    public SystemCpuUtilTask() {
        this.osBean = ManagementFactory.getOperatingSystemMXBean();
    }
    
    @Override
    public float getTelemetryValue() {
        double systemLoad = osBean.getSystemLoadAverage();
        if (systemLoad >= 0) {
            int availableProcessors = osBean.getAvailableProcessors();
            double loadPercentage = (systemLoad / availableProcessors) * 100.0;
            return (float) Math.min(loadPercentage, 100.0);
        }
        return 0.0f;
    }
}