with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the provinceCityMap block
start = content.find('provinceCityMap:')
end_block = content.find('};', start) + 2

# Get the full block
full_block = content[start:end_block]
print(full_block[:300])
print("...")
print(full_block[-300:])