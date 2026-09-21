from frik.main import get_text

def test() -> None:
    path = "./assets/text_1.png"
    text = get_text(path).strip().replace("\n", " ")

    with open("./assets/text_1.txt", "r", newline="") as f:
        real_text = f.read().strip().replace("\n", " ")

    assert text == real_text
