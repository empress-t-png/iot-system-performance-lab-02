import psutil
from BaseSystemUtilTask import BaseSystemUtilTask

class SystemCpuUtilTask(BaseSystemUtilTask):
    def getTelemetryValue(self) -> float:
        return psutil.cpu_percent(interval=1)