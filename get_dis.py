import haversine as hs   
from haversine import Unit
 
def compute_distance(la1, la2, lo1, lo2):

    loc1 = (la1, lo1)
    loc2 = (la2, lo2)
 
    distance = round(hs.haversine(loc1, loc2, unit='mi'), 2)

    result = str(distance) + ' miles'

    return result
