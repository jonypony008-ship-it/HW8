import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    data = f.read()

bin_number = re.search(r'БИН\s+(\d+)', data)
total_sum = re.search(r'ИТОГО:\s+([\d\s,.]+)', data)
date_time = re.search(r'Время:\s+(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})', data)
products = re.findall(r'\d+\.\n(.*?)\n', data)

print("--- PARSED DATA ---")
if bin_number: print(f"BIN: {bin_number.group(1)}")
if date_time: print(f"Date/Time: {date_time.group(1)}")
if total_sum: print(f"Total: {total_sum.group(1).strip()}")

print("\nProducts:")
for p in products:
    print(f"- {p.strip()}")