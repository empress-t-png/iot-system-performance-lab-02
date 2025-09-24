import psutil
from BaseSystemUtilTask import BaseSystemUtilTask

class SystemMemUtilTask(BaseSystemUtilTask):
    def getTelemetryValue(self) -> float:
        memory = psutil.virtual_memory()
        return memory.percent