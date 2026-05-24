with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find ganZhiInfo
for i, line in enumerate(lines):
    if 'ganzhiInfo' in line and 'span' in line.lower():
        print(f"Line {i}: {repr(line)}")
        print(f"Line {i+1}: {repr(lines[i+1])}")