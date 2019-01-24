from datetime import datetime
import DataHandler.DataHandler as db 
import Queries as query


def getSunshineData(item_name):
    item = db.query(query.marketItems(item_name))
    return db.MarketItem(item['item'][0])

# items_used should be an array of uid(s) used
def saveSunshineData(items_used, equil_price, supplySlopeData, demandSlopeData):
    data = {
        "algorithm_tag": "Sunshine",
        "timestamp": datetime.now().isoformat(),
        "items.used": createUIDEdge(items_used),
        "equilibrium_price": equil_price,
        "supply.slopes": supplySlopeData,
        "demand.slopes": demandSlopeData
    }
    try:
        return db.mutate(data)
    except Exception as e:
        return e
    
def getSupplySlope(item_name, price):
    result = db.query(query.getPreviousSupplySlope(item_name, price))
    if len(result['result']) == 0:
        return None
    return result['result'][0]

def getDemandSlope(item_name, price):
    result = db.query(query.getPreviousDemandSlope(item_name, price))
    if len(result['result']) == 0:
        return None
    return result['result'][0]

# Used to create edges that hold uid(s)
def createUIDEdge(items_used):
    uids = []
    for uid in items_used:
        uids.append({"uid": uid})
    return uids