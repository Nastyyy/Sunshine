import json
from Algorithm import Algorithm
from DataHandler import getSunshineData 
from Graph import webGraph, localGraph 
import Slopes as slopes

items = getSunshineData() 

current_item = items['current_item']
previous_item = items['previous_item']

demandSlope = slopes.calculateSlope(current_item.getDemandPrice(0), 
                                    current_item.getDemandCumulative(0), 
                                    current_item.getDemandPrice(1), 
                                    current_item.getDemandCumulative(1))

supplySlope = slopes.calculateSlope(current_item.getSupplyPrice(0), 
                                    current_item.getSupplyCumulative(0), 
                                    current_item.getSupplyPrice(1), 
                                    current_item.getSupplyCumulative(1))

algorithm_data = {
    "demandPrice": current_item.getDemandPrice(0),
    "demandSlope": demandSlope,
    "demandQuantity": current_item.getDemandCumulative(0),
    "supplyPrice": current_item.getSupplyPrice(0),
    "supplySlope" : supplySlope,
    "supplyQuantity":current_item.getSupplyCumulative(0) 
}

sunshine = Algorithm(algorithm_data)
price = sunshine.run()

print(price)

demandSlopes = slopes.calculateSlopes(current_item.getDemandListings())
supplySlopes = slopes.calculateSlopes(current_item.getSupplyListings())

# Plotting logic. webGraph() for a share-able graph, 
# localGraph() for development or speed 
#webGraph(buy_prices, buy_slopes, sell_prices, sell_slopes)
#localGraph(current_item.getDemandPrices(), demandSlopes, current_item.getSupplyPrices(), supplySlopes)