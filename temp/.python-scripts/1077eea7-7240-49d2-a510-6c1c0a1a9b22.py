with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_start = 197
css_end = 15671

new_css = """        /* 温暖女性化色系 */
        :root {
            --primary: #C48793;
            --primary-light: #D9A7B0;
            --primary-dark: #A06B7A;
            --accent: #E8D0D5;
            --accent-light: #F5E8EB;
            --background: #FFF5F3;
            --card: #FFFFFF;
            --text-primary: #4A3535;
            --text-secondary: #8B6F6F;
            --text-light: #B8A0A0;
            --shadow: 0 4px 24px rgba(180, 140, 150, 0.10);
            --shadow-lg: 0 8px 40px rgba(180, 140, 150, 0.15);
            --radius: 20px;
            --radius-sm: 12px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif;
            background: linear-gradient(180deg, var(--background) 0%, #FFF0EE 100%);
            color: var(--text-primary);
            line-height: 1.6;
            padding: 24px;
            min-height: 100vh;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        /* 头部 */
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding: 30px 0 20px;
            border-bottom: 2px solid var(--accent);
            position: relative;
        }

        .header::after {
            content: '';
            position: absolute;
            bottom: -6px;
            left: 50%;
            transform: translateX(-50%);
            width: 48px;
            height: 4px;
            background: var(--primary-light);
            border-radius: 2px;
        }

        .title {
            font-size: 2.2rem;
            font-weight: 700;
            color: var(--primary-dark);
            margin-bottom: 8px;
            letter-spacing: 1px;
        }

        .subtitle {
            font-size: 1rem;
            color: var(--text-secondary);
            font-weight: 400;
        }

        /* 卡片 */
        .card {
            background: var(--card);
            border-radius: var(--radius);
            padding: 32px;
            margin-bottom: 24px;
            box-shadow: var(--shadow);
            border: 1px solid var(--accent-light);
            transition: box-shadow 0.3s ease;
        }

        .card:hover {
            box-shadow: var(--shadow-lg);
        }

        .card-title {
            font-size: 1.3rem;
            font-weight: 600;
            color: var(--primary-dark);
            margin-bottom: 18px;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        /* 表单 */
        .form-group {
            margin-bottom: 22px;
        }

        .form-label {
            display: block;
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--text-primary);
            margin-bottom: 8px;
            letter-spacing: 0.3px;
        }

        .form-input {
            width: 100%;
            padding: 13px 18px;
            border: 2px solid var(--accent);
            border-radius: var(--radius-sm);
            font-size: 1rem;
            color: var(--text-primary);
            background: var(--background);
            transition: all 0.25s ease;
            font-family: inherit;
        }

        .form-input:focus {
            outline: none;
            border-color: var(--primary);
            background: #fff;
            box-shadow: 0 0 0 3px rgba(196, 135, 147, 0.12);
        }

        .form-input::placeholder {
            color: var(--text-light);
        }

        /* 按钮 */
        .btn {
            display: inline-block;
            padding: 14px 36px;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 28px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.25s ease;
            text-align: center;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 16px rgba(196, 135, 147, 0.25);
        }

        .btn:hover {
            background: var(--primary-dark);
            box-shadow: 0 6px 20px rgba(196, 135, 147, 0.35);
            transform: translateY(-1px);
        }

        .btn:active {
            transform: translateY(0);
        }

        .btn:disabled {
            background: var(--accent);
            box-shadow: none;
            cursor: not-allowed;
            transform: none;
        }

        .btn-full {
            width: 100%;
        }

        /* 能量卡片 */
        .energy-card {
            background: linear-gradient(135deg, #C48793 0%, #D9A7B0 40%, #E2B8C0 100%);
            color: white;
            border-radius: var(--radius);
            padding: 44px 40px;
            margin-bottom: 24px;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 40px rgba(196, 135, 147, 0.30);
        }

        .energy-card::before {
            content: '';
            position: absolute;
            top: -40px;
            right: -40px;
            width: 160px;
            height: 160px;
            background: rgba(255,255,255,0.06);
            border-radius: 50%;
            pointer-events: none;
        }

        .energy-card::after {
            content: '';
            position: absolute;
            bottom: -20px;
            left: 20px;
            width: 80px;
            height: 80px;
            background: rgba(255,255,255,0.04);
            border-radius: 50%;
            pointer-events: none;
        }

        .energy-tag {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 18px;
            position: relative;
            z-index: 1;
        }

        .energy-icon {
            font-size: 2.8rem;
            filter: drop-shadow(0 2px 8px rgba(0,0,0,0.15));
        }

        .energy-name {
            font-size: 2.4rem;
            font-weight: 700;
            letter-spacing: 3px;
        }

        .energy-desc {
            font-size: 1.15rem;
            opacity: 0.85;
            margin: 12px 0;
            font-style: italic;
            position: relative;
            z-index: 1;
        }

        .relation-tag {
            display: inline-block;
            background: rgba(255, 255, 255, 0.22);
            border-radius: 24px;
            padding: 8px 22px;
            font-size: 0.95rem;
            margin-bottom: 16px;
            backdrop-filter: blur(10px);
            position: relative;
            z-index: 1;
            letter-spacing: 0.5px;
        }

        .ganzhi-info {
            font-size: 1.05rem;
            opacity: 0.9;
            letter-spacing: 1px;
            position: relative;
            z-index: 1;
        }

        /* 今日底色 */
        .atmosphere-text {
            font-size: 1.2rem;
            line-height: 1.9;
            color: var(--text-primary);
            padding: 0;
            margin: 0;
            font-weight: 500;
        }

        /* 避坑指南列表 */
        .pitfall-list {
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .pitfall-item {
            background: var(--card);
            border-radius: var(--radius-sm);
            padding: 20px 24px;
            display: flex;
            gap: 16px;
            box-shadow: var(--shadow);
            border-left: 4px solid #E8A0A0;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .pitfall-item:hover {
            transform: translateX(3px);
            box-shadow: var(--shadow-lg);
        }

        .pitfall-num {
            font-size: 1.3rem;
            font-weight: 700;
            color: #D48989;
            min-width: 30px;
            line-height: 1.6;
        }

        .pitfall-text {
            font-size: 1.05rem;
            line-height: 1.7;
            color: var(--text-primary);
        }

        /* 好运颜色 & 出行方向 */
        .lucky-section {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
            margin-bottom: 24px;
        }

        .lucky-card {
            background: #fff;
            border-radius: var(--radius);
            padding: 24px 20px;
            box-shadow: var(--shadow);
            text-align: center;
            border: 1px solid var(--accent-light);
            transition: box-shadow 0.3s;
        }

        .lucky-card:hover {
            box-shadow: var(--shadow-lg);
        }

        .lucky-card .lucky-label {
            font-size: 0.9rem;
            color: var(--text-secondary);
            margin-bottom: 16px;
            letter-spacing: 0.5px;
            font-weight: 500;
        }

        .color-swatches {
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        .color-swatch {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 8px;
            cursor: default;
        }

        .color-circle {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            border: 3px solid rgba(0,0,0,0.06);
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            transition: transform 0.25s ease;
        }

        .color-swatch:hover .color-circle {
            transform: scale(1.2);
        }

        .color-label {
            font-size: 0.75rem;
            color: var(--text-secondary);
            white-space: nowrap;
            font-weight: 500;
        }

        .direction-display {
            display: flex;
            justify-content: center;
            gap: 18px;
            flex-wrap: wrap;
        }

        .direction-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 4px;
        }

        .direction-arrow {
            font-size: 1.8rem;
            line-height: 1;
        }

        .direction-text {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-primary);
        }

        /* 日期选择器 */
        .date-picker {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding: 8px 0;
            margin-bottom: 24px;
            -webkit-overflow-scrolling: touch;
            scroll-snap-type: x mandatory;
        }

        .date-picker::-webkit-scrollbar {
            display: none;
        }

        .date-item {
            flex: 0 0 auto;
            min-width: 66px;
            padding: 10px 10px;
            border-radius: var(--radius-sm);
            background: var(--background);
            border: 2px solid transparent;
            text-align: center;
            cursor: pointer;
            transition: all 0.25s ease;
            scroll-snap-align: start;
            user-select: none;
        }

        .date-item:hover {
            border-color: var(--accent);
            background: #fff;
        }

        .date-item.active {
            background: var(--primary);
            border-color: var(--primary);
            color: #fff;
            box-shadow: 0 4px 14px rgba(196, 135, 147, 0.30);
        }

        .date-item.active .date-label {
            color: rgba(255,255,255,0.75);
        }

        .date-item .date-label {
            font-size: 0.7rem;
            color: var(--text-secondary);
            margin-bottom: 3px;
        }

        .date-item .date-day {
            font-size: 1.05rem;
            font-weight: 600;
        }

        .date-item .date-weekday {
            font-size: 0.65rem;
            color: var(--text-secondary);
            margin-top: 3px;
        }

        .date-item.active .date-weekday {
            color: rgba(255,255,255,0.75);
        }

        .date-item.today {
            border-color: var(--accent);
            background: #fff;
        }

        /* 付费弹窗 */
        .payment-modal {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(60, 40, 40, 0.45);
            backdrop-filter: blur(6px);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s, visibility 0.3s;
        }

        .payment-modal.show {
            opacity: 1;
            visibility: visible;
        }

        .payment-content {
            background: #fff;
            border-radius: 24px;
            width: 90%;
            max-width: 400px;
            padding: 32px;
            box-shadow: 0 20px 60px rgba(160, 100, 110, 0.25);
            transform: translateY(20px);
            transition: transform 0.3s ease;
            position: relative;
        }

        .payment-modal.show .payment-content {
            transform: translateY(0);
        }

        .payment-header {
            text-align: center;
            margin-bottom: 25px;
        }

        .payment-header h2 {
            font-size: 1.4rem;
            color: var(--primary-dark);
            margin-bottom: 8px;
        }

        .payment-header p {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .payment-options {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 25px;
        }

        .payment-option {
            border: 2px solid var(--accent);
            border-radius: 14px;
            padding: 18px;
            cursor: pointer;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 14px;
        }

        .payment-option:hover {
            border-color: var(--primary-light);
            background: var(--accent-light);
        }

        .payment-option.selected {
            border-color: var(--primary);
            background: var(--accent-light);
            box-shadow: 0 4px 14px rgba(196, 135, 147, 0.15);
        }

        .payment-option .option-icon {
            font-size: 1.8rem;
            flex-shrink: 0;
        }

        .payment-option .option-text {
            flex: 1;
        }

        .payment-option .option-title {
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 4px;
        }

        .payment-option .option-desc {
            font-size: 0.85rem;
            color: var(--text-secondary);
            line-height: 1.4;
        }

        .payment-option .option-price {
            font-weight: 700;
            color: var(--primary);
            font-size: 1.1rem;
        }

        .payment-footer {
            text-align: center;
        }

        .payment-footer p {
            color: var(--text-light);
            font-size: 0.8rem;
            margin-bottom: 15px;
        }

        .payment-btn {
            background: var(--primary);
            color: #fff;
            border: none;
            border-radius: 14px;
            padding: 14px;
            font-size: 1rem;
            font-weight: 600;
            width: 100%;
            cursor: pointer;
            transition: all 0.25s ease;
            letter-spacing: 0.5px;
        }

        .payment-btn:hover {
            background: var(--primary-dark);
        }

        .payment-btn:disabled {
            background: var(--accent);
            cursor: not-allowed;
        }

        .close-modal {
            position: absolute;
            top: 15px;
            right: 18px;
            background: none;
            border: none;
            font-size: 1.5rem;
            color: var(--text-light);
            cursor: pointer;
            padding: 5px;
            line-height: 1;
            transition: color 0.2s;
        }

        .close-modal:hover {
            color: var(--primary-dark);
        }

        /* 彩票建议 */
        .lottery-banner {
            background: linear-gradient(135deg, #F8A4A4 0%, #FCD5B0 100%);
            border-radius: var(--radius-sm);
            padding: 18px 22px;
            margin-bottom: 20px;
            color: #fff;
            display: flex;
            align-items: center;
            gap: 14px;
            box-shadow: 0 4px 20px rgba(248, 164, 164, 0.30);
            animation: pulse-lottery 2s infinite;
        }

        @keyframes pulse-lottery {
            0%, 100% { box-shadow: 0 0 0 0 rgba(248, 164, 164, 0.4); }
            50% { box-shadow: 0 0 0 10px rgba(248, 164, 164, 0); }
        }

        .lottery-banner .lottery-icon {
            font-size: 2rem;
            flex-shrink: 0;
        }

        .lottery-banner .lottery-text {
            font-size: 0.9rem;
            line-height: 1.6;
        }

        .lottery-banner .lottery-text strong {
            font-size: 1rem;
        }

        /* 状态 */
        .loading {
            text-align: center;
            padding: 40px;
            color: var(--text-secondary);
        }

        .hidden {
            display: none !important;
        }

        /* 页脚 */
        .footer {
            text-align: center;
            padding: 24px 0;
            color: var(--text-light);
            font-size: 0.85rem;
            line-height: 1.6;
            border-top: 2px solid var(--accent);
            margin-top: 40px;
        }

        /* 阴历/阳历切换 */
        .calendar-toggle {
            display: flex;
            gap: 0;
            margin-bottom: 12px;
            border: 2px solid var(--accent);
            border-radius: var(--radius-sm);
            overflow: hidden;
            width: fit-content;
        }

        .toggle-btn {
            padding: 10px 28px;
            border: none;
            background: var(--background);
            color: var(--text-secondary);
            font-size: 0.95rem;
            cursor: pointer;
            transition: all 0.25s ease;
            font-weight: 500;
        }

        .toggle-btn.active {
            background: var(--primary);
            color: white;
        }

        /* 性别切换 */
        .gender-toggle {
            display: flex;
            gap: 0;
            border: 2px solid var(--accent);
            border-radius: var(--radius-sm);
            overflow: hidden;
            width: fit-content;
        }

        /* 所在城市二级选择器 */
        .current-city-selects {
            display: flex;
            gap: 12px;
        }

        .current-city-select {
            flex: 1;
        }

        select.form-input {
            appearance: none;
            background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath fill='%238B6F6F' d='M1.41 0L6 4.58 10.59 0 12 1.41l-6 6-6-6z'/%3E%3C/svg%3E");
            background-repeat: no-repeat;
            background-position: right 14px center;
            padding-right: 36px;
        }

        /* 响应式 */
        @media (max-width: 768px) {
            .title {
                font-size: 1.8rem;
            }

            .energy-card {
                padding: 32px 24px;
            }

            .energy-name {
                font-size: 1.8rem;
            }
            
            .energy-desc {
                font-size: 1rem;
            }

            .card {
                padding: 24px 20px;
            }

            .lucky-section {
                grid-template-columns: 1fr;
            }

            .pitfall-item {
                padding: 16px 18px;
            }
        }"""

new_content = content[:css_start] + new_css + content[css_end:]

with open(r'C:\Users\shi\AppData\Roaming\Tencent\Marvis\User\oAN1i2SO4MEsdcQMvXnYqgVAWeKg\workspace\conv_19e53af327c_14641a7a3bba\output\index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("CSS replacement done successfully!")
print(f"New CSS length: {len(new_css)} chars")
print(f"New file total length: {len(new_content)} chars")