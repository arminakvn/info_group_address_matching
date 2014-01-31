def parcels_in_muni_to_df(muni_id):
    # returns a list of addressess, possibly pairs of mapc_is and street addressess
    muni_id_str = str(int(muni_id))
    where_clause_parcel_df = eval('parcels_muni_id + muni_id', {'parcels_muni_id': "muni_id =", 'muni_id': muni_id_str})
    from arcpy import env, Describe
    from arcpy.da import FeatureClassToNumPyArray
    from env_local_vars_setup import parcels_featureclass, parcels_address_full_field, parcels_address_street_field, parcels_mapc_id_field
    fields_df_parcel_sel = parcels_mapc_id_field + parcels_address_full_field + parcels_address_street_field
    SR_parcels = Describe(parcels_featureclass).spatialReference
    parcel_sel_df_for_matching = FeatureClassToNumPyArray(parcels_featureclass, fields_df_parcel_sel, where_clause_parcel_df, spatial_reference=SR_parcels, skip_nulls=True)
    return parcel_sel_df_for_matching
