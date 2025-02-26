from PIL import Image, ImageFilter, ImageChops, ImageEnhance

def take_diff(before_image: Image, after_image: Image):
    return ImageChops.difference(before_image,after_image)

def find_edges(raw_image: Image) -> Image:
    image = raw_image.convert("L")
    return image.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.EDGE_ENHANCE_MORE).convert("RGBA")

def find_nonpassable(image: Image) -> Image:
    new_data = []
    for datum in image.getdata():
        new_data.append((255, 0, 0, datum[0] * 2))

    image.putdata(new_data)
    return image

before = Image.open("C:\\Users\\teamm\\PycharmProjects\\2024-2025-CubeSAT\\FinalProject\\test_files\\Milton_Before.png")
after = Image.open("C:\\Users\\teamm\\PycharmProjects\\2024-2025-CubeSAT\\FinalProject\\test_files\\Milton_After.png")
edge_before = find_nonpassable(find_edges(before))
edge_after = find_nonpassable(find_edges(after).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR).filter(ImageFilter.BLUR))
diff = take_diff(before, after)

Image.alpha_composite(after.convert("RGBA"), edge_after).show()

