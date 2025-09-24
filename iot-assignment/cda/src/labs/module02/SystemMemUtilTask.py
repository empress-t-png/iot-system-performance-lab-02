"""
System Memory Utilization Task for CDA
PIOT-CDA-02-006: SystemMemUtilTask module
"""

import psutil
from labs.module02 import BaseSystemUtilTask
import logging

class SystemMemUtilTask(BaseSystemUtilTask.BaseSystemUtilTask):
    """
    Task for monitoring memory utilization
    """
    
    def __init__(self):
        """
        Initialize the memory utilization task
        """
        super().__init__()
        self.name = "SystemMemUtilTask"
        self.logger = logging.getLogger(__name__)
        
    def getTelemetryValue(self):
        """
        Get current memory utilization percentage
        """
        try:
            memory = psutil.virtual_memory()
            mem_util = memory.percent
            self.logger.debug("Memory Utilization: %.2f%%", mem_util)
            return mem_util
        except Exception as e:
            self.logger.error("Error getting memory utilization: %s", e)
            return 0.0