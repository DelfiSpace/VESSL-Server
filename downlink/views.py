from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from tempy.tags import Html, Head, Body, Meta, Header, Title, Link, Div, P, A, H1, H2, Fieldset, Legend, Table, Tr, Th,\
    Td, Footer, Img
from tempy.widgets import TempyTable

frame1 = {}
for i in range(1, 4):
    frame1[i] = ["var" + str(i), "val" + str(i), "unit" + str(i)]


# Adding a view that returns some generated HTML code inside a HttpResponse
def index(request):
    # return HttpResponse("Hello World!")
    # return HttpResponse(generate_downlink_gui(frame1))

    # downlink_table = "<h2>I am a downlink table.</h2>"
    downlink_table = generate_downlink_gui(frame1)
    return render(request, 'downlink/index.html', {'downlink_table': downlink_table})


def generate_downlink_gui_old(frame):

    def dict_to_tabledata(frame: dict, headers: list):
        tabledata = [headers]
        {tabledata.append(val) for key, val in frame.items()}
        return tabledata

    table_headers = ["Variable", "Value", "Unit"]
    table_data = dict_to_tabledata(frame, table_headers)
    table_rows = len(table_data)
    table_cols = len(table_data[0])

    datatable1 = TempyTable(rows=table_rows,
                            cols=table_cols,
                            data=table_data,
                            head=True,
                            caption="A nice test table",
                            width="100%",
                            klass="data_table",
                            )

    gui_html = Html()(
        Head()(
            Link(rel="stylesheet", href="style.css"),
            Title()("Test webpage"),
            Meta(charset='utf-8'),
            Meta(name="viewport"),
            Meta(content="width=device-width, initial-scale=1"),
        ),
        body=Body()(
            Header()(
                Div(klass="cols")(
                    Div(klass="headerA")(
                        H1()("Data Frame"),
                    ),
                    Div(klass="headerB")(
                        Img(alt="VESSL logo", src="vessl_logo_small.png"),
                    ),
                ),
            ),
            Div(klass="cols")(
                Div(klass="fsA")(
                    Fieldset()(
                        Legend()("Data entries:"),
                        datatable1,
                    ),
                ),
                Div(klass="fsB")(
                    Fieldset()(
                        Legend()("Data entries 2 - Electric Boogaloo:"),
                        datatable1,
                    ),
                ),
            ),
            Footer()(
                Div(klass="cols")(
                    Div(klass="footerA")(
                        H2()("Footer")
                    ),
                    Div(klass="footerB")(
                        Img(alt="TU Delft logo", src="tu_logo_small.png"),
                    ),
                ),
            ),
        ),
    )

    datatable1.col_class("td-rightalign", 1)

    # print(gui_html.render(pretty=True))

    return gui_html.render()


def generate_downlink_gui(frame):

    def dict_to_tabledata(frame: dict, headers: list):
        tabledata = [headers]
        {tabledata.append(val) for key, val in frame.items()}
        return tabledata

    table_headers = ["Variable", "Value", "Unit"]
    table_data = dict_to_tabledata(frame, table_headers)
    table_rows = len(table_data)
    table_cols = len(table_data[0])

    datatable1 = TempyTable(rows=table_rows,
                            cols=table_cols,
                            data=table_data,
                            head=True,
                            caption="A nice test table",
                            width="100%",
                            klass="data_table",
                            )

    gui_html = Div(klass="cols")(
        Div(klass="fsA")(
            Fieldset()(
                Legend()("Data entries:"),
                datatable1,
            ),
        ),
        Div(klass="fsB")(
            Fieldset()(
                Legend()("Data entries 2 - Electric Boogaloo:"),
                datatable1,
            ),
        ),
    )

    datatable1.col_class("td-rightalign", 1)

    # print(gui_html.render(pretty=True))

    return gui_html.html()


# test = generate_downlink_gui(frame1)







