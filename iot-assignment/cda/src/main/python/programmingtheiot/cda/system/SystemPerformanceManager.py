import threading
import time
from SystemCpuUtilTask import SystemCpuUtilTask
from SystemMemUtilTask import SystemMemUtilTask

class SystemPerformanceManager:
    def __init__(self, pollRate=5):
        self.pollRate = pollRate
        self.cpuUtilTask = SystemCpuUtilTask()
        self.memUtilTask = SystemMemUtilTask()
        self.isActive = False
        self.thread = None
        
    def startManager(self):
        if not self.isActive:
            self.isActive = True
            self.thread = threading.Thread(target=self._run)
            self.thread.daemon = True
            self.thread.start()
            print("SystemPerformanceManager started")
            
    def stopManager(self):
        if self.isActive:
            self.isActive = False
            if self.thread:
                self.thread.join(timeout=2.0)
            print("SystemPerformanceManager stopped")
        
    def _run(self):
        while self.isActive:
            try:
                cpuUtil = self.cpuUtilTask.getTelemetryValue()
                memUtil = self.memUtilTask.getTelemetryValue()
                
                print(f"CPU Utilization: {cpuUtil:.1f}%")
                print(f"Memory Utilization: {memUtil:.1f}%")
                print("-" * 40)
                
                time.sleep(self.pollRate)
            except Exception as e:
                print(f"Error in performance manager: {e}")
                time.sleep(self.pollRate)