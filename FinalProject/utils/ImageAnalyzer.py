from PIL import Image, ImageFilter, ImageChops

def take_diff(before_image:str, after_image:str):
    bfr = Image.open(before_image)
    aftr = Image.open(after_image)
    diff = ImageChops.difference(bfr,aftr)
    return diff

def find_nonpassable(after_image:str):
    image = Image.open(after_image)
    image = Image.convert("L")
    edges = image.filter(imageFilter.FIND_EDGES)
    nonpassable = edges.filter(imageFilter.BLUR)


    