with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Search for where province/city/location is used in JS logic
import re

# Find calculateTodayCard and related functions
cal_start = content.find('function calculateTodayCard')
if cal_start > 0:
    print(content[cal_start:cal_start+2000])