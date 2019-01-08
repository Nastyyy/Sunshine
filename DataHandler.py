import pydgraph
import json 

query = """
{
        items(func: eq(item_name, "Time of Triumph"), orderdesc: timestamp, first: 2) {
            market_data {
                buy_order_graph {
                    listings(orderdesc: price) {
                        price
                        amount_at_price
                        cumulative_listings
                    }
                }
                sell_order_graph {
                    listings(orderasc: price) {
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
    items = queryDB(query)

def queryDB(query):
    client = newDgraphClient()
    data = client.query(query)
    return json.loads(data.json)

def newDgraphClient():
    client_stub = pydgraph.DgraphClientStub('localhost:9080')
    return pydgraph.DgraphClient(client_stub)

class Item:
    def __init__(self, item):
