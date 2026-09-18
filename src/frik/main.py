from pytesseract import image_to_string
from datetime import datetime
from subprocess import run
from pyperclip import copy

def main() -> None:
    cords = run(['slurp'], capture_output=True).stdout.decode().strip()

    if cords == "":
        print("cancelling..")
        return

    path = f"/home/quandela/Images/frik_{datetime.now()}.png"
    run(['grim', '-g', cords, path])

    print(f"saved screenshot in {path}\n")
    text = get_text(path).strip()

    if text == "":
        print("no text recognized.. exiting")
        return

    copy(text)
    print("text copied succesfully!")

def get_text(path) -> str:
    return image_to_string(path, lang="eng")
