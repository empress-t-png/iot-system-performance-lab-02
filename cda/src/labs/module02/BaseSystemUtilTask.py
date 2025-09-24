"""
Base System Utility Task for CDA
PIOT-CDA-02-004: BaseSystemUtilTask module
"""

import abc

class BaseSystemUtilTask(abc.ABC):
    """
    Abstract base class for system utility tasks
    """
    
    def __init__(self):
        """
        Initialize the base task
        """
        self.name = "BaseSystemUtilTask"
        
    @abc.abstractmethod
    def getTelemetryValue(self):
        """
        Abstract method to get telemetry value
        Must be implemented by subclasses
        """
        pass