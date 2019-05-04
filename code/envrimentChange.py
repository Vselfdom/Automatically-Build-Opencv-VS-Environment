#coding UTF-8
#author PE
from __future__ import print_function
import os
import sys
from subprocess import check_call
import ctypes
import _thread

if sys.hexversion > 0x03000000:
    import winreg
else:
    import _winreg as winreg

import subprocess


def run_cmd(cmd, cwd=None, runas=None):
    u"""
    运行cmd命令。
    """
    if not sys.platform.startswith('win') and runas and runas != 'root':
        cmd = 'su - {} -c "{}"'.format(runas, cmd)
    # logger.info(cmd)
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT,
                            shell=True,
                            cwd=cwd)
    return proc


def get_output(cmd, cwd=None, wait=True, runas=None):
    u"""
    获得命令执行后的标准输出或错误输出。
    """
    proc = run_cmd(cmd, cwd=cwd, runas=runas)
    lines = []
    if wait:
        while proc.poll() is None:
            if proc.stdout:
                lines.extend(proc.stdout.readlines())
    lines.extend(proc.stdout.readlines())
    return lines

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
def changemd():
    try:
        check_call(
            '''\"%s" -c "import win32api, win32con;assert win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE,0, 'Environment')"''' % sys.executable)
    except subprocess.CalledProcessError:
        return


class Win32Environment:
    """Utility class to get/set windows environment variable"""

    def __init__(self, scope):
        # assert scope in ('user', 'system')
        self.scope = scope
        if scope == 'user':
            self.root = winreg.HKEY_CURRENT_USER
            self.subkey = 'Environment'
        else:
            self.root = winreg.HKEY_LOCAL_MACHINE
            self.subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

    def search(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        # if is_admin():
        #     key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        # else:
        #     if sys.version_info[0] == 3:
        #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

        key_value = ''
        try:
            i = 0
            while i >= 0:
                key_value, path, value = winreg.EnumValue(key, i)
                i += 1
                if key_value == name:
                    break
        except:
            key_value = ''
        return key_value


    def getenv(self, name):
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        try:
            value, _ = winreg.QueryValueEx(key, name)
        except:
            value = ''
        return value

        # if is_admin():
        #     key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_READ)
        #     try:
        #         value, _ = winreg.QueryValueEx(key, name)
        #     except:
        #         value = ''
        #     return value
        # else:
        #     if sys.version_info[0] == 3:
        #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



    def setenv(self, name, value):
        # Note: for 'system' scope, you must run this as Administrator
        key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)
        winreg.CloseKey(key)
        # For some strange reason, calling SendMessage from the current process
        # doesn't propagate environment changes at all.
        # TODO: handle CalledProcessError

        # _thread.start_new_thread(changemd())

        # try:
        #     check_call(
        #         '''\"%s" -c "import win32api, win32con;assert win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE,0, 'Environment')"''' % sys.executable)
        # except subprocess.CalledProcessError:
        #         return


        # if is_admin():
        #     key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        #     winreg.SetValueEx(key, name, 0, winreg.REG_EXPAND_SZ, value)
        #     winreg.CloseKey(key)
        #     # For some strange reason, calling SendMessage from the current process
        #     # doesn't propagate environment changes at all.
        #     # TODO: handle CalledProcessError (for assert)
        #     check_call(
        #         '''\"%s" -c "import win32api, win32con;assert win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE,0, 'Environment')"''' % sys.executable)
        # else:
        #     if sys.version_info[0] == 3:
        #         ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

    def get_userenv(self, name):
        # Note: for 'system' scope, you must run this as Administrator
        # key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
        # value, _ = winreg.QueryValueEx(key, name)
        # return value

        if is_admin():
            key = winreg.OpenKey(self.root, self.subkey, 0, winreg.KEY_ALL_ACCESS)
            value, _ = winreg.QueryValueEx(key, name)
            return value
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)



def set_env_path(env_obj, env_name, env_path, refresh):
    need_add = False
    path_values = None
    exist_path = None
    if env_obj.search(env_name):
        exist_path = env_obj.get_userenv(env_name)
    if not exist_path and env_obj.search(env_name.upper()):
        exist_path = env_obj.get_userenv(env_name.upper())

    if refresh:
        exist_path = None

    if exist_path:
        path_values = [i for i in exist_path.split(';')]
        for i in env_path.split(';'):
            if i not in path_values:
                path_values.append(i)
                need_add = True
    if not need_add and path_values:
        return '已添加环境变量{}:{}'.format(env_name, exist_path)

    if path_values:
        env_path = ';'.join(path_values)

    env_obj.setenv(env_name, os.path.expanduser(env_path))
    path_value = env_obj.get_userenv(env_name)
    return '已添加环境变量{}:{}'.format(env_name, path_value)


def envrimentChange(Path_behind):
    env_obj = Win32Environment(scope="SYSTEM")
    Path=os.getenv('Path');
    Path=Path_behind #Path+';'+Path_behind
    # print(Path)
    set_env_path(env_obj, 'Path', Path, refresh=False)
    # print(set_env_path(env_obj, 'Path',Path, refresh=False))
    # print
    # set_env_path(env_obj, 'Path', '%JAVA_HOME%\\bin;%JAVA_HOME%\\jre\\bin')
    # print
    # set_env_path(env_obj, 'CLASSPATH',
    #              '.;%JAVA_HOME%\\lib\\dt.jar;%JAVA_HOME%\\lib\\tools.jar')