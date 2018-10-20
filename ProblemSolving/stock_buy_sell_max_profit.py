'''Python program to maximize the profit by doing at most k transactions given stock prices for n days'''

# Function to get maximum profit by buying & selling a share atmost k times for the given stock prices of n days.

def get_max_profit(stock_prices, n, k):

    # Bottom-up DP approach
    profit = [[0 for i in range(k + 1)]
              for j in range(n)]

    # Profit is zero for the first day and for zero transactions
    for i in range(1, n):

        for j in range(1, k + 1):
            max_so_far = 0

            for l in range(i):
                max_so_far = max(max_so_far, stock_prices[i] -
                                 stock_prices[l] + profit[l][j - 1])

            profit[i][j] = max(profit[i - 1][j], max_so_far)

    return profit[n - 1][k]

# Driver code
k = 2  # Number of max transation allowed
stock_prices = [10, 7, 5, 8, 11, 9]
n = len(stock_prices)

print('Maximum profit is:')
print(get_max_profit(stock_prices, n, k))

'''Output:
        6
'''
