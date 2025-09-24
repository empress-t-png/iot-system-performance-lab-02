"""
System CPU Utilization Task for CDA
PIOT-CDA-02-005: SystemCpuUtilTask module
"""

import psutil
from labs.module02 import BaseSystemUtilTask
import logging

class SystemCpuUtilTask(BaseSystemUtilTask.BaseSystemUtilTask):
    """
    Task for monitoring CPU utilization
    """
    
    def __init__(self):
        """
        Initialize the CPU utilization task
        """
        super().__init__()
        self.name = "SystemCpuUtilTask"
        self.logger = logging.getLogger(__name__)
        
    def getTelemetryValue(self):
        """
        Get current CPU utilization percentage
        """
        try:
            cpu_util = psutil.cpu_percent(interval=1)
            self.logger.debug("CPU Utilization: %.2f%%", cpu_util)
            return cpu_util
        except Exception as e:
            self.logger.error("Error getting CPU utilization: %s", e)
            return 0.0