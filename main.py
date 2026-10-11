import yfinance as yf

def load_data(stock, start, end):
    return stock.history(start=start, end=end)

stock = yf.Ticker("AAPL")
startdate = "2000-01-01"
enddate = "2020-01-01"
data = load_data(stock, startdate, enddate)
