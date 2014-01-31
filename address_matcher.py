from out_table_writer import write_to_csv
from Levenshtein import ratio as lratio
def info_parcel_address_matcher(muni_id):
    from events import event
    address_match_dict = {}
    from info_points_to_df import info_point_to_df
    muni_sel_df_for_matching = info_point_to_df(muni_id)
    for item in muni_sel_df_for_matching.transpose():
        e_info = event()
        e_info.info_muni = muni_id
        raw_address = item[1]
        from all_address_parser import pars_street_name, pars_house_number
        e_info.info_street_address = pars_street_name(raw_address)
        e_info.info_house_number = pars_house_number(raw_address)
        e_info.info_id = item[2]
        from parcels_street_finder import parcels_street_finder
        all_parcels_street = parcels_street_finder(e_info.info_street_address, e_info.info_muni)
        e_matcher = event()
        house_numbers_list = []
        for key, value in all_parcels_street.iteritems():
            house_numbers_list.append(key)
        try:
            for house in all_parcel_street:
                e_matcher.parcel_mapcid = all_parcels_street[e_info.info_house_number]
                e_matcher.info_id = e_info.info_id
                address_match_dict.update({e_matcher.info_id: e_matcher.parcel_mapcid})
                print "match found based on dictionary lookup method"
                print "updating the csv..."
                write_to_csv(address_match_dict, r'E:\SkyDrive\_code\info_group_address_matching\address_match.csv')
                
        except:
            for value in house_numbers_list:
                parcel_house_number = value
                
                u_s_parcel_house_number = unicode(str(parcel_house_number).lower())
                u_s_info_house_number = unicode(str(e_info.info_house_number).lower())
                house_matcher = lratio(u_s_parcel_house_number, u_s_info_house_number)
                if house_matcher > 0.8:
                    e_matcher.parcel_mapcid = all_parcels_street[parcel_house_number]
                    e_matcher.info_id = e_info.info_id
                    address_match_dict.update({e_matcher.info_id: e_matcher.parcel_mapcid})
                    print "match found based on Levenshtein method"
                    print "updating the csv..."
                    write_to_csv(address_match_dict, r'E:\SkyDrive\_code\info_group_address_matching\address_match.csv')
                else:
                    print "no matches found for",str(e_info.info_house_number), str(e_info.info_street_address), " parcel house number: ", u_s_parcel_house_number
info_parcel_address_matcher()

