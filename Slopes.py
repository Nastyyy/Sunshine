from SunshineData import getSupplySlope, getDemandSlope

class SlopeData:
    supplySlopeData = None
    demandSlopeData = None

    def __init__(self, item_name, supply_listings, demand_listings):
        self.item_name = item_name
        self.supplySlopeData = calculateListingSlopes(supply_listings)
        self.demandSlopeData = calculateListingSlopes(demand_listings) 
        try:
            self.checkForSupplySlopes()
            self.checkForDemandSlopes()
        except:
            pass

    def getSupplySlopes(self): 
        slopes = []
        for item in self.supplySlopeData:
            slopes.append(item['slope'])
        return slopes

    def getDemandSlopes(self):
        slopes = []
        for item in self.demandSlopeData:
            slopes.append(item['slope'])
        return slopes
    
    def checkForSupplySlopes(self):
        # check first and last slope for match price in
        # previous algoritm result
        firstCheckSlope = getSupplySlope(self.item_name, self.supplySlopeData[0]['index_price'])
        if firstCheckSlope is not None:
            self.supplySlopeData[0]['slope'] = firstCheckSlope['slope']
            self.supplySlopeData[0]['used_slope'] = True
            self.supplySlopeData[0]['slope.used'] = {"uid": firstCheckSlope['uid']}

        lastCheckSlope = getSupplySlope(self.item_name, self.supplySlopeData[len(self.supplySlopeData)-1]['index_price'])
        if lastCheckSlope is not None:
            self.supplySlopeData[len(self.supplySlopeData)-1]['slope'] = lastCheckSlope['slope']
            self.supplySlopeData[len(self.supplySlopeData)-1]['used_slope'] = True
            self.supplySlopeData[len(self.supplySlopeData)-1]['slope.used'] = {"uid": lastCheckSlope['uid']}
    
    def checkForDemandSlopes(self):
        # check first and last slope for match price in 
        # previous algorithm result
        firstCheckSlope = getDemandSlope(self.item_name, self.supplySlopeData[0]['index_price'])
        if firstCheckSlope is not None:
            self.demandSlopeData[0]['slope'] = firstCheckSlope['slope']
            self.demandSlopeData[0]['used_slope'] = True
            self.demandSlopeData[0]['slope.used'] = {"uid": firstCheckSlope['uid']}

        lastCheckSlope = getDemandSlope(self.item_name, self.supplySlopeData[len(self.supplySlopeData)-1]['index_price'])
        if lastCheckSlope is not None:
            self.demandSlopeData[len(self.supplySlopeData)-1]['slope'] = lastCheckSlope['slope']
            self.demandSlopeData[len(self.supplySlopeData)-1]['used_slope'] = True
            self.demandSlopeData[len(self.supplySlopeData)-1]['slope.used'] = {"uid": lastCheckSlope['uid']}

def calculateListingSlopes(listings):
    slopes = []
    for i, listing in enumerate(listings):
        if i == 0:
            # First listing
            start_price = listing['price']    
            start_cumul = listing['cumulative_listings']
            nextListing = listings[i+1]
            next_price = nextListing['price']
            next_cumul = nextListing['cumulative_listings']
            slope = calculateSlope(start_price, start_cumul, next_price, next_cumul)
            slopes.append(makeSlopeNode(i, slope, listing['price'], makeFirstListingNode(listing['uid'], nextListing['uid'])))
            continue
        if i == len(listings)-1:
            # Last listing
            startListing = listings[i-1]
            start_price = startListing['price']
            start_cumul = startListing['cumulative_listings']
            next_price = listing['price']
            next_cumul = listing['cumulative_listings']
            slope = calculateSlope(start_price, start_cumul, next_price, next_cumul)
            slopes.append(makeSlopeNode(i, slope, listing['price'], makeLastListingNode(startListing['uid'], listing['uid'])))
            continue
        # Inner listings
        prevListing = listings[i-1]
        prev_price = prevListing['price']
        prev_cumul = prevListing['cumulative_listings']
        nextListing = listings[i+1]
        next_price = nextListing['price']
        next_cumul = nextListing['cumulative_listings']
        slope = calculateSlope(prev_price, prev_cumul, next_price, next_cumul)
        slopes.append(makeSlopeNode(i, slope, listing['price'], makeInnerListingNode(prevListing['uid'], listing['uid'], nextListing['uid'])))
    return slopes

def calculateSlope(startPrice, startCumulative, nextPrice,  nextCumulative):
    return round((nextPrice - startPrice) / (nextCumulative - startCumulative), 3)

def makeSlopeNode(index, slope, index_price, listingNodes):
    return {
        "index": index,
        "slope": slope,
        "index_price": index_price, 
        "listings": listingNodes 
    }

def makeFirstListingNode(indexUID, nextUID):
    return {
        "index.listing": {
            "uid": indexUID
        },
        "next.listing": {
            "uid": nextUID
        }
    }

def makeLastListingNode(prevUID, indexUID):
    return {
        "previous.listing": {
            "uid": prevUID
        },
        "index.listing": {
            "uid": indexUID
        }
    }

def makeInnerListingNode(prevUID, indexUID, nextUID):
    return {
        "previous.listing": {
            "uid": prevUID
        },
        "index.listing": {
            "uid": indexUID
        },
        "next.listing": {
            "uid": nextUID
        }
    }