def max_profit_brute_force(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            # print(prices[j], prices[i])
            profit = prices[j] - prices[i]
            # print(profit)
            max_profit = max(max_profit, profit)


def max_profit(prices):
    max_p = 0
    min_purchase = prices[0]
    for i in range(1, len(prices)):
        max_p = max(max_p, prices[i] - min_purchase)
        min_purchase = min(min_purchase, prices[i])
    return max_p


def max_profit_another_approach(prices):
    max_profit = 0
    cur_profit = 0
    for i in range(len(prices) - 1):
        cur_profit += prices[i + 1] - prices[i]
        if cur_profit < 0:
            cur_profit = 0
        max_profit = max(max_profit, cur_profit)
    return max_profit


def max_profit_another_approach_left_right(prices):
    left = 0
    right = 0
    max_profit = 0
    while right < len(prices):
        current_profit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(max_profit, current_profit)
        else:
            left = right
        right = right + 1
    return max_profit


prices = [7, 1, 5, 3, 6, 4]
