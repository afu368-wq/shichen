with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the style block end (closing </style> tag after the media query)
style_close = content.find('</style>')
print(f"</style> at: {style_close}")

# Find the media query block
media_start = content.rfind('@media (max-width: 768px)', 0, style_close)
print(f"@media starts at: {media_start}")

# Get the content from media start to </style>
if media_start > 0:
    seg = content[media_start:style_close]
    # Find where it actually ends (closing brace of media query)
    brace_count = 0
    end_idx = 0
    for i, ch in enumerate(seg):
        if ch == '{':
            brace_count += 1
        elif ch == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = i + 1
                break
    
    print(f"Media query block ends at offset: {end_idx}")
    print("Last 200 chars of media block:")
    print(repr(seg[end_idx-200:end_idx]))
    
    # Show what comes right after }
    after_media = content[media_start+end_idx:style_close]
    print("\nBetween media query end and </style>:")
    print(repr(after_media[:200]))
    
    # The CSS we need to replace starts at the style block beginning (197) and ends at the last } before </style>
    css_start = 197
    css_end = media_start + end_idx  # end of media query's closing brace
    
    print(f"\nCSS block to replace: {css_start} to {css_end}")
    print(f"Length: {css_end - css_start}")

    # Find the actual end - include all whitespace and closing } before </style>
    # after_media might contain whitespace/newline and then </style>
    # The CSS actually ends at style_close (right before </style>)
    # But we want to replace only the CSS content, keeping </style> tag
    
    # Let's find the last non-whitespace before </style>
    tmp = content[:style_close].rstrip()
    actual_css_end = len(tmp)
    
    print(f"\nActual CSS end (before whitespace): {actual_css_end}")
    print(f"CSS content length: {actual_css_end - css_start}")
    
    # The CSS we want to replace: from css_start to actual_css_end
    # Let's see what's right around actual_css_end
    print(f"\nChars around CSS end:")
    print(repr(content[actual_css_end-30:actual_css_end+30]))