from Message_LOG import Data_Logger


logger = Data_Logger('Data_Log.txt')

logger._message_log('important', 'hello there')
