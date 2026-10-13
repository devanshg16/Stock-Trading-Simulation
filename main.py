import plot
from market_data import StockData
    
sma_windows = [2, 5, 10, 20, 50, 100, 150, 200]

apple = StockData("AAPL", "2000-01-01", "2020-01-01")  # end is non-inclusive, so last date is 2019-12-31
apple.add_multiple_smas(sma_windows)
apple.add_log_returns()
apple.add_returns()

print(apple.data)

plot.plot_line_graph("Apple Stock", apple.data, line1="Close", line2=apple.get_sma(20), line3=apple.get_sma(50), 
                     xlabel="Year", ylabel="Price (USD)", log=False)
plot.plot_line_graph("Apple Stock (log scale)", apple.data, line1="Close", line2=apple.get_sma(20), line3=apple.get_sma(50), 
                     xlabel="Year", ylabel="Price (USD)", log=True)

print(f"Total return: {apple.total_return() * 100:.4f}%")

plot.plot_histogram(f"{apple.ticker} Daily Log Returns", apple.data, "LogReturns", 
                    xlabel="Daily log return", density=True)
plot.plot_histogram(f"{apple.ticker} Daily Log Returns (log scale)", apple.data, "LogReturns", 
                    xlabel="Daily log return", log=True, density=True)
