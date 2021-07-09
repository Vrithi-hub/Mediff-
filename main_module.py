import logging


logging.basicConfig(filename='log.txt',filemode='w',level=logging.DEBUG)
logging.debug('this is a debug message')
logging.warning('this is warning')
logging.error('this is error')
logger = logging.getLogger(__name__)
with open('log.txt', "rb") as f:
    for line in f:
        stripped_line=line.strip()
        print(stripped_line)

logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
# create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handler to the logger
logger.addHandler(handler)


