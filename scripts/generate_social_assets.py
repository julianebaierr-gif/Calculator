import os
from PIL import Image, ImageDraw, ImageFont

os.makedirs('assets', exist_ok=True)

def generate_logo():
    # 512x512 logo
    size = 512
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Rounded badge
    radius = 110
    draw.rounded_rectangle([10, 10, size - 10, size - 10], radius=radius, fill=(37, 99, 235, 255))
    
    try:
        font = ImageFont.truetype("arial.ttf", 320)
        bbox = draw.textbbox((0, 0), "∑", font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (size - w) / 2 - bbox[0]
        y = (size - h) / 2 - bbox[1] - 15
        draw.text((x, y), "∑", fill=(255, 255, 255, 255), font=font)
    except Exception as e:
        print(f"Font fallback for logo: {e}")
        sigma_pts = [
            (120, 100), (392, 100), (392, 160), (240, 160),
            (300, 256), (240, 352), (392, 352), (392, 412),
            (120, 412), (120, 372), (220, 256), (120, 140)
        ]
        draw.polygon(sigma_pts, fill=(255, 255, 255, 255))
        
    img.save('logo.png', format='PNG')
    img.save('assets/logo.png', format='PNG')
    print("Created logo.png and assets/logo.png (512x512)")

def generate_og_image():
    # 1200x630 OpenGraph Banner
    w, h = 1200, 630
    img = Image.new('RGBA', (w, h), (15, 23, 42, 255)) # Dark slate (#0F172A)
    draw = ImageDraw.Draw(img)
    
    # Draw soft subtle gradient / glow
    for i in range(150):
        alpha = int(25 * (1 - i / 150))
        draw.ellipse([w//2 - 400 - i, h//2 - 250 - i, w//2 + 400 + i, h//2 + 250 + i], fill=(37, 99, 235, alpha))
        
    # Draw Logo badge (140x140)
    badge_size = 140
    bx, by = (w - badge_size) // 2, 85
    draw.rounded_rectangle([bx, by, bx + badge_size, by + badge_size], radius=32, fill=(37, 99, 235, 255))
    
    try:
        font_sigma = ImageFont.truetype("arial.ttf", 95)
        bbox = draw.textbbox((0, 0), "∑", font=font_sigma)
        sw = bbox[2] - bbox[0]
        sh = bbox[3] - bbox[1]
        draw.text((bx + (badge_size - sw)//2 - bbox[0], by + (badge_size - sh)//2 - bbox[1] - 5), "∑", fill=(255, 255, 255, 255), font=font_sigma)
    except:
        pass
        
    try:
        font_title = ImageFont.truetype("arial.ttf", 64)
        font_sub = ImageFont.truetype("arial.ttf", 28)
        font_pill = ImageFont.truetype("arial.ttf", 22)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_pill = ImageFont.load_default()
        
    # Title: CalcHub
    title_text = "CalcHub"
    bbox_t = draw.textbbox((0, 0), title_text, font=font_title)
    tw = bbox_t[2] - bbox_t[0]
    draw.text(((w - tw)//2, 250), title_text, fill=(255, 255, 255, 255), font=font_title)
    
    # Subtitle: Precision Engineering, Clinical & Financial Calculators
    sub_text = "Precision Standards-Compliant Scientific Calculators"
    bbox_s = draw.textbbox((0, 0), sub_text, font=font_sub)
    draw.text(((w - (bbox_s[2] - bbox_s[0]))//2, 340), sub_text, fill=(226, 232, 240, 255), font=font_sub)
    
    # Description
    desc_text = "400+ Verified Tools · WHO, NEC, ASHRAE, ACI & IEC Standards"
    bbox_d = draw.textbbox((0, 0), desc_text, font=font_sub)
    draw.text(((w - (bbox_d[2] - bbox_d[0]))//2, 390), desc_text, fill=(148, 163, 184, 255), font=font_sub)
    
    # Pill Badge: 100% Client-Side Privacy · Zero Telemetry · Free Forever
    pill_text = "⚡ 100% Client-Side Privacy  ·  Zero Telemetry  ·  Instant & Free"
    bbox_p = draw.textbbox((0, 0), pill_text, font=font_pill)
    pw = bbox_p[2] - bbox_p[0]
    px = (w - pw)//2
    py = 475
    draw.rounded_rectangle([px - 25, py - 12, px + pw + 25, py + 38], radius=25, fill=(30, 41, 59, 255), outline=(59, 130, 246, 255), width=2)
    draw.text((px, py), pill_text, fill=(96, 165, 250, 255), font=font_pill)
    
    # Border
    draw.rectangle([0, 0, w - 1, h - 1], outline=(30, 41, 59, 255), width=4)
    
    # Convert RGBA to RGB for standard web OG image
    rgb_img = Image.new('RGB', (w, h), (15, 23, 42))
    rgb_img.paste(img, mask=img.split()[3])
    rgb_img.save('og-image.png', format='PNG')
    rgb_img.save('assets/og-image.png', format='PNG')
    print("Created og-image.png and assets/og-image.png (1200x630)")

if __name__ == '__main__':
    generate_logo()
    generate_og_image()
