import os
import json
from PIL import Image, ImageDraw, ImageFont

def generate_pwa_icons():
    # Use existing logo.png (512x512) or draw cleanly
    size_512 = 512
    img512 = Image.new('RGBA', (size_512, size_512), (0, 0, 0, 0))
    draw512 = ImageDraw.Draw(img512)
    radius512 = 110
    draw512.rounded_rectangle([10, 10, size_512 - 10, size_512 - 10], radius=radius512, fill=(37, 99, 235, 255))
    
    try:
        font = ImageFont.truetype("arial.ttf", 320)
        bbox = draw512.textbbox((0, 0), "∑", font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (size_512 - w) / 2 - bbox[0]
        y = (size_512 - h) / 2 - bbox[1] - 15
        draw512.text((x, y), "∑", fill=(255, 255, 255, 255), font=font)
    except Exception as e:
        sigma_pts = [
            (120, 100), (392, 100), (392, 160), (240, 160),
            (300, 256), (240, 352), (392, 352), (392, 412),
            (120, 412), (120, 372), (220, 256), (120, 140)
        ]
        draw512.polygon(sigma_pts, fill=(255, 255, 255, 255))

    img512.save('android-chrome-512x512.png', format='PNG')
    print("Created android-chrome-512x512.png")

    img192 = img512.resize((192, 192), Image.Resampling.LANCZOS)
    img192.save('android-chrome-192x192.png', format='PNG')
    print("Created android-chrome-192x192.png")

def create_manifest():
    manifest_data = {
        "name": "CalcHub — Precision Scientific & Engineering Calculators",
        "short_name": "CalcHub",
        "description": "400+ Free precision calculators built to published mathematical, clinical, and industrial engineering standards. 100% private and client-side.",
        "start_url": "/",
        "display": "standalone",
        "background_color": "#FFFFFF",
        "theme_color": "#2563EB",
        "orientation": "any",
        "icons": [
            {
                "src": "/favicon-16x16.png",
                "sizes": "16x16",
                "type": "image/png"
            },
            {
                "src": "/favicon-32x32.png",
                "sizes": "32x32",
                "type": "image/png"
            },
            {
                "src": "/apple-touch-icon.png",
                "sizes": "180x180",
                "type": "image/png"
            },
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
                "purpose": "any maskable"
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
                "purpose": "any maskable"
            }
        ],
        "categories": [
            "education",
            "utilities",
            "productivity"
        ]
    }
    
    with open('site.webmanifest', 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2)
    print("Created site.webmanifest")

if __name__ == '__main__':
    generate_pwa_icons()
    create_manifest()
