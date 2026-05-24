with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the CSS section
idx = content.find('/* 卡片区域样式 */')
if idx < 0:
    idx = content.find('/* 卡片样式 */')
print(f"CSS start at {idx}")
print(repr(content[idx:idx+500]))