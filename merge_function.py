import os
from datetime import datetime
import pandas as pd

def perform_merge(folder_path):
    # 获取 main.py 文件所在的目录作为基准目录
    base_path = os.path.dirname(os.path.abspath(__file__))
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    output_folder = f"{current_time}OutputFolder"
    output_folder_path = os.path.join(base_path, output_folder)
    os.makedirs(output_folder_path, exist_ok=True)

    all_data = []
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_pairs = [files[i:i + 2] for i in range(0, len(files), 2)]
        for pair in file_pairs:
            if len(pair) == 2:
                data_list = []
                for file in pair:
                    if file.endswith('.txt'):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8') as txt_file:
                            lines = txt_file.readlines()
                            found_keyword = False
                            for index, line in enumerate(lines):
                                if line.startswith("mm\tkN\tsec"):
                                    found_keyword = True
                                    continue
                                if found_keyword:
                                    # 分割每行数据，去除第三列后添加到列表
                                    data = line.split('\t')[:2]
                                    if index >= 1 and index % 200 == 0:
                                        data_list.append(['', ''])
                                    data_list.append(data)
                        # 在每个文件读取完后添加一个空行用于分隔
                        data_list.append(['', ''])

                # 将数据列表转换为DataFrame，并添加列名
                df = pd.DataFrame(data_list, columns=[f"Column1_{file_count}", f"Column2_{file_count}"])
                all_data.append(df)
                file_count += 1

    # 合并所有的DataFrame
    combined_df = pd.concat(all_data, axis=1)

    # 保存为Excel文件
    new_file_name = os.path.join(output_folder_path, f"{current_time}_combined.xlsx")
    combined_df.to_excel(new_file_name, index=False)