import logging

from logging import handlers

class db_backupfilter(logging.Filter):

    def filter(self, record):
        return "db backup" in record.getMessage()



# 1. 生成 logger 对象
logger = logging.getLogger("web")

# she zhi level
logger.setLevel(logging.DEBUG)


# 1.1 把 filter 对象 添加  logger 中
logger.addFilter(db_backupfilter())

# 2. 生成 handler 对象
ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# fh = logging.FileHandler('web.log')
# fh = handlers.RotatingFileHandler('web.log',maxBytes=10,backupCount=3) # an daxiao filter
fh = handlers.TimedRotatingFileHandler('web,log',when='S',interval=5,backupCount=4)  # an time filter
# fh.setLevel(logging.WARNING)

# 2.1 把handler 对象  绑定到logger
logger.addHandler(ch)
logger.addHandler(fh)

# 3 生城 formatter 对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')

# 3.1 吧formatter 对象  绑定handler 对象
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)



logger.debug(msg='test log db backup ')
logger.debug(msg='test log  1')
logger.info(msg='test log 2')




