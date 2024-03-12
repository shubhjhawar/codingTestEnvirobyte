import plotly.graph_objects as go
import pandas as pd
import numpy as np

# extract the excel file
df = pd.read_excel("forecast_data.xlsx")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# synthetic data from historical inflation
historical_dates = pd.date_range(start='2000-01-01', end='2023-12-31', freq='M')
historical_inflation = np.random.normal(loc=2.5, scale=0.5, size=len(historical_dates))

# Hypothetical predicted inflation data after Jan 1st 2024
predicted_dates = pd.date_range(start='2024-01-01', end='2025-12-31', freq='M')
predicted_inflation = [3.0] * len(predicted_dates)

fig = go.Figure()

# other CIs - individual
# fig.add_trace(go.Scatter(x=df['date'], y=df['LB_50'], fill=None, mode='lines', line_color='red', name='LB_50'))
# fig.add_trace(go.Scatter(x=df['date'], y=df['UB_50'], fill='tonexty', mode='lines', line_color='red', name='UB_50'))
# fig.add_trace(go.Scatter(x=df['date'], y=df['LB_75'], fill=None, mode='lines', line_color='orange', name='LB_75'))
# fig.add_trace(go.Scatter(x=df['date'], y=df['UB_75'], fill='tonexty', mode='lines', line_color='orange', name='UB_75'))
# fig.add_trace(go.Scatter(x=df['date'], y=df['LB_95'], fill=None, mode='lines', line_color='pink', name='LB_95'))
# fig.add_trace(go.Scatter(x=df['date'], y=df['UB_95'], fill='tonexty', mode='lines', line_color='pink', name='UB_95'))

# other CIs - grouped together
fig.add_trace(go.Scatter(x=df['date'], y=df['UB_50'], mode='lines', line_color='red', name='50% CI', legendgroup="50% CI", showlegend=False))
fig.add_trace(go.Scatter(x=df['date'], y=df['LB_50'], mode='lines', line_color='red', fill='tonexty', name='50% CI', legendgroup="50% CI"))
fig.add_trace(go.Scatter(x=df['date'], y=df['UB_75'], mode='lines', line_color='orange',name='70% CI', legendgroup="70% CI", showlegend=False))
fig.add_trace(go.Scatter(x=df['date'], y=df['LB_75'], mode='lines', line_color='orange', fill='tonexty', name='70% CI', legendgroup="70% CI"))
fig.add_trace(go.Scatter(x=df['date'], y=df['UB_95'], mode='lines', line_color='pink', name='95% CI',legendgroup="95% CI", showlegend=False))
fig.add_trace(go.Scatter(x=df['date'], y=df['LB_95'], mode='lines', line_color='pink', fill='tonexty', name='95% CI', legendgroup="95% CI"))

# predicted data graph
fig.add_trace(go.Scatter(x=df['date'], y=df['value'], mode='lines', name='Forecast', line=dict(color='black', dash='dot')))

# historical data graph
fig.add_trace(go.Scatter(x=historical_dates, y=historical_inflation, name='Historical Inflation', mode='markers+lines', line_color='black'))


fig.update_layout(
    title_text="US Inflation"
)

# dark backgound
fig.update_layout(
    shapes=[
        dict(
            type="rect",
            xref="x",
            yref="paper",
            x0="2024-01-01",
            y0=0,
            x1="2025-07-1",
            y1=1,
            fillcolor="black",
            opacity=0.2,
            layer="below",
            line=dict(
                width=0,
            ),
        )
    ]
)

# range slider
fig.update_layout(
    xaxis=dict(
        # options / buttons
        rangeselector=dict(
            buttons=list([
                dict(count=5,
                     label="5y",
                     step="year",
                     stepmode="backward"),
                dict(count=10,
                     label="10y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date",
        range=['2023-01-01', '2025-07-1']
        # default
    )
)

fig.show()
