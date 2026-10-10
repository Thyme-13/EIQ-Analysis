import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))

def Excel_CSV(file_path):
    if os.path.exists(file_path) and os.path.isdir(file_path):
        file_list = os.listdir(file_path)
        formats = ['.xlsx', '.xls']
        for i in file_list:
            if os.path.splitext(i)[1] in formats:
                in_path = os.path.join(file_path, i)
                if not os.path.exists(in_path):
                    continue
                mi = pd.read_excel(in_path, dtype=object)
                csv_path = os.path.join(script_dir, 'cache', os.path.splitext(i)[0] + '.csv')
                mi.to_csv(csv_path, index=False, encoding='UTF-8-SIG')
                return csv_path
        return None
    else:
        return None