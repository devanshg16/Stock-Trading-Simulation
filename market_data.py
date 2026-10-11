import yfinance as yf
import numpy as np

def load_data(stockname, start, end):
    return yf.Ticker(stockname).history(start=start, end=end)

def add_sma(data, refcolumn, newcolumn, spread): #sma stands for simple moving average
    data[newcolumn] = data[refcolumn].rolling(window=spread).mean()
    # this is possible since data is a dataframe type
    # dataframe types are always passed by reference, so a new item is not created

def add_log_returns(data, refcolumn, newcolumn):
    data[newcolumn] = np.log(data[refcolumn] / data[refcolumn].shift(1))

def add_returns(data, refcolumn, newcolumn):
    data[newcolumn] = (data[refcolumn] / data[refcolumn].shift(1))
