def max_profit(prices):
  min_price = float("inf")
  max_profit = 0

for price in prices:
  min_price = min(min_price, price)
  max_price = max(max_price, price - min_price)

return max_profit

prices = list(map(int, input("Enter stock prices: ").split()))

print("Maximuum profit:", max_profit(prices))