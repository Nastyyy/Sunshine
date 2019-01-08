import json
from Algorithm import Algorithm
from DataHandler import getSunshineData 
from Graph import webGraph, localGraph 
import Slopes as slopes

# Sell = Supply (people listing)
# Buy = Demand (people buying)

items = getSunshineData() 

current_gamma_data = items['items'][0]
previous_gamma_data = items['items'][1]

previous_buy_listings = previous_gamma_data['market_data'][0]['buy_order_graph'][0]['listings']
previous_sell_listings = previous_gamma_data['market_data'][0]['sell_order_graph'][0]['listings']
current_buy_listings = current_gamma_data['market_data'][0]['buy_order_graph'][0]['listings']
current_sell_listings = current_gamma_data['market_data'][0]['sell_order_graph'][0]['listings']

buyStartPrice = previous_buy_listings[0]['price']
buyNextPrice = previous_buy_listings[1]['price']
buyStartCumulative = previous_buy_listings[0]['amount_at_price']
buyNextCumulative = (previous_buy_listings[1]['amount_at_price'] + buyStartCumulative)

sellStartPrice = previous_sell_listings[0]['price']
sellNextPrice = previous_sell_listings[1]['price']
sellStartCumulative = previous_sell_listings[0]['amount_at_price']
sellNextCumulative = (previous_sell_listings[1]['amount_at_price'] + sellStartCumulative)

buySlope = slopes.calculateSlope(buyStartPrice, buyNextPrice, buyStartCumulative, buyNextCumulative)
sellSlope = slopes.calculateSlope(sellStartPrice, sellNextPrice, sellStartCumulative, sellNextCumulative)

algorithm_data = {
    "demandPrice": buyStartPrice,
    "demandSlope": buySlope,
    "demandQuantity": buyStartCumulative,
    "supplyPrice": sellStartPrice,
    "supplySlope" : sellSlope,
    "supplyQuantity": sellStartCumulative 
}

sunshine = Algorithm(algorithm_data)
price = sunshine.run()
print(price)

'''
current_buy_listings = items['items'][0]['market_data'][0]['buy_order_graph'][0]['listings']
current_sell_listings = items['items'][0]['market_data'][0]['sell_order_graph'][0]['listings']

buy_prices = []
sell_prices = []
for listing in current_buy_listings:
    buy_prices.append(listing['price'])
for listing in current_sell_listings:
    sell_prices.append(listing['price'])

buy_slopes = slopes.calculateSlopes(current_buy_listings)
sell_slopes = slopes.calculateSlopes(current_sell_listings)

# Plotting logic. webGraph() for a share-able graph, 
# local for development or speed 
#webGraph(buy_prices, buy_slopes, sell_prices, sell_slopes)
#localGraph(buy_slopes, buy_prices, sell_prices, sell_slopes)
'''