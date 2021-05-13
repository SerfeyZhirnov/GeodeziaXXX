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
    
