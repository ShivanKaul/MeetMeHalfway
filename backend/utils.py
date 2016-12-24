def get_c(a_long, a_lat, b_long, b_lat):
    return ((a_long + b_long) // 2, (a_lat + b_lat) // 2)

# Why does Python not have a flatten method
def flatten(things):
    return [rec for genreRec in things for rec in genreRec]


# Filter out repeated dictionaries
# Citation: http://stackoverflow.com/a/11092590/2989693


def filter_repeated_dicts(things):
    return {v['name']: v for v in things}.values()
