import logging
# logging.basicConfig(filename="demo.txt", filemode='a',level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
f = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s','%Y-%m-%d %H:%M:%S')
fh = logging.FileHandler('demo.log')
fh.setFormatter(f)
logger.addHandler(fh)
logging.info("Start to save")

def saveData(filename,value1,operation,value2,result):
    logger.debug(f'saving details of {filename}..')
    with open('demo.log','a') as appendFile:
        appendFile.write(f'Filename:{filename} - Value1:{value1}, Operation:{operation}, Value2:{value2} - Result:{result}\n')
    return appendFile
logger.info(f"Details saved successfully")
