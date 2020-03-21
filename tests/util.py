def load_mockup(filename: str, encoding="utf-8"):
    with open(f"tests/mockups/{filename}", mode="r", encoding=encoding) as f:
        return f.read()
