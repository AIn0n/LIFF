from liff.liff import *

center(
    children=[
        text("Hello world"),
        button(text("go to other side"), action=goto("other_side/moon")),
    ]
)
