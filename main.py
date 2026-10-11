import yfinance as yf
import plot

def load_data(stockname, start, end):
    return yf.Ticker(stockname).history(start=start, end=end)

def add_moving_average(data , refcolumn, newcolumn, spread):
    data[newcolumn] = data[refcolumn].rolling(window=spread).mean()
    # this is possible since data is a dataframe type
    # dataframe types are always passed by value

apple = "AAPL"
startdate = "2000-01-01"
enddate = "2020-01-01"
data = load_data(apple, startdate, enddate)
add_moving_average(data, "Close", "MA-20", 20)
add_moving_average(data, "Close", "MA-50", 50)

plot.plot_data("Apple Stock", data, line1="Close", line2="MA-20", line3="MA-50", xlabel="Year", ylabel="Price (USD)")
