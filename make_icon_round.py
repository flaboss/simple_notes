from PIL import Image, ImageDraw, ImageOps

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

def make_round_icon(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    
    # Create a mask for rounded corners
    # Apple uses a specific superellipse shape, but a simple rounded rectangle is a good approximation for now.
    # Standard curvature for macOS icons is roughly 22% of the size.
    
    size = img.size
    radius = int(min(size) * 0.22) # 22% radius
    
    # Create a rounded rectangle mask
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), size], radius=radius, fill=255)
    
    # Apply mask
    output = ImageOps.fit(img, size, centering=(0.5, 0.5))
    output.putalpha(mask)
    
    output.save(output_path)
    print(f"Saved rounded icon to {output_path}")

if __name__ == "__main__":
    make_round_icon("app/app_icon.png", "app/app_icon_rounded.png")
