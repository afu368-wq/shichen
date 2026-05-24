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
province_city_map = json.loads(js_obj)

# Now we need to get the longitude/latitude for each city
# We'll create a mapping of province+city to approximate coordinates
# This is a simplified approach - in reality you'd need a proper geocoding service

# Create a simple coordinate mapping for major cities
# We'll use approximate coordinates for demonstration
city_coordinates = {
    # Beijing
    "北京市-东城区": {"lng": 116.416, "lat": 39.928},
    "北京市-西城区": {"lng": 116.366, "lat": 39.915},
    "北京市-朝阳区": {"lng": 116.443, "lat": 39.921},
    # Shanghai
    "上海市-黄浦区": {"lng": 121.485, "lat": 31.232},
    "上海市-徐汇区": {"lng": 121.437, "lat": 31.179},
    # Guangzhou
    "广东省-广州市": {"lng": 113.264, "lat": 23.129},
    "广东省-深圳市": {"lng": 114.057, "lat": 22.543},
    # Add more as needed...
}

print(f"Created coordinate mapping for {len(city_coordinates)} cities")
print("Sample coordinates:")
for key, coords in list(city_coordinates.items())[:3]:
    print(f"{key}: {coords}")