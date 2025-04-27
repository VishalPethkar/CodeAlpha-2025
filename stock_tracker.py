# Simple offline stock tracker with fake prices

# Predefined fake stock prices
fake_prices = {
    "AAPL": 170.00,
    "GOOGL": 2800.00,
    "MSFT": 310.00,
    "TSLA": 750.00,
    "AMZN": 3400.00
}

# Portfolio dictionary
portfolio = {}

# Add stock
def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    shares = int(input("Enter number of shares: "))
    if symbol in fake_prices:
        portfolio[symbol] = portfolio.get(symbol, 0) + shares
        print(f"Added {shares} shares of {symbol}.\n")
    else:
        print(f"Sorry, we don't have price data for {symbol}.\n")

# Remove stock
def remove_stock():
    symbol = input("Enter stock symbol to remove: ").upper()
    if symbol in portfolio:
        shares = int(input("Enter number of shares to remove: "))
        if shares >= portfolio[symbol]:
            del portfolio[symbol]
            print(f"Removed all shares of {symbol}.\n")
        else:
            portfolio[symbol] -= shares
            print(f"Removed {shares} shares of {symbol}.\n")
    else:
        print(f"{symbol} is not in your portfolio.\n")

# View portfolio
def view_portfolio():
    total_value = 0
    if not portfolio:
        print("\nYour portfolio is empty.\n")
        return
    
    print("\nYour Portfolio:")
    for symbol, shares in portfolio.items():
        price = fake_prices.get(symbol, 0)
        value = price * shares
        total_value += value
        print(f"{symbol}: {shares} shares x ${price:.2f} = ${value:.2f}")
    print(f"\nTotal Portfolio Value: ${total_value:.2f}\n")

# Main menu
while True:
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        add_stock()
    elif choice == "2":
        remove_stock()
    elif choice == "3":
        view_portfolio()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.\n")


#1. Add Stock
#2. Remove Stock
#3. View Portfolio
#4. Exit
#Choose an option (1-4): 1
#Enter stock symbol (e.g., AAPL): AAPL
#Enter number of shares: 10
#Added 10 shares of AAPL.