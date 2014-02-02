def csv_file_name_maker(muni_id, location="E:\SkyDrive\_code\info_group_address_matching"):
    from os import path
    dir_location = location
    muni_str = unicode(str(muni_id))
    csv_file_ext = ".csv"
    csv_file_name = "address_match"
    uniq_csv_file =  csv_file_name  + "_" + muni_str + csv_file_ext
    file_name_update = path.join(dir_location, unicode(uniq_csv_file))
    return file_name_update
