import json
import re

# Read the HTML file
with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find provinceCityMap
start = content.find('provinceCityMap:')
end = start
depth = 0
for i in range(start, len(content)):
    if content[i] == '{':
        depth += 1
    elif content[i] == '}':
        depth -= 1
        if depth == 0:
            end = i + 1
            break

# Extract the JavaScript object
js_obj = content[start:end]
# Convert to Python dict - this is a simple approach
js_obj = js_obj.replace('provinceCityMap:', '').strip()
# Replace single quotes with double quotes for JSON
js_obj = js_obj.replace("'", '"')
# Parse as JSON
try:
    province_city_map = json.loads(js_obj)
    print(f"Successfully parsed {len(province_city_map)} provinces")
    # Show first few
    for i, (province, cities) in enumerate(list(province_city_map.items())[:3]):
        print(f"{province}: {len(cities)} cities, first 3: {cities[:3]}")
except json.JSONDecodeError as e:
    print(f"JSON parse error: {e}")
    print("First 500 chars of js_obj:")
    print(js_obj[:500])