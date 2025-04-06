import os
from PIL import Image, ImageDraw, ImageFont
import sys

# List of required image files
required_images = [
    'static/images/loading.gif',
    'static/images/logo.png',
    'static/images/soil2e.jpg',
    'static/images/soil3e.jpg',
    'static/images/bannere.jpg',
    'static/images/banner.jpg',
    'static/images/soilpred.jpg',
    'static/images/cropdisease.jpg',
    'static/images/weather.jpg',
    'static/images/chose.jpg',
    'static/images/fevicon.png',
]

# Create placeholder images
for img_path in required_images:
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(img_path), exist_ok=True)
    
    # Skip if file already exists
    if os.path.exists(img_path):
        print(f"File already exists: {img_path}")
        continue
    
    # Determine image format
    if img_path.endswith('.gif'):
        # For GIF, create a simple white image
        img = Image.new('RGB', (200, 200), color='white')
        img.save(img_path, format='GIF')
    else:
        # For other formats, create an image with the filename as text
        img = Image.new('RGB', (400, 300), color='lightgray')
        draw = ImageDraw.Draw(img)
        
        # Add text with filename
        filename = os.path.basename(img_path)
        draw.text((50, 150), filename, fill='black')
        
        # Save in appropriate format
        if img_path.endswith('.png'):
            img.save(img_path, format='PNG')
        else:
            img.save(img_path, format='JPEG')
    
    print(f"Created placeholder: {img_path}")

print("All placeholder images created successfully!")

# List of required CSS files
required_css = [
    'static/css/bootstrap.min.css',
    'static/css/responsive.css',
    'static/css/owl.carousel.min.css',
    'static/css/normalize.css',
    'static/css/icomoon.css',
    'static/css/bootstrap-datepicker.min.css',
    'static/css/nice-select.css',
]

# Create placeholder CSS files
for css_path in required_css:
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(css_path), exist_ok=True)
    
    # Skip if file already exists
    if os.path.exists(css_path):
        print(f"File already exists: {css_path}")
        continue
    
    # Create a simple CSS file
    with open(css_path, 'w') as f:
        f.write(f"/* Placeholder for {os.path.basename(css_path)} */\n")
    
    print(f"Created placeholder: {css_path}")

print("All placeholder CSS files created successfully!")
