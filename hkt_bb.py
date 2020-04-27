import urllib.request, json


lat_south = 22.26
lat_north = 22.28

long_west = 114.17
long_east = 114.18

zoomlevel = 20

results = []


pccw_url = f'https://shop.hkt.com/broadband/marker.html?zoomlevel={zoomlevel}&latLower={lat_south}&latUpper={lat_north}&lngLower={long_west}&lngUpper={long_east}'
print(pccw_url)

with urllib.request.urlopen(
        pccw_url) as url:
    data = json.loads(url.read().decode())
    print(data)
    results += data

with open('hkt_data.txt', 'w') as outfile:
    json.dump(data, outfile,
              sort_keys=True,
              indent=4,
              separators=(',', ': '),
              ensure_ascii=False
              )