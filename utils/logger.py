from enum import Enum

class Logger:

    def __init__(self) -> None:
        pass

    def log(self, str, logLevel: 'LogLevel') -> None:
        if not isinstance(logLevel, LogLevel):
            raise TypeError("logLevel must be an instance of LogLevel() enum !\nFailed to log line.")
        print(logLevel.value, ":",  str)

class LogLevel(Enum):

    INFO = "INFO"
    FINE = "FINE"
    WARNING = "WARN"
    ERROR = "ERROR"
    SEVERE = "SEVERE"
    CRITICAL = "CRITICAL"