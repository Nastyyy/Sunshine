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
    marketItems = {
        "current_item": MarketItem(items['items'][0]),
        "previous_item": MarketItem(items['items'][1])
    }
    return marketItems 

def queryDB(query):
    client = newDgraphClient()
    data = client.query(query)
    return json.loads(data.json)

def newDgraphClient():
    client_stub = pydgraph.DgraphClientStub('localhost:9080')
    return pydgraph.DgraphClient(client_stub)

class MarketItem:
    def __init__(self, item):
        self.item = item

    def getMarketData(self):
        return self.item['market_data'][0]

    def getSupplyListings(self):
        return self.getMarketData()['sell_order_graph'][0]['listings']

    def getDemandListings(self):
        return self.getMarketData()['buy_order_graph'][0]['listings']

    def getSupplyListing(self, i):
        return self.getSupplyListings()[i]

    def getDemandListing(self, i):
        return self.getDemandListings()[i]

    def getSupplyPrice(self, i):
        return self.getSupplyListing(i)['price']

    def getDemandPrice(self, i):
        return self.getDemandListing(i)['price']

    ### AAP = amount_at_price
    def getSupplyAAP(self, i):
        return self.getSupplyListing(i)['amount_at_price']

    def getDemandAAP(self, i):
        return self.getDemandListing(i)['amount_at_price']
    ####
    
    def getSupplyCumulative(self, i):
        return self.getSupplyListing(i)['cumulative_listings']
    
    def getDemandCumulative(self, i):
        return self.getDemandListing(i)['cumulative_listings']

    ### Getters for all of a certain field in a MarketItem ###
    def getSupplyPrices(self):
        supplyPrices = []
        for listing in self.getSupplyListings():
            supplyPrices.append(listing['price'])
        return supplyPrices
    
    def getDemandPrices(self):
        demandPrices = []
        for listing in self.getDemandListings():
            demandPrices.append(listing['price'])
        return demandPrices

    ### End Getters ###