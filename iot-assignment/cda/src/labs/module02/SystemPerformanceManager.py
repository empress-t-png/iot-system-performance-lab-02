"""
System Performance Manager for CDA
PIOT-CDA-02-002: SystemPerformanceManager module
"""

import logging
import threading
import time

class SystemPerformanceManager:
    """
    Manages system performance monitoring tasks
    """
    
    def __init__(self, pollCycleSecs = 10):
        """
        Initialize the System Performance Manager
        """
        self.pollCycleSecs = pollCycleSecs
        self.enableSystemPerformance = True
        self.scheduler_thread = None
        self.cpu_task = None
        self.mem_task = None
        
        # Initialize logger
        self.logger = logging.getLogger(__name__)
        
    def startManager(self):
        """
        Start the system performance manager
        """
        self.logger.info("Starting System Performance Manager...")
        
        # Import tasks here to avoid circular imports
        from labs.module02 import SystemCpuUtilTask, SystemMemUtilTask
        
        # Initialize tasks
        self.cpu_task = SystemCpuUtilTask.SystemCpuUtilTask()
        self.mem_task = SystemMemUtilTask.SystemMemUtilTask()
        
        # Start scheduler thread
        self.scheduler_thread = threading.Thread(target=self._schedulerLoop)
        self.scheduler_thread.daemon = True
        self.scheduler_thread.start()
        
        self.logger.info("System Performance Manager started with poll cycle: %d seconds", self.pollCycleSecs)
        
    def stopManager(self):
        """
        Stop the system performance manager
        """
        self.logger.info("Stopping System Performance Manager...")
        self.enableSystemPerformance = False
        
        if self.scheduler_thread and self.scheduler_thread.is_alive():
            self.scheduler_thread.join(timeout=5)
            
        self.logger.info("System Performance Manager stopped.")
        
    def _schedulerLoop(self):
        """
        Scheduler loop for periodic task execution
        """
        while self.enableSystemPerformance:
            try:
                # Run performance tasks
                if self.cpu_task:
                    cpu_util = self.cpu_task.getTelemetryValue()
                    self.logger.info("CPU Utilization: %.2f%%", cpu_util)
                    
                if self.mem_task:
                    mem_util = self.mem_task.getTelemetryValue()
                    self.logger.info("Memory Utilization: %.2f%%", mem_util)
                    
            except Exception as e:
                self.logger.error("Error in scheduler loop: %s", e)
                
            # Wait for next cycle
            time.sleep(self.pollCycleSecs)