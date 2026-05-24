with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the end of provinceCityMap
prov_start = content.find('provinceCityMap:')
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

# Get context around the end
ctx = content[end_prov-30:end_prov+100]
print(repr(ctx))