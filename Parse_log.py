import logging
logging.basicConfig(filename='log.txt',filemode='a',level=logging.DEBUG)
logging.debug('this is a debug message')
logging.warning('this s warning')
logger = logging.getLogger(__name__)


