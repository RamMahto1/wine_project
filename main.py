from src.logger import logger
from src.excepation import CustomException
import sys 

def main():
    # print("MAIN.PY EXECUTED")  # Just to test
    # logger.info("Main started")
    # logger.info("Running model...")
    try:
        1 / 0  # example error
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()
