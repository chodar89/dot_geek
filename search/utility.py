"""
Utility functions for search views
"""

def _get_price(price_range):
    if price_range == "0-10":
        gte = 0
        lte = 10
    if price_range == "10-20":
        gte = 10
        lte = 20
    if price_range == "20-30":
        gte = 20
        lte = 30
    if price_range == "30-40":
        gte = 30
        lte = 40
    if price_range == "40-50":
        gte = 40
        lte = 50
    if price_range == "50+":
        gte = 50
        lte = 0
    return (gte, lte)
