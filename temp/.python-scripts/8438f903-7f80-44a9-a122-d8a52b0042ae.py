with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the HTML element with id="ganzhi-info"
idx = content.find('id="ganzhi-info"')
if idx < 0:
    idx = content.find("id='ganzhi-info'")
print(f"Found at index {idx}")
print(repr(content[idx:idx+150]))