from PIL import ImageGrab
from frik.main import get_text

def test():
    cords = ["817,0", "296x30"]

    left, upper = cords[0].split(",")
    length, height = cords[1].split("x")

    bbox = (int(left), int(upper), int(left)+int(length), int(upper)+int(height))
    image = ImageGrab.grab(bbox)

    text = get_text(image).strip().replace("\n", " ")

    assert text == "quandela@quandela-archlinux:~"
