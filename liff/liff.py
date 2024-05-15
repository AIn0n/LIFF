from pathlib import Path


def center(children=None):
    print(Path(__file__).resolve())
    code = '<div style="width: 50%; margin: 0 auto; background-color: lightblue;">'
    for child in children:
        code += child
    code += "</div>"
    return code


def text(string: str):
    return f"<p> {string} </p>"


def button(child=None, action=None):
    return f"<button>{child}</button>"


def goto(path: str):
    pass
