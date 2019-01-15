import pydgraph
import json 

def query(query):
    client = newDgraphClient()
    try:
        data = client.query(query)
    except:
        print("Coudld not query")
        return False 
    return json.loads(data.json)

def mutate(mutation):
    client = newDgraphClient()
    try:
        txn = client.txn()
        assigned = txn.mutate(set_obj=mutation)
        txn.commit()
        return assigned.uids['blank-0']
    except Exception as e:
        print("Could not do mutation")
        return e 

def newDgraphClient():
    client_stub = pydgraph.DgraphClientStub('localhost:9080')
    return pydgraph.DgraphClient(client_stub)

class MarketItem:
    def __init__(self, item):
        self.item = item

    def getUID(self):
        return self.item['uid']

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

    def getSupplyUID(self, i):
        return self.getSupplyListing(i)['uid']

    def getDemandUID(self, i):
        return self.getDemandListing(i)['uid']

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

    def getSupplyUIDs(self):
        supplyUIDs = []
        for listing in self.getSupplyListings():
            supplyUIDs.append(listing['uid'])
        return supplyUIDs

    def getDemandUIDs(self):
        demandUIDs = []
        for listing in self.getDemandListings():
            demandUIDs.append(listing['uid'])
        return demandUIDs
    ### End Getters ###