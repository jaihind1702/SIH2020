import requests
import json
from math import radians, sin, cos, acos

di = {
    "password": "letitbeanything"
}
x = requests.post("http://127.0.0.1:8000/api/admin/getActiveImagesData", data=di)
data = x.json()
print(data)
print(data[0])
latitude = []
longitude = []
animals = []

for element in data:
    latitude.append(element['latitude'])
    longitude.append(element['longitude'])
    animals.append(element['animals'])

print(latitude, longitude, animals)



def compute_distance(x, y, u, v):

    slat = radians(float(x))
    slon = radians(float(y))
    elat = radians(float(u))
    elon = radians(float(v))

    dist = 1000 * 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    return dist

final_latitude = []
final_longitude = []
final_animals = []
locations = []
water_body = []

while len(latitude) != 0:

    p = latitude[0]
    q = longitude[0]
    a = animals[0]
    loc = 1

    latitude.remove(latitude[0])
    longitude.remove(longitude[0])
    animals.remove(animals[0])

    cnt = len(latitude)
    j = 0

    while cnt != 0:

        u = latitude[j]
        v = longitude[j]
        dist = compute_distance(p, q, u, v)
        if dist <= float(100):

            a += animals[j]
            loc += 1
            latitude.remove(latitude[j])
            longitude.remove(longitude[j])
            animals.remove(animals[j])
        else:
            j += 1
        cnt -= 1


    final_latitude.append(p)
    final_longitude.append(q)
    final_animals.append(a)
    locations.append(loc)


for i in range(0, len(final_latitude)):

    water_cnt = 0

    x = final_latitude[i]
    y = final_longitude[i]
    loc = str(x)+','+str(y)
    river = requests.post('https://maps.googleapis.com/maps/api/place/textsearch/json?query=river&key=AIzaSyDAaGzlR9XHDGvdBHn2ZpHl7RU_tWMgil0&radius=100&sensor=false&location='+loc)#&rankby=distance')
    lake = requests.post('https://maps.googleapis.com/maps/api/place/textsearch/json?query=lake&key=AIzaSyDAaGzlR9XHDGvdBHn2ZpHl7RU_tWMgil0&radius=100&sensor=false&location='+loc)#&rankby=distance')
    river = river.json()
    lake = lake.json()

    for element in river['results']:
        
        geo = element['geometry']
        a = geo['location']['lat']
        b = geo['location']['lng']
        d = compute_distance(x, y, a, b)
        if d <= float(1000):
            water_cnt += 1

    for element in lake['results']:
        
        geo = element['geometry']
        a = geo['location']['lat']
        b = geo['location']['lng']
        d = compute_distance(x, y, a, b)
        if d <= float(1000):
            water_cnt += 1
        
    water_body.append(water_cnt)

print(final_latitude)
print(final_longitude)
print(final_animals)
print(locations)
print(water_body)



