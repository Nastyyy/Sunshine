# itemQuery is the query for the items needed in Sunshine
def marketItems(item_name):
    return f"""
        {{
            item(func: eq(item_name, "{item_name}"), orderdesc: timestamp, first: 1) {{
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

# previousItem is the query for getting the previous 
# algorithm result for a given item_name
def previousItem(item_name):
    return f"""
        {{
            items as var(func: eq(algorithm_tag, "Sunshine")) @cascade {{
                items.used @filter(eq(item_name, "{item_name}"))
            }}
                
            sunshine(func: uid(items), orderdesc: timestamp, first: 1) {{
                timestamp
            }}
        }}
    """

def getPreviousDemandSlope(item_name, price):
    return f"""
    {{
            items as var(func: eq(algorithm_tag, "Sunshine")) @cascade {{
            items.used @filter(eq(item_name, "{item_name}"))
        }}
            
        result(func: uid(items), orderdesc: timestamp) @normalize {{
            demand_slopes @filter(eq(index_price, {price})) {{
                slope: slope
                uid: uid
            }}
        }}
    }}
    """

def getPreviousSupplySlope(item_name, price):
    return f"""
    {{
            items as var(func: eq(algorithm_tag, "Sunshine")) @cascade {{
            items.used @filter(eq(item_name, "{item_name}"))
        }}
            
        result(func: uid(items), orderdesc: timestamp) @normalize {{
            supply_slopes @filter(eq(index_price, {price})) {{
                slope: slope
                uid: uid
            }}
        }}
    }}
    """