from pytesseract import image_to_string
from subprocess import run
from pyperclip import copy

from PIL import ImageGrab

def main() -> None:
    cords = run(['slurp'], capture_output=True).stdout.decode().strip().split(" ")

    if cords == "":
        print("cancelling..")
        return

    left, upper = cords[0].split(",")
    length, height = cords[1].split("x")

    bbox = (int(left), int(upper), int(left)+int(length), int(upper)+int(height))
    image = ImageGrab.grab(bbox)

    text = get_text(image).strip().replace("\n", " ")

    if text == "":
        print("no text recognized.. exiting")
        return

    copy(text)
    print("text copied succesfully!")

def get_text(path) -> str:
    return image_to_string(path, lang="eng")
