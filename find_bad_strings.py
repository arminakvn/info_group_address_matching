def fix_bad_string_address(string_object):
    st = string_object
    bad_str_location = st.find("/")
    if bad_str_location == -1:
        st_update = st
        return st_update
    else:
        len_st = len(st)
        #print "lenght", len_st
        st_before = st.find(' ', 0, bad_str_location)
        #print "before /", st_before
        st_after = st.find(' ', bad_str_location, len_st)
        #print "after /", st_after
        st_update = st[:st_before] + st[st_after:]
        return st_update
def fix_range_house_numbers(string_object):
    print "original: ", string_object
    st = string_object
    dash_location = st.find("-")
    if dash_location == -1:
        st_update = st
        return st_update
    else:
        len_st = len(st)
        st_before = st.find(' ', 0, dash_location)
        st_after = st.find(' ', dash_location, len_st)
        hn_left_range = st[st_before+1:dash_location]
        print "not tried left: ", hn_left_range
        hn_right_range = st[dash_location+1:st_after]
        print "not tried right: ", hn_right_range 
        try:
            hn_update = range(int(hn_left_range), int(hn_right_range))
        except:
            for s in hn_left_range:
                if s.isdigit()==False:
                    i=hn_left_range.index(s)
                    hn_left_range = hn_left_range[:i] + hn_left_range[i+1:]
                    print hn_left_range
            for sdo in hn_right_range:
                if sdo.isdigit()==False:
                    ido=hn_right_range.index(sdo)
                    hn_right_range = hn_right_range[:ido] + hn_right_range[ido+1:]
                    print hn_right_range
            hn_update = range(int(hn_left_range), int(hn_right_range))    
        return hn_update
