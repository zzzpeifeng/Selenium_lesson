import logging
import os
import time
import getcwd


def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间，转换为设置格式
    rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))

    # 设置所有日志和错误日志存放路径
    path = getcwd.getcwd()
    # 通过绝对路径拼接日志存放路径
    all_log_path = os.path.join(path, 'logs/logs/ALL_Logs/')
    error_log_path = os.path.join(path, 'logs/logs/ERROR_Logs/')

    # 设置日志文件名
    all_log_name = all_log_path + rq + ".log"
    error_log_name = error_log_path + rq + ".log"

    # 创建handler
    # 创建一个handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)
    # 创建一个handler写入错误日志
    eh = logging.FileHandler(error_log_name)
    eh.setLevel(logging.ERROR)

    # 创建一个handler输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # 定义日志输出格式
    # 以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 以时间-日志名称-日志级别-文件名-函数行号-错误内容
    error_log_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    return logger

log1 = get_log("selenium")
