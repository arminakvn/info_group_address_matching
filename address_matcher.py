def info_parcel_address_matcher(muni_id):
    from out_table_writer import write_to_csv
    from Levenshtein import ratio as lratio
    from events import event
    address_match_dict = {}
    all_parcels_street= []
    parcel_street_index = event()
    list_of_streets_already_indexed = []
    incre_id = 0
    from info_points_to_df import info_point_to_df
    muni_sel_df_for_matching = info_point_to_df(muni_id)
    from csv_file_name_maker import csv_file_name_maker

    for item in muni_sel_df_for_matching.transpose():
        e_info = event()
        e_info.info_muni = muni_id
        out_csv_file_name = csv_file_name_maker(muni_id, location="E:\SkyDrive\_code\info_group_address_matching")
        raw_address_s = item[1]
        from find_bad_strings import fix_bad_string_address
        raw_address = fix_bad_string_address(raw_address_s)
        from all_address_parser import pars_street_name, pars_house_number
        e_info.info_street_address = pars_street_name(raw_address)
        e_info.info_house_number = pars_house_number(raw_address)
        e_info.info_id = item[2]
        from parcels_street_finder import parcels_street_finder

        if e_info.info_street_address in list_of_streets_already_indexed:
            temp_lookup_dict = {}
            temp_lookup_dict = getattr(parcel_street_index, 'index_look_up')
            all_parcels_street = temp_lookup_dict[e_info.info_street_address]
            print "using the index for parcel street name of: ", e_info.info_street_address
        else:
            print "no indexed for parcel street name of: ", e_info.info_street_address
            print "appeding to the list..."
            parcel_street_index.make_index_streets(e_info.info_street_address, e_info.info_muni)
            list_of_streets_already_indexed.append(e_info.info_street_address)
            print "list updated: ", list_of_streets_already_indexed
            temp_lookup_dict = {}
            temp_lookup_dict = getattr(parcel_street_index, 'index_look_up')
            #all_parcels_street = parcels_street_finder(e_info.info_street_address, e_info.info_muni)
            all_parcels_street = temp_lookup_dict[e_info.info_street_address] 
        #all_parcels_street= []
            #all_parcels_street = parcels_street_finder(e_info.info_street_address, e_info.info_muni)
        e_matcher = event()
        house_numbers_list = []
        house_mapcid_dict = {}
        for each in all_parcels_street:
            for key, value in each.iteritems():
                house_numbers_list.append(value)
                house_mapcid_dict.update({value: key})
        
        for value in house_numbers_list:
            parcel_house_number = value
            
            u_s_parcel_house_number = unicode(str(parcel_house_number).lower())
            u_s_info_house_number = unicode(str(e_info.info_house_number).lower())
            house_matcher = lratio(u_s_parcel_house_number, u_s_info_house_number)
            if house_matcher > 0.85:
                e_matcher.parcel_mapcid = house_mapcid_dict[parcel_house_number]
                e_matcher.info_id = e_info.info_id
                e_matcher.match_hn_lratio = house_matcher
                incre_id += 1
                address_match_dict.update({incre_id: (e_matcher.info_id, e_matcher.parcel_mapcid, e_matcher.match_hn_lratio)})
                print "match found-Levenshtein method:", "parcel house number: ", u_s_parcel_house_number, " and info gr house number: ", u_s_info_house_number
                print "updating the csv...", "mapc_id=", e_matcher.parcel_mapcid, " match with infogroup_id=",e_matcher.info_id, "with leventhtein ratio of:", e_matcher.match_hn_lratio
                write_to_csv(address_match_dict, out_csv_file_name)
            else:
                print "no matches found for",str(e_info.info_house_number), str(e_info.info_street_address), " parcel house number: ", u_s_parcel_house_number
            #except:
                #if e_info.info_house_number in parcel_house_number:
                #    e_matcher.parcel_mapcid = all_parcels_street[parcel_house_number]
                #    e_matcher.info_id = e_info.info_id
                #    e_matcher.match_hn_lratio = -1
                #    address_match_dict.update({e_matcher.info_id: (e_matcher.parcel_mapcid, e_matcher.match_hn_lratio)})
                #    print "match found based on range of house numbers", "parcel house number: ", u_s_parcel_house_number, " and info gr house number: ", u_s_info_house_number
                #    print "updating the csv..."
                #    write_to_csv(address_match_dict, r'E:\SkyDrive\_code\info_group_address_matching\address_match.csv')
             
for muni_id in munis_no_info_match:
    try:
        info_parcel_address_matcher(muni_id)

    except:
        pass
