from transformers import pipeline

from dash import Dash, Input, Output, State, callback
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

MODEL_ID = "facebook/galactica-1.3b"

pipe = pipeline("text-generation", model=MODEL_ID, tokenizer=MODEL_ID, device=0)

app = Dash(
    __name__, meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.title = "DE Semantic Search"

app.config.suppress_callback_exceptions = True

server = app.server


def generate_text(input_text):
    output = pipe(input_text, max_length=100)
    return output[0]["generated_text"]


app.layout = dmc.MantineProvider(
    theme={
        "colorScheme": "light",
        "fontFamily": "'Inter', sans-serif",
        "primaryColor": "indigo",
    },
    styles={"Button": {"root": {"fontWeight": 400}}},
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        dmc.Center(
            children=[
                dmc.SimpleGrid(
                    cols=2,
                    spacing="md",
                    children=[
                        dmc.TextInput(
                            label="Type a query",
                            id="input-text",
                        ),
                        dmc.Button(
                            id="search-button",
                            children="Search",
                        ),
                        dmc.Text(
                            id="model-output",
                        ),
                    ],
                )
            ],
        ),
    ],
)


@callback(
    Output("model-output", "children"),
    Input("search-button", "n_clicks"),
    State("input-text", "value"),
)
def update_output(n_clicks, input_text):
    if n_clicks is None:
        return ""
    output_text = generate_text(input_text)
    return output_text


if __name__ == '__main__':
    app.run_server()