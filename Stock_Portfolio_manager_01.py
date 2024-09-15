import yfinance as yf
import csv
import matplotlib.pyplot as plt

# Load portfolio from CSV
def load_portfolio(filename):
    portfolio = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['quantity'] = int(row['quantity'])
                row['purchase_price'] = float(row['purchase_price'])
                portfolio.append(row)
    except FileNotFoundError:
        print("No portfolio found, starting with an empty portfolio.")
    return portfolio

# Save portfolio to CSV
def save_portfolio(portfolio, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ticker', 'quantity', 'purchase_price'])
        writer.writeheader()
        writer.writerows(portfolio)
    print(f"Portfolio saved to {filename}")

# Add a stock to the portfolio
def add_stock(portfolio, ticker, quantity, purchase_price):
    stock = {
        'ticker': ticker,
        'quantity': quantity,
        'purchase_price': purchase_price
    }
    portfolio.append(stock)

# Fetch real-time stock prices
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return price

# Calculate total value of the portfolio
def calculate_portfolio_value(portfolio):
    total_value = 0
    total_invested = 0
    for stock in portfolio:
        current_price = get_stock_price(stock['ticker'])
        stock_value = current_price * stock['quantity']
        total_value += stock_value
        total_invested += stock['purchase_price'] * stock['quantity']
        print(f"{stock['ticker']}: Current Price = {current_price}, Value = {stock_value}")
    profit_loss = total_value - total_invested
    print(f"\nTotal Portfolio Value: {total_value}")
    print(f"Profit/Loss: {profit_loss}")
    return total_value, profit_loss

# Visualize portfolio composition
def visualize_portfolio(portfolio):
    labels = [stock['ticker'] for stock in portfolio]
    sizes = [get_stock_price(stock['ticker']) * stock['quantity'] for stock in portfolio]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Portfolio Composition")
    plt.show()

def main():
    filename = "portfolio.csv"
    portfolio = load_portfolio(filename)

    while True:
        print("\nStock Portfolio Manager")
        print("1. Add a stock")
        print("2. View portfolio value")
        print("3. Visualize portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            add_stock(portfolio, ticker, quantity, purchase_price)
            save_portfolio(portfolio, filename)
        elif choice == "2":
            calculate_portfolio_value(portfolio)
        elif choice == "3":
            visualize_portfolio(portfolio)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
