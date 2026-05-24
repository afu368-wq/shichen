with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace old green with new primary color
content = content.replace("color: '#6D8B74', icon: '☯'", "color: '#C48793', icon: '☯'")

# Replace old harsh orange with softer coral
content = content.replace("color: '#FF8A65', text: '今日地支逢冲，注意情", "color: '#D48989', text: '今日地支逢冲，注意情")

with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inline color replacements done!")

# Verify no more old colors remain
import re
old_colors = ['#6D8B74', '#5F7161', '#D0C9C0', '#F5F1E8', '#333333', '#666666', '#999999', '#FF8A65']
for color in old_colors:
    count = content.count(color)
    if count > 0:
        print(f"⚠ {color} still appears {count} times in JS/HTML portion")