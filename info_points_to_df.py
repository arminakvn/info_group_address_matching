def info_point_to_df(muni_id):
    from arcpy import env
    from env_local_vars_setup import myWorkdirectory
    env.workspace = myWorkdirectory
    from env_local_vars_setup import info_group_featureclass, info_muni_id_field, info_address_field, info_id_field, info_zip_field
    fields_df_muni_sel = info_muni_id_field + info_address_field + info_id_field + info_zip_field
    from arcpy import Describe
    SR_info_group = Describe(info_group_featureclass).spatialReference
    muni_id_str = str(int(muni_id))
    where_clause_info_df = eval('muni_field + muni_id', {'muni_field': "Muni_ID =", 'muni_id': muni_id_str})
    from arcpy.da import FeatureClassToNumPyArray
    muni_sel_df_for_matching = FeatureClassToNumPyArray(info_group_featureclass, fields_df_muni_sel, where_clause_info_df, spatial_reference=SR_info_group, skip_nulls=True)
    return muni_sel_df_for_matching
