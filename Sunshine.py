import json
import Graph as graph
from SunshineData import getSunshineData, saveSunshineData
from Algorithm import Algorithm
import Slopes as slopes

items = getSunshineData() 

current_item = items['current_item']
previous_item = items['previous_item']

#print(json.dumps(slopes.calculateSlopes(current_item)['supply_slopes'], indent=2, sort_keys=True))
slopeData = slopes.calculateSlopes(current_item)

'''
demandSlope = slopes.calculateSlope(current_item.getDemandPrice(0), 
                                    current_item.getDemandCumulative(0), 
                                    current_item.getDemandPrice(1), 
                                    current_item.getDemandCumulative(1))

supplySlope = slopes.calculateSlope(current_item.getSupplyPrice(0), 
                                    current_item.getSupplyCumulative(0), 
                                    current_item.getSupplyPrice(1), 
                                    current_item.getSupplyCumulative(1))
'''

supplySlope = slopeData.supplySlopeData[0]['slope']
demandSlope = slopeData.demandSlopeData[0]['slope']

algorithm_data = {
    "demandPrice": current_item.getDemandPrice(0),
    "demandSlope": demandSlope,
    "demandQuantity": current_item.getDemandCumulative(0),
    "supplyPrice": current_item.getSupplyPrice(0),
    "supplySlope" : supplySlope,
    "supplyQuantity":current_item.getSupplyCumulative(0) 
}

sunshine = Algorithm(algorithm_data)

print(saveSunshineData(sunshine.equilibrium_price, 
                       slopeData.supplySlopeData, 
                       slopeData.demandSlopeData))

### TODO: Update to fit new calculateSlopes logic ###
# Plotting logic. webGraph() for a share-able graph, 
# localGraph() for development or speed 
#graph.webGraph(current_item.getDemandPrices(), slopeData.getDemandSlopes(), current_item.getSupplyPrices(), slopeData.getSupplySlopes())
#graph.localGraph(current_item.getDemandPrices(), slopeData.getDemandSlopes(), current_item.getSupplyPrices(), slopeData.getSupplySlopes())