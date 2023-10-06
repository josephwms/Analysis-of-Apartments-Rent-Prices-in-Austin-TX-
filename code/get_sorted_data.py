def sort_data(data):

    lst_sort = sorted(data, key=lambda x: (x['Price'], x['LivingArea'], x['Distance to the university']))

    return lst_sort
