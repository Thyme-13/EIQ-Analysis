import tkinter as tk
from tkinter import simpledialog, messagebox

import controller
import draw
import statistician
from Excel2CSV import Excel_CSV
from filter import CSV_filter
from path_input import input_inspect

controller.start()

file_path = input_inspect()

root = tk.Tk()
root.withdraw()
names = simpledialog.askstring("Input", "请输入商品名所在列的字母索引（大写字母）")
sale_volumes = simpledialog.askstring("Input", "请输入销售量所在列的字母索引（大写字母）")
root.destroy()

if names is None or sale_volumes is None:
    import sys
    sys.exit()

csv_path = Excel_CSV(file_path)
data_list = CSV_filter(csv_path, sale_volumes, output_form=1)
new_list, total = statistician.data_screening(data_list, names, sale_volumes)
sale_volume = statistician.sales_volumes(new_list)
max_v, min_v = controller.mai(sale_volume, total)
boundaries = controller.abc_input(max_v, min_v, csv_path)

if boundaries is None or boundaries[0] is None:
    import sys
    sys.exit()

sorted_list = statistician.proportion_calculation(sale_volume, total, boundaries)[0]
kinds = statistician.proportion_calculation(sale_volume, total, boundaries)[1]
sum_list = draw.l_d2sum(sorted_list, boundaries[1], kinds)
tuple_lists = draw.l_d2list(sorted_list, boundaries[1])

draw.all_pie(sum_list, boundaries[1])

root = tk.Tk()
root.withdraw()
show_detail = messagebox.askyesno("Continue", "是否显示详细分类图表？")
root.destroy()

if show_detail:
    draw.draw_pie(tuple_lists, boundaries[1])

controller.end(csv_path)