import plot
import market_data

spread1 = 20
spread2 = 50
spread1str = f"SMA-{spread1}"
spread2str = f"SMA-{spread2}"

apple = "AAPL"
startdate = "2000-01-01"
enddate = "2020-01-01" # end is non-inclusive so the last date fetched is 2019-12-31
data = market_data.load_data(apple, startdate, enddate)

market_data.add_sma(data, "Close", spread1str, spread1)
market_data.add_sma(data, "Close", spread2str, spread2)
market_data.add_log_returns(data, "Close", "LogReturns")

print(data)
# log       plot.plot_line_graph("Apple Stock", data, line1="Close", line2=spread1str, line3=spread2str, xlabel="Year", ylabel="Price (USD)", log=True)
# non-log   plot.plot_line_graph("Apple Stock", data, line1="Close", line2=spread1str, line3=spread2str, xlabel="Year", ylabel="Price (USD)", log=False)
