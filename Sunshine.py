import json
from SunshineData import getSunshineData, saveSunshineData, getSupplySlope, getDemandSlope
from Algorithm import Algorithm
from Slopes import SlopeData

item_name = "Annihilation"
artifact_data = open('alpha_artifact.json', 'r')
items = json.load(artifact_data)
artifact_data.close()

for item in items:
    try:
        current_item = getSunshineData(item['name']) 

        current_item.slopeData = SlopeData(item_name, current_item.getSupplyListings(), current_item.getDemandListings())

        algorithm_data = {
            "demandPrice": current_item.getDemandPrice(0),
            "demandSlope": current_item.slopeData.getDemandSlopes()[0],
            "demandQuantity": current_item.getDemandCumulative(0),
            "supplyPrice": current_item.getSupplyPrice(0),
            "supplySlope" : current_item.slopeData.getSupplySlopes()[0],
            "supplyQuantity":current_item.getSupplyCumulative(0) 
        }

        sunshine = Algorithm(algorithm_data)

        try:
            print(saveSunshineData([current_item.getUID()],
                                sunshine.equilibrium_price, 
                                current_item.slopeData.supplySlopeData, 
                                current_item.slopeData.demandSlopeData))
        except Exception as e:
            print(e)
    except:
        print(f"Could not work with item {item['name']}")
