import plotly.graph_objects as go

import pandas as pd

from ipywidgets import interactive, HBox, VBox, widgets, interact

# Load data
df = pd.read_csv("finance-charts-apple.csv")
df.columns = [col.replace("AAPL.", "") for col in df.columns]

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.High)))

# Set title
fig.update_layout(
    title_text="Time series with range slider and selectors"
)

# Add range slider
fig.update_layout(
    xaxis=go.layout.XAxis(
        rangeselector=dict(
            buttons=list([
                dict(count=2,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# find the range of the slider.
xx, yy = fig['layout']['xaxis']['range']

xmax, xmin = 0, 0
# create FigureWidget from fig
f = go.FigureWidget(data=fig.data, layout=fig.layout)

slider = widgets.FloatRangeSlider(
    min=xmin,
    max=xmax,
    step=(xmax - xmin) / 1000.0,
    readout=False,
    description='Time')
slider.layout.width = '800px'


# our function that will modify the xaxis range
def update_range(y):
    f.layout.xaxis.range = [y[0], y[1]]


# display the FigureWidget and slider with center justification
vb = VBox((f, interactive(update_range, y=slider)))
vb.layout.align_items = 'center'
vb

fig.show()