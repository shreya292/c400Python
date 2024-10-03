import requests
import csv

url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
output_file = "/root/taxi_zone_output.txt"

response = requests.get(url)
csv_data = response.content.decode('utf-8')

lines = csv_data.splitlines()
reader = csv.DictReader(lines)

records = list(reader)

total_records = len(records)

unique_boroughs = sorted(set(record['Borough'] for record in records))

brooklyn_count = sum(1 for record in records if record['Borough'] == 'Brooklyn')

with open(output_file, 'w') as f:
    f.write(f"Total Number of Records: {total_records}\n")
    f.write(f"Unique Boroughs (Sorted): {', '.join(unique_boroughs)}\n")
    f.write(f"Records for Brooklyn Borough: {brooklyn_count}\n")

print("Facts saved to /root/taxi_zone_output.txt")
