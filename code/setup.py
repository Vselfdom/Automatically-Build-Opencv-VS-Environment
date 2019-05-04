#coding UTF-8
#author PE
from PyInstaller.__main__ import run
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    opts = ['-F',
            '-w',
            '-y',
            '--paths=E:\\PythonCode\\demo\\dist\\platforms',
            '--clean',
            # '--icon=calculator.ico',
            'main.py']
    run(opts)