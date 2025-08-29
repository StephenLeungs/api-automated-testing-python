import logging
import logging.handlers
import os


def get_logger(log_name, time='D', count=1, filename=None, level="WARNING"):
    """
    创建并配置日志器

    Args:
        log_name (str): 日志器名称，通常使用类名或模块名
        time (str): 日志轮转时间单位，默认按天('D')
        count (int): 保留的备份文件数量
        filename (str): 日志文件路径，None表示只输出到控制台
        level (str): 日志级别，默认'WARNING'

    Returns:
        logging.Logger: 配置好的日志器实例
    """
    # 创建日志器
    logger = logging.getLogger(log_name)
    logger.setLevel(getattr(logging, level.upper()))

    # 避免重复添加处理器（防止在多次调用时创建重复处理器）
    if logger.handlers:
        return logger

    # 创建格式器 - 修改为期望的格式
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 创建控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 如果指定了文件名，创建文件处理器
    if filename:
        # 确保日志目录存在
        log_dir = os.path.dirname(filename)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # 创建按时间轮转的文件处理器
        file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=filename,
            when=time,
            backupCount=count,
            encoding='utf-8'  # 指定编码避免中文乱码
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
