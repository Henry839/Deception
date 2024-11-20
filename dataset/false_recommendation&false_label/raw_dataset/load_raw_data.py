import pandas as pd
import os
import json
dataset_type = './base_orig'
file_path_list = [
    "first_order_false_label_deception.xlsx",
    "second_order_false_label_deception.xlsx",
    "first_order_false_recommendation_deception.xlsx",
    "second_order_false_recommendation_deception.xlsx"
]
dataset = {}
for file_path in file_path_list:
    sub_dataset = pd.read_excel(os.path.join(dataset_type,file_path), usecols=[0], engine='openpyxl').iloc[:, 0].tolist()
    dataset[file_path[:-5]] = sub_dataset

with open(os.path.join('../dataset',dataset_type+'.json'),'w',encoding='utf-8') as f_out:
    json.dump(dataset, f_out, indent=4, ensure_ascii=False)
f_out.close()