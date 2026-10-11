import plot
import market_data

apple = "AAPL"
startdate = "2000-01-01"
enddate = "2020-01-01" # end is non-inclusive so the last date fetched is 2019-12-31
data = market_data.load_data(apple, startdate, enddate)
market_data.add_sma(data, "Close", "SMA-20", 20)
market_data.add_sma(data, "Close", "SMA-50", 50)

plot.plot_line_graph("Apple Stock", data, line1="Close", line2="SMA-20", line3="MA-50", xlabel="Year", ylabel="Price (USD)", log=True)
plot.plot_line_graph("Apple Stock", data, line1="Close", line2="SMA-20", line3="MA-50", xlabel="Year", ylabel="Price (USD)", log=False)
