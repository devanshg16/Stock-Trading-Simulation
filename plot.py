import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def plot_line_graph(title, dataframe, line1, line2=None, line3=None, xlabel=None, ylabel=None, log=False):
    #to clarify, line1 simply is the heading of a column in dataframe

    plt.style.use('seaborn-v0_8-whitegrid')

    plt.figure(figsize=(14, 7), dpi=100)
    plt.plot(dataframe.index, dataframe[line1], label=line1, color='#2980b9', linewidth=1.0, alpha=0.6)
    if line2: plt.plot(dataframe.index, dataframe[line2], label=line2, color='#e67e22', linewidth=1.8)
    if line3: plt.plot(dataframe.index, dataframe[line3], label=line3, color='#27ae60', linewidth=1.8)

    plt.title(title, fontsize=16, fontweight='bold', pad=15)
    if xlabel: plt.xlabel(xlabel, fontsize=12, labelpad=10)
    if ylabel: plt.ylabel(ylabel, fontsize=12, labelpad=10)

    if log: 
        plt.yscale("log")
        ax = plt.gca()
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:g}'))

    plt.legend()
    plt.grid(True, which='major', linestyle='-', linewidth=0.7, alpha=0.7)
    plt.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.4)
    
    plt.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11)
    plt.tight_layout()
    plt.show()
