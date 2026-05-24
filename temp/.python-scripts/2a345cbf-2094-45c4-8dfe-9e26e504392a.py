import re

with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of provinceCityMap block, after its closing brace + comma
prov_start = content.find('provinceCityMap:')
# Find the closing of the provinceCityMap object
depth = 0
end_prov = prov_start
for i in range(prov_start, len(content)):
    if content[i] == '{':
        depth += 1
    elif content[i] == '}':
        depth -= 1
        if depth == 0:
            end_prov = i
            break

# Show what comes after the provinceCityMap closing brace
print(repr(content[end_prov:end_prov+100]))