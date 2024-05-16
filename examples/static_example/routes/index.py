from liff import *

page(
    center(
        children=[
            text("Hello world"),
            button(text("go to other side"), action=goto("other_side/moon")),
        ]
    )
)
