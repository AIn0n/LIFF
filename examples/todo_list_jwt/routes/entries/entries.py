(state, this, global_state, view_model) = essentials()

view_model = auth_wrapper(view_model, global_state["jwt"])

center(
    children=[
        is_empty(state["entries"])
        .then(text("No entries found, add something here!"))
        .ellse(
            state["entries"].for_each(
                lambda x: row(
                    children=[
                        text(x.text),
                        button(
                            clicked=view_model.remove(x.id),
                            text="X",
                        ),
                    ]
                )
            )
        ),
        row(
            children=[
                text_area(value=this["new_entry"]),
                button(clicked=view_model.add(this["new_entry"])),
            ]
        ),
    ]
)
