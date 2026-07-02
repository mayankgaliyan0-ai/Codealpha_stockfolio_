stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 400
}

my_portfolio = {}

print("====== STOCK PORTFOLIO TRACKER ======")
print("Available Stocks:")
print("AAPL  TSLA  MSFT")

while True:

    stock = input("\nEnter Stock Name (type stop to finish): ").upper()

    if stock == "STOP":
        break

    if stock in stocks:

        quantity = int(input("Enter Quantity: "))
        my_portfolio[stock] = quantity

    else:
        print("Stock is not available.")

total = 0

file = open("portfolio_report.txt", "w")

print("\n------ REPORT ------")
file.write("STOCK REPORT\n\n")

for item in my_portfolio:

    amount = stocks[item] * my_portfolio[item]

    total += amount

    text = item + " = " + str(my_portfolio[item]) + " Shares = $" + str(amount)

    print(text)
    file.write(text + "\n")

print("\nTotal Value = $", total)
file.write("\nTotal Portfolio Value = $" + str(total))

file.close()

print("\nReport Saved Successfully.")