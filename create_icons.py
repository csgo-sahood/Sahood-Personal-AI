from PIL import Image, ImageDraw, ImageFont

for size in (192, 512):
    img = Image.new("RGB", (size, size), "#080808")
    draw = ImageDraw.Draw(img)

    margin = size // 12
    draw.rounded_rectangle(
        (margin, margin, size-margin, size-margin),
        radius=size//5,
        outline="#ff1010",
        width=max(3, size//100)
    )

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            size//3
        )
    except:
        font = ImageFont.load_default()

    text = "AI"
    box = draw.textbbox((0, 0), text, font=font)
    x = (size - (box[2]-box[0])) // 2
    y = (size - (box[3]-box[1])) // 2 - box[1]

    draw.text((x, y), text, fill="#ff2020", font=font)

    img.save(f"app/static/icon-{size}.png")

print("Sahood AI icons created successfully!")
