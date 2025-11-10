"""
Generate PWA icons using PIL only (no Cairo needed)
Creates simple gradient icons with text
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Icon sizes needed for PWA
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

# Paths
OUTPUT_DIR = 'minor/myapp/static/icons'

def create_icon(size):
    """Create a simple gradient icon with text"""
    
    # Create image with gradient background
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)
    
    # Create gradient (teal to green)
    for y in range(size):
        # Calculate color for this row
        ratio = y / size
        r = int(20 + (16 - 20) * ratio)
        g = int(184 + (185 - 184) * ratio)
        b = int(166 + (129 - 166) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))
    
    # Add rounded corners
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    corner_radius = size // 5
    mask_draw.rounded_rectangle([(0, 0), (size, size)], corner_radius, fill=255)
    
    # Apply mask
    output = Image.new('RGBA', (size, size))
    output.paste(img, (0, 0))
    output.putalpha(mask)
    
    # Add simple design elements
    draw = ImageDraw.Draw(output)
    
    # Draw a simple head silhouette (circle)
    head_size = size // 3
    head_x = size // 2
    head_y = size // 3
    draw.ellipse(
        [(head_x - head_size//2, head_y - head_size//2),
         (head_x + head_size//2, head_y + head_size//2)],
        fill=(255, 255, 255, 200)
    )
    
    # Draw hair strands (simple lines)
    strand_length = size // 6
    for i in range(-2, 3):
        x = head_x + (i * size // 15)
        y_start = head_y - head_size//2
        y_end = y_start - strand_length
        draw.line([(x, y_start), (x, y_end)], fill=(255, 255, 255, 180), width=max(2, size//100))
    
    # Add medical cross at bottom
    cross_size = size // 8
    cross_x = size // 2
    cross_y = size * 2 // 3
    cross_width = max(2, size // 50)
    
    # Vertical bar
    draw.rectangle(
        [(cross_x - cross_width, cross_y - cross_size//2),
         (cross_x + cross_width, cross_y + cross_size//2)],
        fill=(255, 255, 255, 200)
    )
    # Horizontal bar
    draw.rectangle(
        [(cross_x - cross_size//2, cross_y - cross_width),
         (cross_x + cross_size//2, cross_y + cross_width)],
        fill=(255, 255, 255, 200)
    )
    
    # Try to add text (if font available)
    try:
        font_size = size // 10
        try:
            font = ImageFont.truetype("arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        text = "HAIR AI"
        # Get text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        text_x = (size - text_width) // 2
        text_y = size - size // 6
        
        draw.text((text_x, text_y), text, fill=(255, 255, 255, 220), font=font)
    except:
        pass  # Skip text if font not available
    
    return output

def generate_icons():
    """Generate PNG icons"""
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("=" * 70)
    print("Generating PWA Icons")
    print("=" * 70)
    print()
    
    for size in ICON_SIZES:
        output_path = os.path.join(OUTPUT_DIR, f'icon-{size}x{size}.png')
        
        try:
            icon = create_icon(size)
            icon.save(output_path, 'PNG')
            print(f"✓ Generated {size}x{size} icon")
            
        except Exception as e:
            print(f"✗ Error generating {size}x{size} icon: {e}")
    
    print()
    print("=" * 70)
    print("✅ Icon generation complete!")
    print(f"Icons saved to: {OUTPUT_DIR}")
    print("=" * 70)

if __name__ == '__main__':
    generate_icons()
