import json, re

with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find provinceCityMap start and end
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

js_obj = content[start:end].replace('provinceCityMap:', '').strip().replace("'", '"')
province_city_map = json.loads(js_obj)

# Province-level longitude data (approximate, representing capital or geographic center)
province_longitudes = {
    "北京市": 116.40,
    "天津市": 117.20,
    "河北省": 114.48,
    "山西省": 112.53,
    "内蒙古": 111.65,
    "辽宁省": 123.43,
    "吉林省": 125.35,
    "黑龙江省": 126.63,
    "上海市": 121.47,
    "江苏省": 118.78,
    "浙江省": 120.15,
    "安徽省": 117.27,
    "福建省": 119.30,
    "江西省": 115.85,
    "山东省": 117.00,
    "河南省": 113.65,
    "湖北省": 114.31,
    "湖南省": 112.98,
    "广东省": 113.23,
    "广西": 108.33,
    "海南省": 110.33,
    "重庆市": 106.55,
    "四川省": 104.07,
    "贵州省": 106.71,
    "云南省": 102.83,
    "西藏": 91.17,
    "陕西省": 108.95,
    "甘肃省": 103.83,
    "青海省": 101.78,
    "宁夏": 106.27,
    "新疆": 87.62,
    "台湾省": 121.50,
    "香港": 114.17,
    "澳门": 113.55
}

# For each province, print the solar time offset from Beijing (120°E reference)
print("Province Longitudes & Solar Time Offsets:")
print(f"{'Province':<10} {'Longitude':>8} {'Offset(min)':>12} {'Shift Impact':>20}")
print("-" * 52)

for prov in province_city_map:
    lng = province_longitudes.get(prov, 116)
    offset_min = (lng - 120) * 4  # 4 minutes per degree
    # 时辰 boundary impact
    impact = ""
    if abs(offset_min) > 30:
        impact = "可能跨时辰边界"
    elif abs(offset_min) > 15:
        impact = "时辰边缘微调"
    else:
        impact = "无影响"
    
    print(f"{prov:<10} {lng:>8.2f}° {offset_min:>+8.1f}min {impact:>20}")

print(f"\nTotal provinces with longitude: {len(province_longitudes)}")
print(f"Total provinces in city map: {len(province_city_map)}")