import json, re

with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the full calculateTodayCard function
card_start = content.find('function calculateTodayCard')
card_end = content.find('function getTodayGanZhi', card_start)
print(content[card_start:card_end])
print("\n" + "="*60 + "\n")

# Find shichenList 
shi_start = content.find('shichenList')
if shi_start > 0:
    shi_end = content.find(']', shi_start) + 1
    print(content[shi_start:shi_end+200])