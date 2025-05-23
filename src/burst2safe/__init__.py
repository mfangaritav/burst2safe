import logging
import sys


log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, format=log_format, level=logging.INFO, force=True)