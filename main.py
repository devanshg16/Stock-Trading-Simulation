import plot
from market_data import StockData
    
sma_windows = [2, 5, 10, 20, 50, 100, 150, 200]

apple = StockData("AAPL", "2000-01-01", "2020-01-01")  # end is non-inclusive, so last date is 2019-12-31
apple.add_multiple_smas(sma_windows)
apple.add_log_returns()

print(apple.data)

# plot.plot_line_graph("Apple Stock", apple.data, line1="Close", line2=apple.get_sma(20), line3=apple.get_sma(50), 
#                      xlabel="Year", ylabel="Price (USD)", log=False)
# plot.plot_line_graph("Apple Stock (log scale)", apple.data, line1="Close", line2=apple.get_sma(20), line3=apple.get_sma(50), 
#                      xlabel="Year", ylabel="Price (USD)", log=True)

print(f"Total return: {apple.total_return() * 100:.4f}%")

print(f"Mean daily log return: {apple.data['LogReturns'].mean():.4f}")
print(f"Standard deviation of daily log returns: {apple.data['LogReturns'].std():.4f}")
print(f"Annualised mean: {apple.data['LogReturns'].mean()*252:.2%}")
print(f"Annualised volatility: {apple.data['LogReturns'].std()*252**0.5:.2%}")
print(f"Skewness: {apple.data['LogReturns'].skew():.4f}")
print(f"Excess Kurtosis: {apple.data['LogReturns'].kurtosis():.4f}")

#skewness and kurtosis excluding outlier September 29, 2000:
print(f"Skewness (excluding outlier September 29, 2000): {apple.data['LogReturns'].drop(apple.data.index[apple.data.index.get_loc('2000-09-29')]).skew():.4f}")
print(f"Excess Kurtosis (excluding outlier September 29, 2000): {apple.data['LogReturns'].drop(apple.data.index[apple.data.index.get_loc('2000-09-29')]).kurtosis():.4f}")

# plot.plot_histogram(f"{apple.ticker} Daily Log Returns", apple.data, "LogReturns", 
#                     xlabel="Daily log return", density=True)
# plot.plot_histogram(f"{apple.ticker} Daily Log Returns (log scale)", apple.data, "LogReturns", 
#                     xlabel="Daily log return", log=True, density=True)

snp500 = StockData("^GSPC", "2000-01-01", "2020-01-01")
snp500.add_multiple_smas(sma_windows)
snp500.add_log_returns()

plot.plot_line_graph("S&P 500", snp500.data, line1="Close", line2=snp500.get_sma(20), line3=snp500.get_sma(50), 
                     xlabel="Year", ylabel="Price (USD)", log=False)
plot.plot_line_graph("S&P 500 (log scale)", snp500.data, line1="Close", line2=snp500.get_sma(20), line3=snp500.get_sma(50), 
                     xlabel="Year", ylabel="Price (USD)", log=True)
