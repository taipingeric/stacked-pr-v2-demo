from wallet import pay

PRICE = {"potion": 50, "sword": 120}

def buy(coins, item):
    return pay(coins, PRICE[item])
