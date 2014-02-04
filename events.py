class event:
    #class defining an address matching instance/event
    info_muni             = [] # town in which the matching is taking place
    info_street_address   = [] # info group street address string
    info_house_number     = [] # info group house number
    info_zip              = [] # info group info group zip code
    info_id               = [] # info group id
    parcel_muni           = [] # town in which the matching is taking place
    parcel_street_address = [] # parcel street address string
    parcel_house_number   = [] # parcel house number
    parcel_zip            = [] # parcel info group zip code
    parcel_mapcid         = [] # parcel's mapc_id
    match_hn_lratio       = [] # levenshtein ration between the house numbers that mathched
    match_sn_lratio       = [] # levenshtein ration between the street names that matched
    index_street_name     = [] # name of the street for which the index has made from the parcels
    index_street_values   = [] # indexed values of the street which contains the address list created by the all_street_finder
    index_look_up         = {} 
    
    def make_index_streets(self, street_name, muni_id):
        from parcels_street_finder import parcels_street_finder
        self.index_street_name = street_name
        self.info_muni = muni_id
        self.index_street_values = []
        self.index_street_values.append(parcels_street_finder(self.index_street_name, self.info_muni))
        self.index_look_up.update({self.index_street_name: self.index_street_values})

        


