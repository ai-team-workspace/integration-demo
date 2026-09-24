"""Small synthetic shopping-cart fixture for the Team Workspace demonstration."""


def summarize_cart(prices):
    if not prices:
        return {'item_count': 0, 'total': 0, 'average_price': 0}

    if any(price < 0 for price in prices):
        raise ValueError

    total = sum(prices)
    return {
        'item_count': len(prices),
        'total': round(total, 2),
        'average_price': round(total / len(prices), 2),
    }
  
