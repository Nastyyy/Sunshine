import json
import Graph as graph
from SunshineData import getSunshineData, saveSunshineData
from Algorithm import Algorithm
from Slopes import SlopeData

items = getSunshineData("Time of Triumph") 

current_item = items['current_item']
previous_item = items['previous_item']

slopeData = SlopeData(current_item.getSupplyListings(), current_item.getDemandListings())

algorithm_data = {
    "demandPrice": current_item.getDemandPrice(0),
    "demandSlope": slopeData.getDemandSlopes()[0],
    "demandQuantity": current_item.getDemandCumulative(0),
    "supplyPrice": current_item.getSupplyPrice(0),
    "supplySlope" : slopeData.getSupplySlopes()[0],
    "supplyQuantity":current_item.getSupplyCumulative(0) 
}

sunshine = Algorithm(algorithm_data)

print(sunshine.equilibrium_price)

try:
    print(saveSunshineData([current_item.getUID(), previous_item.getUID()],
                           sunshine.equilibrium_price, 
                           slopeData.supplySlopeData, 
                           slopeData.demandSlopeData))
except Exception as e:
    print(e)

# Plotting logic. webGraph() for a share-able graph, 
# localGraph() for development or speed 
#graph.webGraph(current_item.getDemandPrices(), slopeData.getDemandSlopes(), current_item.getSupplyPrices(), slopeData.getSupplySlopes())
#graph.localGraph(current_item.getDemandPrices(), slopeData.getDemandSlopes(), current_item.getSupplyPrices(), slopeData.getSupplySlopes())