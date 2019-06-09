stock_prices = [10, 7, 5, 8, 11, 9]

def get_max_profit(stock_prices):
    max_profit = 0

    # Go through every price (with its index as the time)
    for earlier_time, earlier_price in enumerate(stock_prices):

        # And go through all the LATER prices
        for later_time in range(earlier_time + 1, len(stock_prices)):
            later_price = stock_prices[later_time]

            # See what our profit would be if we bought at the
            # earlier price and sold at the later price
            potential_profit = later_price - earlier_price

            # Update max_profit if we can do better
            max_profit = max(max_profit, potential_profit)

    return max_profit

print(get_max_profit(stock_prices))