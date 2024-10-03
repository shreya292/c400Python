import requests

url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

response = requests.get(url)

with open('/root/taxi_zone_lookup.csv', 'wb') as f:
    f.write(response.content)

file = open('/root/taxi_zone_lookup.csv', 'r')
lines = file.readlines()
file.close()

lines = lines[1:]
lines.sort()

print(len(lines))

boroughs = set()

for line in lines:
    line = line.split(',')
    boroughs.add(line[1])

print(boroughs)

brooklyn = 0

for line in lines:
    line = line.split(',')
    if line[1] == '"Brooklyn"':
        brooklyn += 1

print(brooklyn)

output = open('/root/taxi_zone_output.txt', 'w') # D:\\mthree\\Tools\\c400Python\\c400Python\\taxi_zone_output.txt

output.write(f'Total number of records: {len(lines)}\n')
output.write(f'Unique boroughs: {boroughs}\n')
output.write(f'Number of records for Brooklyn: {brooklyn}\n')

output.close()
