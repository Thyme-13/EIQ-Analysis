import os
import sys

import win32api
import win32con
import win32gui
import win32print
import ybc_box


def start():
    if not os.path.exists('cache'):
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache")


def mai(sale_volume, total):
    keys = []
    for i in sale_volume:
        keys.append(i)
    most = sale_volume[keys[0]]
    least = sale_volume[keys[-1]]

    max_v = most * 100 / total
    min_v = least * 100 / total

    del keys
    return max_v, min_v


def abc_input(max_v, min_v, csv_path):
    while True:
        max_min = 'a应大于：' + str('%.4f' % max_v) + '；余下部分应大于：' + str('%.4f' % min_v)
        flag = 0  # 循环标志
        strs = ybc_box.multenterbox('''
            仅填a：A类：前a%；B类：剩余部分
            填a、b：A类：前a%；B类：a%~a%+b%；C类：剩余部分
            均填：A类：前a%；B类：a%~a%+b%；C类：b%~b%+c%；D类：剩余部分
            若不填a，则无效；若填a、b，则忽略c
            ''' + max_min, ['a(必填):', 'b(选填):', 'c(选填):'])

        if strs is not None:
            if strs[0] == '':
                win32api.MessageBox(0, 'Enter the value of a', 'INVALID INPUT', win32con.MB_ICONWARNING)
            else:
                try:
                    a = float(strs[0])
                    b = float(strs[1]) if len(strs) > 1 and strs[1] != '' else None
                    c = float(strs[2]) if len(strs) > 2 and strs[2] != '' else None

                    if a > 100:
                        win32api.MessageBox(0, 'The value of a is greater than 100', 'ENTER THE CORRECT NUMBERS',
                                            win32con.MB_ICONWARNING)
                        continue

                    if b is not None and c is not None:
                        sums = round(a + b + c, 2)
                        if sums != 100:
                            win32api.MessageBox(0, f'Total is {sums}, must be exactly 100!',
                                                'ENTER THE CORRECT NUMBERS',
                                                win32con.MB_ICONWARNING)
                            continue
                        return [a, b, c], 3

                    elif b is not None:
                        sums = round(a + b, 2)
                        if sums > 100:
                            win32api.MessageBox(0, f'Sum ({sums}) > 100', 'ENTER THE CORRECT NUMBERS',
                                                win32con.MB_ICONWARNING)
                            continue
                        return [a, b, 100 - sums], 2

                    else:
                        return [a, 100 - a, 0], 1

                except Exception as e:
                    win32api.MessageBox(0, str(e), 'ENTER THE CORRECT NUMBERS', win32con.MB_ICONWARNING)
                    continue
        else:
            os.remove(csv_path)
            win32api.MessageBox(0, 'You shut down the program', 'PROGRAM QUIT', win32con.MB_ICONWARNING)
            sys.exit(0)

def resolution():
    hDC = win32gui.GetDC(0)
    x = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    y = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    re_on = x * y
    return x, y, re_on


def end(csv_path):
    win32api.MessageBox(0, 'Program has ended.',
                        'END OF RUN!',
                        win32con.MB_ICONINFORMATION)
    os.remove(csv_path)
