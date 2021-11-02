from tempy.tags import Html, Head, Body, Div

test1 = Html()(
    Div()(
        Div()("Hi")
    )
)


test1.remove_attr(Head)

print(test1.html(pretty=True))