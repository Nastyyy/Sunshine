import plotly.plotly as plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt 

def webGraph(demandPrices, demandSlopes, supplyPrices, supplySlopes):
    demand_trace = go.Scatter(
        x = demandPrices,
        y = demandSlopes,
        name = 'Demand Slopes',
        line = dict(
            color = ('rgb(22, 96, 167)'),
            width = 4,)
    )

    supply_trace = go.Scatter(
        x = supplyPrices,
        y = supplySlopes,
        name = 'Supply Slopes',
        line = dict(
            color = ('rgb(167, 25, 25)'),
            width = 4,)
    )

    data = [demand_trace, supply_trace]

    layout = dict(title = 'Slopes at price for supply and demand',
                xaxis = dict(title = 'Price'),
                yaxis = dict(title = 'Slope'),
                )

    fig = dict(data=data, layout=layout)
    plotly.iplot(fig, filename='slopes')

def localGraph(demandPrices, demandSlopes, supplyPrices, supplySlopes):
    plt.plot(demandPrices, demandSlopes, label='Demand Slopes')
    plt.plot(supplyPrices, supplySlopes, label='Supply Slopes')
    plt.xlabel('Prices')
    plt.ylabel('Slopes')
    plt.title('Slopes at Price')
    plt.legend()
    plt.show()