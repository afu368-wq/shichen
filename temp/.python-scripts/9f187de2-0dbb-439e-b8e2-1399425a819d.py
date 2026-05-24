import json, re

with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JavaScript functions we added
# Find getSolarTimeOffset
start = content.find('function getSolarTimeOffset(province)')
end = content.find('function getCurrentShichen', start)
print("=== getSolarTimeOffset ===")
print(content[start:end])

# Find getCurrentShichen
start = content.find('function getCurrentShichen(date', end)
end = content.find('function getBirthDayBranch', start)
print("\n=== getCurrentShichen ===")
print(content[start:end])

# Find getBirthDayBranch
start = content.find('function getBirthDayBranch(birthdayData)')
end = content.find('function getTodayGanZhi', start)
print("\n=== getBirthDayBranch ===")
print(content[start:end])