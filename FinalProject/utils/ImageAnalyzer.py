from PIL import Image, ImageFilter, ImageChops, ImageEnhance

from FinalProject.utils.misc import calculate_average


def take_diff(before_image: Image, after_image: Image):
    return ImageChops.difference(before_image,after_image)

def find_edges(raw_image: Image) -> Image:
    image = raw_image.convert("L")
    return image.filter(ImageFilter.FIND_EDGES).filter(ImageFilter.EDGE_ENHANCE_MORE).convert("RGBA")

def process_edges(image: Image) -> Image:
    new_data = []
    data = image.getdata()
    average = data[0][0]
    num = 1
    for i in range(len(data) - 2):
        if data[i + 1][0] > 5:
            average = calculate_average(average, data[i + 1][0], num)
            num += 1

    for datum in image.getdata():
        if datum[0] >= average:
            new_data.append((255, 0, 0, 255))
        else:
            new_data.append((0, 0, 0, 0))

    image.putdata(new_data)
    return image

before = Image.open("C:\\Users\\teamm\\PycharmProjects\\2024-2025-CubeSAT\\FinalProject\\test_files\\Milton_Before.png")
after = Image.open("C:\\Users\\teamm\\PycharmProjects\\2024-2025-CubeSAT\\FinalProject\\test_files\\Milton_After.png")
edge_before = process_edges(find_edges(before))
edge_after = process_edges(find_edges(after).filter(ImageFilter.SMOOTH))
diff = take_diff(before, after)

out = Image.alpha_composite(after.convert("RGBA"), edge_after)
out.putalpha(255)
out.show()

