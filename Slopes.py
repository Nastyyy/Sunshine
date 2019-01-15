class SlopeData:
    supplySlopeData = None
    demandSlopeData = None

    def __init__(self, supply_slopes, demand_slopes):
        self.supplySlopeData = supply_slopes
        self.demandSlopeData = demand_slopes

def calculateSlopes(marketItem):
    return SlopeData(calculateListingSlopes(marketItem.getSupplyListings()), calculateListingSlopes(marketItem.getDemandListings()))

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
            slopes.append(makeSlopeNode(i, slope, makeFirstListingNode(listing['uid'], nextListing['uid'])))
            continue
        if i == len(listings)-1:
            # Last listing
            startListing = listings[i-1]
            start_price = startListing['price']
            start_cumul = startListing['cumulative_listings']
            next_price = listing['price']
            next_cumul = listing['cumulative_listings']
            slope = calculateSlope(start_price, start_cumul, next_price, next_cumul)
            slopes.append(makeSlopeNode(i, slope, makeLastListingNode(startListing['uid'], listing['uid'])))
            continue
        # Inner listings
        prevListing = listings[i-1]
        prev_price = prevListing['price']
        prev_cumul = prevListing['cumulative_listings']
        nextListing = listings[i+1]
        next_price = nextListing['price']
        next_cumul = nextListing['cumulative_listings']
        slope = calculateSlope(prev_price, prev_cumul, next_price, next_cumul)
        slopes.append(makeSlopeNode(i, slope, makeInnerListingNode(prevListing['uid'], listing['uid'], nextListing['uid'])))
    return slopes

def calculateSlope(startPrice, startCumulative, nextPrice,  nextCumulative):
    return (nextPrice - startPrice) / (nextCumulative - startCumulative)

def makeSlopeNode(index, slope, listingNodes):
    return {
        "index": index,
        "slope": slope,
        "listings": listingNodes 
    }

def makeFirstListingNode(indexUID, nextUID):
    return {
        "index_listing": {
            "uid": indexUID
        },
        "next_listing": {
            "uid": nextUID
        }
    }

def makeLastListingNode(prevUID, indexUID):
    return {
        "previous_listing": {
            "uid": prevUID
        },
        "index_listing": {
            "uid": indexUID
        }
    }

def makeInnerListingNode(prevUID, indexUID, nextUID):
    return {
        "previous_listing": {
            "uid": prevUID
        },
        "index_listing": {
            "uid": indexUID
        },
        "next_listing": {
            "uid": nextUID
        }
    }