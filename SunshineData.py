import DataHandler.DataHandler as db 

query = """
{
        items(func: eq(item_name, "Time of Triumph"), orderdesc: timestamp, first: 2) {
            uid
            market_data {
                buy_order_graph {
                    listings(orderdesc: price) {
                        uid
                        price
                        amount_at_price
                        cumulative_listings
                    }
                }
                sell_order_graph {
                    listings(orderasc: price) {
                        uid
                        price
                        amount_at_price
                        cumulative_listings
                    }
                }
            }
        }
    }
"""

def getSunshineData():
    items = db.query(query)
    marketItems = {
        "current_item": db.MarketItem(items['items'][0]),
        "previous_item": db.MarketItem(items['items'][1])
    }
    return marketItems 

def saveSunshineData(equil_price, supplySlopeData, demandSlopeData):
    data = {
        "equilibrium_price": equil_price,
        "supply_slopes": supplySlopeData,
        "demand_slopes": demandSlopeData
    }
    return db.mutate(data)
