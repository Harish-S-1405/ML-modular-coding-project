import logging
import os,sys
from datetime import datetime

LOG_DIR = "Logs"
LOG_DIR =os.path.join(os.getcwd(),LOG_DIR)

os.makedirs(LOG_DIR,exist_ok=True)

# .log  log_2023_o4_01_hh_mm_ss

CURREENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURREENT_TIME_STAMP}.log"

log_file_path = os.path.join(LOG_DIR,file_name)

logging.basicConfig(filename = log_file_path ,
                    filemode = "w",
                    format = '[%(asctime)s] %(name)s -%(levelname)s - %(message)s',
                    level = logging.INFO )

