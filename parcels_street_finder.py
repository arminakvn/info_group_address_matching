def parcels_street_finder(info_street_address, muni_id):
    from events import event
    from Levenshtein import ratio as lratio
    from parcels_in_muni_to_df import parcels_in_muni_to_df
    parcel_sel_df_for_matching = parcels_in_muni_to_df(muni_id)
    all_parcels_street = {}
    for item in parcel_sel_df_for_matching.transpose():
        e_parcel = event()
        raw_address = item[1]
        from all_address_parser import pars_street_name
        e_parcel.parcel_street_address = pars_street_name(raw_address)
        from all_address_parser import pars_house_number
        parcel_house_number = pars_house_number(raw_address)
        #from find_bad_strings import fix_range_house_numbers
        #house_number_range = fix_range_house_numbers(raw_address)
        #if house_number_range == parcel_house_number:
        #    e_parcel.parcel_house_number = parcel_house_number
        #else:
        #    e_parcel.parcel_house_number = house_number_range
        e_parcel.parcel_house_number = parcel_house_number
        e_parcel.parcel_mapcid = item[0]
        u_parcel_address = unicode(str(e_parcel.parcel_street_address).lower())
        u_info_street_address = unicode(str(info_street_address).lower())
        
        matcher = lratio(u_parcel_address, u_info_street_address)
         
        if matcher > 0.95:
            e_parcel.match_sn_lratio = matcher
            all_parcels_street.update({e_parcel.parcel_mapcid: e_parcel.parcel_house_number})
            print "levenstein ratio in making parcel street for ", u_info_street_address, " and ", u_parcel_address, ": ", matcher
        
    return all_parcels_street        
    
