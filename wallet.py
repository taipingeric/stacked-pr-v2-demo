def pay(coins, price):
    if price > coins:  # 錢不夠
        return coins   # 不扣錢
    return coins - price
