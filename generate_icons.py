"""
Generate PWA icons from SVG
Requires: pip install cairosvg pillow
"""

try:
    import cairosvg
    from PIL import Image
    import io
    import os
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'cairosvg', 'pillow'])
    import cairosvg
    from PIL import Image
    import io
    import os

# Icon sizes needed for PWA
ICON_SIZES = [72, 96, 128, 144, 152, 192, 384, 512]

# Paths
SVG_PATH = 'minor/myapp/static/icons/app-icon.svg'
OUTPUT_DIR = 'minor/myapp/static/icons'

def generate_icons():
    """Generate PNG icons from SVG"""
    
    # Create output directory if it doesn't exist
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print(f"Generating icons from {SVG_PATH}...")
    
    for size in ICON_SIZES:
        output_path = os.path.join(OUTPUT_DIR, f'icon-{size}x{size}.png')
        
        try:
            # Convert SVG to PNG
            png_data = cairosvg.svg2png(
                url=SVG_PATH,
                output_width=size,
                output_height=size
            )
            
            # Save PNG
            with open(output_path, 'wb') as f:
                f.write(png_data)
            
            print(f"✓ Generated {size}x{size} icon")
            
        except Exception as e:
            print(f"✗ Error generating {size}x{size} icon: {e}")
    
    print("\n✅ Icon generation complete!")
    print(f"Icons saved to: {OUTPUT_DIR}")

if __name__ == '__main__':
    generate_icons()
