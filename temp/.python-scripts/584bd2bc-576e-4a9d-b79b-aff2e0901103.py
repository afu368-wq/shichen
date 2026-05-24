with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line containing the closing of provinceCityMap
for i, line in enumerate(lines):
    if '氹仔' in line:
        print(f"Line {i}: {repr(line)}")
    if '路氹城' in line:
        print(f"Line {i}: {repr(line)}")
        
# Also check around line numbers
for i, line in enumerate(lines):
    if '澳门' in line and '氹仔' in lines[i+1] if i+1 < len(lines) else False:
        print(f"\nLine {i}: {repr(line)}")
        print(f"Line {i+1}: {repr(line)}")
        if i+2 < len(lines):
            print(f"Line {i+2}: {repr(line)}")
        if i+3 < len(lines):
            print(f"Line {i+3}: {repr(line)}")