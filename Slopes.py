def calculateSlope(startPrice, startCumulative, nextPrice,  nextCumulative):
    return (nextPrice - startPrice) / (nextCumulative - startCumulative)

# currentPrice - previousPrice / currentCumulative - previousCumulative

def calculateSlopes(listings):
    slopes = []
    for i, listing in enumerate(listings):
        if i == 0:
            # First listing
            start_price = listing['price']    
            start_cumul = listing['cumulative_listings']
            next_price = listings[i+1]['price']
            next_cumul = listings[i+1]['cumulative_listings']
            slopes.append(calculateSlope(start_price, start_cumul, next_price, next_cumul))
            continue
        if i == len(listings)-1:
            # Last listing
            start_price = listings[i-1]['price']
            start_cumul = listings[i-1]['cumulative_listings']
            next_price = listing['price']
            next_cumul = listing['cumulative_listings']
            slopes.append(calculateSlope(start_price, start_cumul, next_price, next_cumul))
            continue
        prev_price = listings[i-1]['price']
        prev_cumul = listings[i-1]['cumulative_listings']
        next_price = listings[i+1]['price']
        next_cumul = listings[i+1]['cumulative_listings']
        slope = calculateSlope(prev_price, prev_cumul, next_price, next_cumul)
        slopes.append(slope)
    
    return slopes
