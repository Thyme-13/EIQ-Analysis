import os
import pandas as pd


def Excel_CSV(file_path: str) -> str | None:
    """将文件夹中的 Excel 文件转换为 CSV
    :param file_path: Excel 文件所在文件夹路径
    :return: 生成的 CSV 文件路径，未找到 Excel 文件则返回 None
    """
    if os.path.exists(file_path):
        file_list = os.listdir(file_path)
        formats = ['.xlsx', '.xls']
        for i in file_list:
            if os.path.splitext(i)[1] in formats:
                in_path = os.path.join(file_path, i)
                mi = pd.read_excel(in_path, dtype=object)
                script_dir = os.path.dirname(os.path.abspath(__file__))
                csv_path = os.path.join(script_dir, 'cache', os.path.splitext(i)[0] + '.csv')
                mi.to_csv(csv_path, index=False, encoding='UTF-8-SIG')
                del mi
                return csv_path
        return None
    else:
        return None