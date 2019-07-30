import os

def getcwd():
    """返回当前文件的绝对路径"""
    path = os.path.dirname(os.path.abspath(__file__))
    return path
