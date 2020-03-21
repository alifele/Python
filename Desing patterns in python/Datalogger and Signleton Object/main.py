import Message_LOG as ML

logger = ML.Data_Logger('Data_log_class.txt')

logger.critical('critical. you should remove it')

logger.debug('there is a bug here. please debug it')

logger.error('this is a error. please fix this')

logger.warning('It is just a warning. you can ignore it')

logger.info('it is for extra information')



try:
    a = 1/0

except :

    logger.error("Devision by zero!!!")
