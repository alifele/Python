'''
def critical(message):
    with open('Data_Log.txt', 'a') as logfile:
        logfile.write('[CRITICAL]{0}\n'.format(message))


def error(message):
    with open('Data_Log.txt', 'a') as logfile:
        logfile.write('[ERROR]{0}\n'.format(message))


def warning(message):
    with open('Data_Log.txt', 'a') as logfile:
        logfile.write('[WARNING]{0}\n'.format(message))


def info(message):
    with open('Data_Log.txt', 'a') as logfile:
        logfile.write('[INFO]{0}\n'.format(message))


def debug(message):
    with open('Data_Log.txt', 'a') as logfile:
        logfile.write('[DEGUB]{0}\n'.format(message))

'''


# Here is another way to implement

'''

def message_log(level, message):
    with open('Data_Log.txt', 'a') as logfile:
        logfile.write('[{0}] {1}\n'.format(level, message))


def critical(message):
    message_log('CRITICAL', message)

def info(message):
    message_log('INFO', message)

def error(message):
    message_log('ERROR', message)

def warning(message):
    message_log('WARNING', message)

def debug(message):
    message_log('DEBUG', message)


'''

class Data_Logger():
    def __init__ (self, filename):
        self.filename = filename

    def _message_log(self, level, message):
        with open('Data_Log.txt', 'a') as logfile:
            logfile.write('[{0}] {1}\n'.format(level, message))


    def critical(self,message):
        self.message_log('CRITICAL', message)

    def info(self,message):
        self.message_log('INFO', message)

    def error(self, message):
        self.message_log('ERROR', message)

    def warning(self,message):
        self.message_log('WARNING', message)

    def debug(self,message):
        self.message_log('DEBUG', message)









if __name__ == '__main__':
    LOGFILE('Hello ali How are you')
    LOGFILE('By the way! How you are going to participate?')
