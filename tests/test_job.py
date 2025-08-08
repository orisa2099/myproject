# tests/test_job.py
import sys
import os
import logging

logging.basicConfig(filename="C:\\Users\\orisa\\Documents\\myproject\\testresult.log",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#etl = "C:\\Users\\orisa\\Documents\\myproject\\etl"

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(parent_dir, "etl"))

#if etl not in sys.path:
#    sys.path.append(etl)


from job import *

def test_transform():
    if transform([1, 2]) == [2, 4]:
        logging.info("Test Passed")
    else:
        logging.error("Test Failed")

if __name__ == "__main__":
    test_transform() 
    
    #logging.INFO(assert transform([1, 2]) == [2, 4])
