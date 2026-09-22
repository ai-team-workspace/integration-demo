"""Small synthetic shopping-cart fixture for the Team Workspace demonstration."""


def summarize_cart(prices):
      total = sum(prices)
      return {
          'item_count': len(prices),
          'total': round(total, 2),
          'average_price': round(total / len(prices), 2),
      }
  
