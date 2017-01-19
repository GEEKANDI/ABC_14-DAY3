def find_missing(list_1,list_2):
    if list_1 == list_2 :
        return  0
    # else:
    #     return int([item for item in list_1 if item not in list_2])
    else:
        return list(set(list_2) - set(list_1)) [0]