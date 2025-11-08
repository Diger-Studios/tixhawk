#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

# Create 1200x630 image for OG (Open Graph) social sharing
width, height = 1200, 630
img = Image.new('RGB', (width, height), color='#ffffff')
draw = ImageDraw.Draw(img)

# Create gradient background (purple to pink)
for y in range(height):
    # Calculate color transition from purple (#667eea) to pink (#764ba2)
    r = int(102 + (118 - 102) * (y / height))
    g = int(126 + (75 - 126) * (y / height))
    b = int(234 + (162 - 234) * (y / height))
    draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))

# Try to use available system fonts, fallback to default
font_paths = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/System/Library/Fonts/Helvetica.ttc',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
]

title_font = None
subtitle_font = None

for font_path in font_paths:
    if os.path.exists(font_path):
        try:
            title_font = ImageFont.truetype(font_path, 90)
            subtitle_font = ImageFont.truetype(font_path, 45)
            break
        except:
            continue

# Fallback to default font if none found
if title_font is None:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()

# Add text content
title = "TicketHawk"
subtitle = "Never miss sold-out concerts again"
tagline = "Get instant alerts when last-minute tickets drop"

# Draw white text with shadow for better readability
shadow_offset = 4

# Title
title_bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = title_bbox[2] - title_bbox[0]
title_x = (width - title_width) // 2
title_y = 180

# Shadow
draw.text((title_x + shadow_offset, title_y + shadow_offset), title,
          font=title_font, fill=(0, 0, 0, 100))
# Main text
draw.text((title_x, title_y), title, font=title_font, fill='white')

# Subtitle
subtitle_bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
subtitle_x = (width - subtitle_width) // 2
subtitle_y = 300

draw.text((subtitle_x + shadow_offset, subtitle_y + shadow_offset), subtitle,
          font=subtitle_font, fill=(0, 0, 0, 80))
draw.text((subtitle_x, subtitle_y), subtitle, font=subtitle_font, fill='white')

# Tagline
tagline_bbox = draw.textbbox((0, 0), tagline, font=subtitle_font)
tagline_width = tagline_bbox[2] - tagline_bbox[0]
tagline_x = (width - tagline_width) // 2
tagline_y = 380

draw.text((tagline_x + shadow_offset, tagline_y + shadow_offset), tagline,
          font=subtitle_font, fill=(0, 0, 0, 80))
draw.text((tagline_x, tagline_y), tagline, font=subtitle_font, fill='white')

# Save the image
output_path = '/home/user/tixhawk/og-image.png'
img.save(output_path, 'PNG', optimize=True)
print(f"OG image created successfully at {output_path}")
