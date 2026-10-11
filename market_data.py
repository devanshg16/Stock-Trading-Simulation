import yfinance as yf

def load_data(stockname, start, end):
    return yf.Ticker(stockname).history(start=start, end=end)
