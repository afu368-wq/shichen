with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the style block boundaries
start_marker = '/* 莫兰迪色系 */'
end_marker = '@media (max-width: 768px) {'

start = content.find(start_marker)
end = content.find(end_marker, start)

print(f"Style block: {start} to {end}")
print(f"Length: {end - start}")
print()

# Check surrounding context
if start > 0:
    # Show 50 chars before
    ctx_start = max(0, start-50)
    print("Context before:", repr(content[ctx_start:start]))