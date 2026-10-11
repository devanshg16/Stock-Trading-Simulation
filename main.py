import plot
import market_data

def add_moving_average(data , refcolumn, newcolumn, spread):
    data[newcolumn] = data[refcolumn].rolling(window=spread).mean()
    # this is possible since data is a dataframe type
    # dataframe types are always passed by reference, so a new item is not created

apple = "AAPL"
startdate = "2000-01-01"
enddate = "2020-01-01" # end is non-inclusive so the last date fetched is 2019-12-31
data = market_data.load_data(apple, startdate, enddate)
add_moving_average(data, "Close", "MA-20", 20)
add_moving_average(data, "Close", "MA-50", 50)

plot.plot_line_graph("Apple Stock", data, line1="Close", line2="MA-20", line3="MA-50", xlabel="Year", ylabel="Price (USD)", log=True)
plot.plot_line_graph("Apple Stock", data, line1="Close", line2="MA-20", line3="MA-50", xlabel="Year", ylabel="Price (USD)", log=False)
