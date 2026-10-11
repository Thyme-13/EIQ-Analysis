import os
import sys
import win32api
import win32con
import tkinter as tk
from tkinter import simpledialog, messagebox


def input_inspect():
    """
    弹出输入弹窗并对输入的文件路径进行检查
    :return: 若关闭弹窗，则返回None；若路径正确，则返回路径
    """
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    while True:
        file_path = simpledialog.askstring("Input", "Please enter the folder path")
        if file_path is None:
            win32api.MessageBox(0, 'You shut down the program.',
                                'PROGRAM QUIT!',
                                win32con.MB_ICONINFORMATION)
            sys.exit()
        elif file_path == '':
            win32api.MessageBox(0, 'You DID NOT enter a path.',
                                'PLEASE ENTER PATH!',
                                win32con.MB_ICONERROR)
            continue
        elif not os.path.exists(file_path):
            win32api.MessageBox(0, 'You did not enter a CORRECT path.',
                                'PLEASE ENTER THE CORRECT PATH!',
                                win32con.MB_ICONWARNING)
            continue
        elif not Excel_inspect(file_path):
            continue
        else:
            root.destroy()
            return file_path


def Excel_inspect(file_path: str) -> bool:
    """
    输入文件路径并进行检查
    :param file_path: 需要检查的文件路径
    :return: 若路径错误，则返回False；若路径正确，则返回True
    """
    file_list = os.listdir(file_path)
    formats = ['.xlsx', '.xls']
    flag = 0
    con = 0
    for i in file_list:
        if os.path.splitext(i)[1] in formats:
            flag = 1
            con += 1
    if con > 1:
        messagebox.showwarning("Warning", "Multiple Excel files found. Please ensure only one Excel file exists in the folder.")
        return False
    elif flag == 0:
        win32api.MessageBox(0, 'Ensure there is a Excel files in this path.',
                            'NO EXCEL FILE FOUND!',
                            win32con.MB_ICONWARNING)
        return False
    else:
        return True