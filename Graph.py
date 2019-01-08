import plotly.plotly as plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt 

def webGraph(buy_prices, buy_slopes, sell_prices, sell_slopes):
    buy_trace = go.Scatter(
        x = buy_prices,
        y = buy_slopes,
        name = 'Buy Slopes',
        line = dict(
            color = ('rgb(22, 96, 167)'),
            width = 4,)
    )

    sell_trace = go.Scatter(
        x = sell_prices,
        y = sell_slopes,
        name = 'Sell Slopes',
        line = dict(
            color = ('rgb(167, 25, 25)'),
            width = 4,)
    )

    data = [buy_trace, sell_trace]

    layout = dict(title = 'Slopes at price for buy and sell orders',
                xaxis = dict(title = 'Price'),
                yaxis = dict(title = 'Slope'),
                )

    fig = dict(data=data, layout=layout)
    plotly.iplot(fig, filename='slopes')

def localGraph(buy_slopes, buy_prices, sell_prices, sell_slopes):
    plt.plot(buy_prices, buy_slopes, label='Buy Slopes')
    plt.plot(sell_prices, sell_slopes, label='Sell Slopes')
    plt.xlabel('Prices')
    plt.ylabel('Slopes')
    plt.title('Slopes at Price')
    plt.legend()
    plt.show()