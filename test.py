from utils import logger
import numpy as np
from utils import maths_utils as math
from chessconfig import chessconfig
import time

log = logger.Logger()
logLevel = logger.LogLevel
log.log("Starting ChessEngine IA made by JourBoon", logLevel.INFO)
for i in range (0,4):  
    b = "Loading" + "." * i
    print (b, end="\r")
    time.sleep(0.5)

config = chessconfig.ChessConfig("config")
config_data = config.createFile()

print("Données lues:")
print(config_data)