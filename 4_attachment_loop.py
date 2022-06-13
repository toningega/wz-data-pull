import pandas as pd
import json
from itertools import combinations, product


gun_data = pd.read_excel('Gun_fct.xlsx')

attachment_dict = {}

gun_unique = gun_data[["gun_name","gun_id"]].drop_duplicates()

for gun,gun_id in zip(gun_unique["gun_name"],gun_unique["gun_id"]):
    attachment_data = gun_data[["attachment_slot","attachment_name","attachment_id"]][(gun_data["gun_name"] == gun) & (gun_data["attachment_slot"] != "optic")]
    # print(attachment_data)
    # attachment_gb = attachment_data.groupby(["attachment_slot"])['attachment_name'].apply(lambda x: list(x)).reset_index()
    attachment_gb = attachment_data.groupby(["attachment_slot"])['attachment_id'].apply(lambda x: list(x)).reset_index()
    attachment_lol = attachment_gb["attachment_id"].to_list()
    # attachment_slot_list = gun_data["attachment_slot"][gun_data["gun_name"] == gun].drop_duplicates().to_list()
    print(gun)


    attachment_dict[gun_id] = {}
    attachment_dict[gun_id]["gun_name"] = gun


    total_comb = []
    for comb_length in range(len(attachment_lol) + 1):
        comb = combinations(attachment_lol, comb_length)
        for c in comb:
            total_comb.append(c)


    gun_att_combinations = []
    for all_comb in total_comb:
        a = [p for p in product(*all_comb)]
        gun_att_combinations.extend(a)

    gun_att_combinations = [att_comb for att_comb in product(*attachment_lol)]

    attachment_dict[gun_id]['attachments_comb'] = gun_att_combinations
    # print(gun_att_combinations)

with open('combo_Gun_fct.json','w') as f:
    json.dump(attachment_dict, f, ensure_ascii=False, indent=4)
