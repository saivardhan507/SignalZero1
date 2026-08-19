import math
from PIL import Image, ImageDraw, ImageFilter, ImageFont

def create_signal_zero_logo(size=300, bg_color=(5, 8, 20), transparent=False, filename="public/signal-zero-logo-300x300.png"):
    scale = 4
    canvas_size = size * scale
    
    if transparent:
        img = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    else:
        img = Image.new("RGBA", (canvas_size, canvas_size), (*bg_color, 255))
        
        # Subtle radial cyber glow in background
        glow = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow)
        cx, cy = canvas_size // 2, canvas_size // 2
        max_r = canvas_size * 0.45
        for r in range(int(max_r), 0, -10):
            alpha = int(22 * (1 - r / max_r))
            glow_draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 204, 255, alpha))
        glow = glow.filter(ImageFilter.GaussianBlur(radius=25))
        img = Image.alpha_composite(img, glow)

    draw = ImageDraw.Draw(img)
    cx, cy = canvas_size / 2, canvas_size / 2

    # Outer ring
    r_outer = canvas_size * 0.42
    draw.ellipse([cx - r_outer, cy - r_outer, cx + r_outer, cy + r_outer], outline=(0, 204, 255, 76), width=int(1.2 * scale))

    # Middle ring
    r_mid = canvas_size * 0.31
    draw.ellipse([cx - r_mid, cy - r_mid, cx + r_mid, cy + r_mid], outline=(0, 204, 255, 160), width=int(1.8 * scale))

    # Inner sine signal wave
    points = []
    width_span = canvas_size * 0.65
    start_x = cx - width_span / 2
    amplitude = canvas_size * 0.16
    
    for i in range(300):
        t = i / 299.0
        x = start_x + t * width_span
        y = cy - math.sin(t * math.pi * 2.0) * amplitude
        points.append((x, y))

    # Draw wave
    line_width = int(2.8 * scale)
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=(0, 204, 255, 255), width=line_width)

    # Center glowing node
    r_center = canvas_size * 0.052
    draw.ellipse([cx - r_center, cy - r_center, cx + r_center, cy + r_center], fill=(0, 204, 255, 255))
    
    r_glow = r_center * 1.5
    draw.ellipse([cx - r_glow, cy - r_glow, cx + r_glow, cy + r_glow], outline=(0, 204, 255, 100), width=int(1 * scale))

    final_img = img.resize((size, size), Image.Resampling.LANCZOS)
    final_img.save(filename, format="PNG", optimize=True)
    print(f"Generated: {filename} ({size}x{size})")

def create_linkedin_banner(width=1128, height=191, filename="public/signal-zero-linkedin-banner.png"):
    scale = 2
    W, H = width * scale, height * scale
    
    img = Image.new("RGBA", (W, H), (5, 8, 20, 255))
    
    # Add background wave lines & cyber glow
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)
    
    # Left cyan glow
    glow_draw.ellipse([W * 0.05, -H * 0.5, W * 0.45, H * 1.5], fill=(0, 204, 255, 25))
    # Right purple glow
    glow_draw.ellipse([W * 0.65, -H * 0.5, W * 1.05, H * 1.5], fill=(123, 47, 255, 20))
    glow = glow.filter(ImageFilter.GaussianBlur(radius=40))
    img = Image.alpha_composite(img, glow)
    
    draw = ImageDraw.Draw(img)
    
    # Draw perspective grid lines
    grid_color = (255, 255, 255, 12)
    for x in range(0, W, 80):
        draw.line([(x, 0), (x, H)], fill=grid_color, width=1)
    for y in range(0, H, 40):
        draw.line([(0, y), (W, y)], fill=grid_color, width=1)
        
    # Draw ambient signal wave across the banner
    wave_pts = []
    for i in range(W):
        t = i / float(W)
        y = (H * 0.5) + math.sin(t * 16.0) * (H * 0.18) + math.cos(t * 8.0) * (H * 0.08)
        wave_pts.append((i, y))
        
    for i in range(len(wave_pts) - 1):
        draw.line([wave_pts[i], wave_pts[i+1]], fill=(0, 204, 255, 60), width=2)
        
    # Draw logo icon on left
    logo_cx = int(W * 0.12)
    logo_cy = int(H * 0.5)
    r_out = int(H * 0.32)
    r_in = int(H * 0.22)
    draw.ellipse([logo_cx - r_out, logo_cy - r_out, logo_cx + r_out, logo_cy + r_out], outline=(0, 204, 255, 90), width=3)
    draw.ellipse([logo_cx - r_in, logo_cy - r_in, logo_cx + r_in, logo_cy + r_in], outline=(0, 204, 255, 180), width=4)
    
    # Icon wave
    pts_icon = []
    span = r_out * 1.4
    for i in range(100):
        t = i / 99.0
        x = (logo_cx - span/2) + t * span
        y = logo_cy - math.sin(t * math.pi * 2.0) * (r_out * 0.4)
        pts_icon.append((x, y))
    for i in range(len(pts_icon) - 1):
        draw.line([pts_icon[i], pts_icon[i+1]], fill=(0, 204, 255, 255), width=5)
    draw.ellipse([logo_cx - 8, logo_cy - 8, logo_cx + 8, logo_cy + 8], fill=(0, 204, 255, 255))
    
    # Text
    try:
        # Load system font if available, else default
        font_title = ImageFont.truetype("arialbd.ttf", 52)
        font_sub = ImageFont.truetype("arial.ttf", 22)
        font_badge = ImageFont.truetype("arialbd.ttf", 20)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_badge = ImageFont.load_default()

    draw.text((logo_cx + r_out + 30, logo_cy - 38), "SIGNAL ZERO", font=font_title, fill=(255, 255, 255, 255))
    draw.text((logo_cx + r_out + 32, logo_cy + 18), "INTEGRATED AI & SYSTEMS ENGINEERING", font=font_sub, fill=(0, 204, 255, 230))
    
    # Right tags / badges
    draw.text((W - 550, logo_cy - 20), "• Custom AI Agents", font=font_badge, fill=(240, 244, 255, 220))
    draw.text((W - 550, logo_cy + 12), "• Real-Time Data Pipelines", font=font_badge, fill=(240, 244, 255, 220))
    draw.text((W - 250, logo_cy - 20), "• Sub-Second ML", font=font_badge, fill=(0, 204, 255, 240))
    draw.text((W - 250, logo_cy + 12), "• wearesignalzero.tech", font=font_badge, fill=(0, 204, 255, 240))
    
    final_img = img.resize((width, height), Image.Resampling.LANCZOS)
    final_img.save(filename, format="PNG", optimize=True)
    print(f"Generated: {filename} ({width}x{height})")

if __name__ == "__main__":
    create_signal_zero_logo(size=300, bg_color=(5, 8, 20), filename="public/signal-zero-logo-300x300.png")
    create_signal_zero_logo(size=800, bg_color=(5, 8, 20), filename="public/signal-zero-logo-800x800.png")
    create_signal_zero_logo(size=300, transparent=True, filename="public/signal-zero-logo-transparent.png")
    create_linkedin_banner(width=1128, height=191, filename="public/signal-zero-linkedin-banner.png")
