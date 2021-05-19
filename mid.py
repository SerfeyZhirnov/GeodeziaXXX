import math
def midPoint(lat1,lon1,lat2,lon2):
    dlon= ((lon2-lon1)*math.pi)/180
    
    lat1= (lat1*math.pi)/180
    lon1= (lon1*math.pi)/180
    lat2= (lat2*math.pi)/180
    lon2= (lon2*math.pi)/180

    Bx = math.cos(lat2)*math.cos(dlon)
    By = math.cos(lat2)*math.sin(dlon)
    lat3 = math.atan2(math.sin(lat1)+math.sin(lat2), math.sqrt((math.cos(lat1)+Bx)*(math.cos(lat1)+Bx)) + By*By)
    lon3 = lon1+math.atan2(By, math.cos(lat1) + Bx)

    return (lat3*180/math.pi),(lon3*180/math.pi)

def dist(lat1,lon1,lat2,lon2):
    lat1= (lat1*math.pi)/180
    lon1= (lon1*math.pi)/180
    lat2= (lat2*math.pi)/180
    lon2= (lon2*math.pi)/180

    rad=6372795
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = lon2 - lon1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)
    y = math.sqrt(math.pow(cl2*sdelta,2)+math.pow(cl1*sl2-sl1*cl2*cdelta,2))
    x = sl1*sl2+cl1*cl2*cdelta
    ad = math.atan2(y,x)
    dist = ad*rad

    return dist


    
