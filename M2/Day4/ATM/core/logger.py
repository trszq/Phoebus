import logging
from conf import settings

def logger(log_type):
    # 创建logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)
    # 创建输出到屏幕的handler
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)
    # 创建输出到文件的handler
    log_file="%s/logs/%s"%(settings.BASE_DIR,settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)
    fh.setLevel(settings.LOG_LEVEL)
    # 配置日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # logger添加handler
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger



