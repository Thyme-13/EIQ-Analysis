import csv


def CSV_filter(csv_path: str, sale_volumes: str, output_form: int = 0):
    """CSV 数据清洗：去除销售量列中的非数值字符
    :param csv_path: CSV 文件路径
    :param sale_volumes: 商品销售量所在列的索引（大写字母）
    :param output_form: 输出形式 0：无输出，1：输出二维列表，2：输出路径
    """
    csv_list = []
    _sale_volumes = ord(sale_volumes) - 65
    with open(csv_path, encoding='UTF-8-SIG') as file:
        file_csv = csv.reader(file)
        for row in file_csv:
            csv_list.append(row)

    for i in csv_list[1:]:
        for j in i[_sale_volumes]:
            if j not in '0123456789.-':
                i[_sale_volumes] = i[_sale_volumes].replace(j, '')

    clean_file = open(csv_path, 'w', encoding='UTF-8-SIG', newline='')
    file_writer = csv.writer(clean_file)
    file_writer.writerows(csv_list)
    clean_file.close()

    if output_form == 1:
        return csv_list
    elif output_form == 2:
        return csv_path
    return None