import pandas
import openpyxl
import matplotlib
import easygui
import ybc_commons
import ybc_exception
import ybc_box

import controller
import draw
import statistician
from Excel2CSV import Excel_CSV
from filter import CSV_filter
from path_input import input_inspect

controller.start()

file_path = input_inspect()
indexes = ybc_box.multenterbox('''
                                请输入商品名及销售量所在列的字母索引
                                ！！！请务必输入大写字母！！！
                                ''',
                               ['商品名索引', '销售量索引']
                               )

names, sale_volumes = indexes[0], indexes[1]
csv_path = Excel_CSV(file_path)
data_list = CSV_filter(csv_path, sale_volumes, output_form=1)
new_list = statistician.data_screening(data_list, names, sale_volumes)[0]
total = statistician.data_screening(data_list, names, sale_volumes)[1]
sale_volume = statistician.sales_volumes(new_list)
max_v, min_v = controller.mai(sale_volume, total)
boundaries = controller.abc_input(max_v, min_v, csv_path)
sorted_list = statistician.proportion_calculation(sale_volume, total, boundaries)[0]
kinds = statistician.proportion_calculation(sale_volume, total, boundaries)[1]
sum_list = draw.l_d2sum(sorted_list, boundaries[1], kinds)
tuple_lists = draw.l_d2list(sorted_list, boundaries[1])

while True:
    draw.all_pie(sum_list, boundaries[1])
    if ybc_box.choicebox('', ['Quit', 'Next']) != 'Next':
        break
    draw.draw_pie(tuple_lists, boundaries[1])
    if ybc_box.choicebox('', ['Quit', 'Last']) != 'Last':
        break

controller.end(csv_path)
