import os
import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
import win32api
import win32con
import win32gui
import win32print


def start():
    cache_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache')
    os.makedirs(cache_dir, exist_ok=True)


def mai(sale_volume: dict, total: float) -> tuple:
    keys = []
    for i in sale_volume:
        keys.append(i)
    most = sale_volume[keys[0]]
    least = sale_volume[keys[-1]]

    max_v = most * 100 / total
    min_v = least * 100 / total

    del keys
    return max_v, min_v


def abc_input(max_v: float, min_v: float, csv_path: str) -> tuple:
    root = tk.Tk()
    root.withdraw()

    while True:
        max_min = f'a应大于：{max_v:.4f}；余下部分应大于：{min_v:.4f}'
        flag = 0

        a_val = simpledialog.askstring("Input", f"{max_min}\n\n仅填a：A类：前a%；B类：剩余部分\n填a、b：A类：前a%；B类：a%~a%+b%；C类：剩余部分\n均填：A类：前a%；B类：a%~a%+b%；C类：b%~b%+c%；D类：剩余部分\n若不填a，则无效；若填a、c，则忽略c\n\n请输入a(必填):")

        if a_val is None:
            win32api.MessageBox(0, 'You shut down the program', 'PROGRAM QUIT', win32con.MB_ICONWARNING)
            os.remove(csv_path)
            sys.exit()

        if a_val == '':
            messagebox.showwarning("Invalid Input", "Enter the value of a")
            continue

        try:
            a_float = float(a_val)
        except ValueError as e:
            messagebox.showwarning("ENTER THE CORRECT NUMBERS", str(e))
            continue

        if a_float > 100:
            messagebox.showwarning("ENTER THE CORRECT NUMBERS", "The value of a is greater than 100")
            continue
        elif 100 - a_float < min_v:
            messagebox.showwarning("ONLY ONE CATEGORIES", f"The rest is less than {min_v:.4f}")
            continue

        b_val = simpledialog.askstring("Input", "请输入b(选填，留空则只有A、B两类):")

        if b_val is None or b_val == '':
            return [a_float], 1

        try:
            b_float = float(b_val)
        except ValueError as e:
            messagebox.showwarning("ENTER THE CORRECT NUMBERS", str(e))
            continue

        sum_ab = a_float + b_float
        if sum_ab > 100:
            messagebox.showwarning("ENTER THE CORRECT NUMBERS", "Sum of ab greater than 100")
            continue
        elif 100 - sum_ab < min_v:
            messagebox.showwarning("ONLY TWO CATEGORIES", f"The rest is less than {min_v:.4f}")
            continue

        c_val = simpledialog.askstring("Input", "请输入c(选填，留空则只有A、B、C三类):")

        if c_val is None or c_val == '':
            return [a_float, b_float], 2

        try:
            c_float = float(c_val)
        except ValueError as e:
            messagebox.showwarning("ENTER THE CORRECT NUMBERS", str(e))
            continue

        sum_abc = a_float + b_float + c_float
        if sum_abc > 100:
            messagebox.showwarning("ENTER THE CORRECT NUMBERS", "Sum of abc greater than 100")
            continue
        elif 100 - sum_abc < min_v:
            messagebox.showwarning("ONLY THREE CATEGORIES", f"The rest is less than {min_v:.4f}")
            continue

        return [a_float, b_float, c_float], 3


def resolution():
    hDC = win32gui.GetDC(0)
    x = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    y = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    re_on = x * y
    return x, y, re_on


def end(csv_path: str):
    win32api.MessageBox(0, 'Program has ended.',
                        'END OF RUN!',
                        win32con.MB_ICONINFORMATION)
    os.remove(csv_path)