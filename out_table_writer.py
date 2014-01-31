import csv
def write_to_csv(address_match_dict, csv_file_to_write=r'E:\SkyDrive\_code\info_group_address_matching\address_match.csv'):
    with open(csv_file_to_write,'wb') as f:
        w = csv.writer(f)
        w.writerows(address_match_dict.items())   
