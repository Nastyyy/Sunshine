from datetime import datetime
import DataHandler.DataHandler as db 


def getSunshineData(item_name):
    query = f"""
    {{
            items(func: eq(item_name, "{item_name}"), orderdesc: timestamp, first: 2) {{
                uid
                market_data {{
                    buy_order_graph {{
                        listings(orderdesc: price) {{
                            uid
                            price
                            amount_at_price
                            cumulative_listings
                        }}
                    }}
                    sell_order_graph {{
                        listings(orderasc: price) {{
                            uid
                            price
                            amount_at_price
                            cumulative_listings
                        }}
                    }}
                }}
            }}
        }}
    """
    items = db.query(query)
    marketItems = {
        "current_item": db.MarketItem(items['items'][0]),
        "previous_item": db.MarketItem(items['items'][1])
    }
    return marketItems 

# items_used should be an array of uids used
def saveSunshineData(items_used, equil_price, supplySlopeData, demandSlopeData):
    data = {
        "timestamp:": str(datetime.now()),
        "items.used": createUIDEdge(items_used),
        "equilibrium_price": equil_price,
        "supply_slopes": supplySlopeData,
        "demand_slopes": demandSlopeData
    }
    try:
        mutation = db.mutate(data)
    except Exception as e:
        print(e)
        mutation = e
    return mutation 

# Used to create edges that hold uid(s)
def createUIDEdge(items_used):
    uids = []
    for uid in items_used:
        uids.append({"uid": uid})
    return uids
