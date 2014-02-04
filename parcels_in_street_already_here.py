def get_parcel_in_street_index(muni_id, street_name, parcel_street_index):
    all_parcels_street = parcel_street_index.index_street_values[parcel_street_index.index_street_name == street_name]
    return all_parcels_street    
