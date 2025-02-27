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
    max = average
    for i in range(len(data) - 2):
        if data[i + 1][0] > 0:
            average = calculate_average(average, data[i + 1][0], num)
            num += 1
            if data[i + 1][0] > max:
                max = data[i + 1][0]

    multiplier = 255 / max

    for datum in image.getdata():
        if datum[0] >= average:
            new_data.append((255, 0, 0, int(datum[0] * multiplier)))
        else:
            new_data.append((0, 0, 0, 0))

    image.putdata(new_data)
    return image

after = Image.open("C:\\Users\\teamm\\PycharmProjects\\2024-2025-CubeSAT\\FinalProject\\test_files\\Milton_After.png")
edge_after = process_edges(find_edges(after.filter(ImageFilter.SHARPEN)).filter(ImageFilter.SMOOTH))

out = Image.alpha_composite(after.convert("RGBA"), edge_after)
out.putalpha(255)
out.show()

