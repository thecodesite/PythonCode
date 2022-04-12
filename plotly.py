#subplots
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=2, cols=2, subplot_titles=("Plot1", "Plot2", "Plot3", "Plot4"))

fig.add_trace(
    go.Scatter(x=df['x'], y=df['y']),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(x=df['x'], y=df['y']),
    row=1, col=2
)
#to add markers active mode
fig.add_trace(
    go.Scatter(x=df['x'], y=df['y'],mode='markers'),
    row=2, col=1
)

fig.add_trace(
    go.Scatter(x=df['x'], y=df['y'],mode='markers'),
    row=2, col=2
)

# Update xaxis properties
fig.update_xaxes(title_text="x1", row=1, col=1)
fig.update_xaxes(title_text="x2", row=1, col=2)
fig.update_xaxes(title_text="x3", row=2, col=1)
fig.update_xaxes(title_text="x4", row=2, col=2)


# Update yaxis properties
fig.update_yaxes(title_text="y1", row=1, col=1)
fig.update_yaxes(title_text="y2", row=1, col=2)
fig.update_yaxes(title_text="y3", row=2, col=1)
fig.update_yaxes(title_text="y4", row=2, col=2)


fig.update_layout(showlegend=False,height=700, width=900, title_text="Title")
fig.show()
