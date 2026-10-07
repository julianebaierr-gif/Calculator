import os
from PIL import Image, ImageDraw, ImageFont

def create_svg():
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="14" fill="#2563EB"/>
  <text x="32" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif" font-size="38" font-weight="bold" fill="#FFFFFF" text-anchor="middle">&#x2211;</text>
</svg>'''
    with open('favicon.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Created favicon.svg")

def create_raster_favicons():
    # Render at high res first (256x256) then downscale with LANCZOS
    base_size = 256
    img = Image.new('RGBA', (base_size, base_size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw rounded rectangle
    # Radius = 56px for 256px
    radius = 56
    draw.rounded_rectangle([0, 0, base_size - 1, base_size - 1], radius=radius, fill=(37, 99, 235, 255))

    # Draw Sigma symbol
    # Try finding standard fonts or draw mathematically
    # Draw sigma symbol ∑ manually for perfect crispness or use font
    try:
        font = ImageFont.truetype("arial.ttf", 150)
        # Bounding box of character
        bbox = draw.textbbox((0, 0), "∑", font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (base_size - w) / 2 - bbox[0]
        y = (base_size - h) / 2 - bbox[1] - 8
        draw.text((x, y), "∑", fill=(255, 255, 255, 255), font=font)
    except Exception as e:
        print(f"Font loading fallback: {e}")
        # Draw Sigma polygon manually:
        # Top bar, top-right to center angle, bottom angle, bottom bar
        sigma_pts = [
            (60, 50), (196, 50), (196, 80), (120, 80),
            (150, 128), (120, 176), (196, 176), (196, 206),
            (60, 206), (60, 186), (110, 128), (60, 70)
        ]
        draw.polygon(sigma_pts, fill=(255, 255, 255, 255))

    # Save apple-touch-icon
    apple_img = img.resize((180, 180), Image.Resampling.LANCZOS)
    apple_img.save('apple-touch-icon.png', format='PNG')
    print("Created apple-touch-icon.png (180x180)")

    # 32x32 and 16x16 pngs
    img_32 = img.resize((32, 32), Image.Resampling.LANCZOS)
    img_32.save('favicon-32x32.png', format='PNG')
    img_16 = img.resize((16, 16), Image.Resampling.LANCZOS)
    img_16.save('favicon-16x16.png', format='PNG')
    print("Created favicon-32x32.png and favicon-16x16.png")

    # Save multi-size favicon.ico
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    ico_imgs = [img.resize(s, Image.Resampling.LANCZOS) for s in sizes]
    ico_imgs[0].save(
        'favicon.ico',
        format='ICO',
        sizes=sizes,
        append_images=ico_imgs[1:]
    )
    print("Created multi-size favicon.ico (16, 32, 48, 64)")

if __name__ == '__main__':
    create_svg()
    create_raster_favicons()
