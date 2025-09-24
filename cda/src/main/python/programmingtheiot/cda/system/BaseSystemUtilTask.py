import abc

class BaseSystemUtilTask(abc.ABC):
    @abc.abstractmethod
    def getTelemetryValue(self) -> float:
        pass