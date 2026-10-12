import yfinance as yf
import numpy as np

def load_data(stockname, start, end):
    return yf.Ticker(stockname).history(start=start, end=end)

def add_sma(data, refcolumn, newcolumn, window): #sma stands for simple moving average
    data[newcolumn] = data[refcolumn].rolling(window=window).mean()
    # this is possible since data is a dataframe type
    # dataframe types are always passed by reference, so a new item is not created

def add_log_returns(data, refcolumn, newcolumn):
    data[newcolumn] = np.log(data[refcolumn] / data[refcolumn].shift(1))

def add_returns(data, refcolumn, newcolumn):
    data[newcolumn] = (data[refcolumn] / data[refcolumn].shift(1))-1

class StockData:
    def __init__(self, ticker, startdate, enddate):
        self.ticker = ticker
        self.startdate = startdate
        self.enddate = enddate  # non-inclusive, so the last date fetched is the day before
        self.data = load_data(ticker, startdate, enddate)
        self.sma_cols = {}  # window -> column name, e.g. {20: "SMA-20"}
    
    def __repr__(self):
        return f"StockData({self.ticker!r}, {self.startdate!r}, {self.enddate!r})"

    def add_sma(self, window, refcolumn="Close"):
        name = f"SMA-{window}"
        add_sma(self.data, refcolumn, name, window)
        self.sma_cols[window] = name
        return name

    def add_multiple_smas(self, windows, refcolumn="Close"):
        return [self.add_sma(w, refcolumn) for w in windows]

    def get_sma(self, window):
        return self.sma_cols[window]
    
    def add_log_returns(self, refcolumn="Close", name="LogReturns"):
        add_log_returns(self.data, refcolumn, name)

    def add_returns(self, refcolumn="Close", name="Returns"):
        add_returns(self.data, refcolumn, name)

    def total_return(self, column="LogReturns"):
        return np.exp(self.data[column].dropna().sum()) - 1
