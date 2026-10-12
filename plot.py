import matplotlib.pyplot as pyplot
import matplotlib.ticker as ticker
import numpy
from scipy.stats import norm

def plot_line_graph(title, dataframe, line1, line2=None, line3=None, xlabel=None, ylabel=None, log=False):
    #to clarify, line1 simply is the heading of a column in dataframe

    pyplot.style.use('seaborn-v0_8-whitegrid')

    pyplot.figure(figsize=(14, 7), dpi=100)
    pyplot.plot(dataframe.index, dataframe[line1], label=line1, color='#2980b9', linewidth=1.0, alpha=0.6)
    if line2: pyplot.plot(dataframe.index, dataframe[line2], label=line2, color='#e67e22', linewidth=1.8)
    if line3: pyplot.plot(dataframe.index, dataframe[line3], label=line3, color='#27ae60', linewidth=1.8)

    pyplot.title(title, fontsize=16, fontweight='bold', pad=15)
    if xlabel: pyplot.xlabel(xlabel, fontsize=12, labelpad=10)
    if ylabel: pyplot.ylabel(ylabel, fontsize=12, labelpad=10)

    if log: 
        pyplot.yscale("log")
        ax = pyplot.gca()
        ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('${x:g}'))

    pyplot.grid(True, which='major', linestyle='-', linewidth=0.7, alpha=0.7)
    pyplot.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.4)
    
    pyplot.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11)
    pyplot.tight_layout()
    pyplot.show()

def plot_histogram(title, dataframe, column, bins=100, normal_curve=True, xlabel=None, ylabel=None, log=False, density=False):

    pyplot.style.use('seaborn-v0_8-whitegrid')

    pyplot.figure(figsize=(14, 7), dpi=100)
    counts, edges, _ = pyplot.hist(dataframe[column], bins=bins, density=density, label=column, color='#2980b9', alpha=0.6, edgecolor='white', linewidth=0.3)

    if normal_curve:
        bin_width = edges[1] - edges[0]
        x = numpy.linspace(dataframe[column].min(), dataframe[column].max(), 500)
        scale = 1 if density else len(dataframe[column]) * bin_width
        pyplot.plot(x, norm.pdf(x, dataframe[column].mean(), dataframe[column].std()) * scale, label='Normal distribution', color='#e67e22', linewidth=1.8)

    pyplot.title(title, fontsize=16, fontweight='bold', pad=15)
    if xlabel: pyplot.xlabel(xlabel, fontsize=12, labelpad=10)
    pyplot.ylabel(ylabel or ("Density" if density else "Frequency"), fontsize=12, labelpad=10)

    if log:
        pyplot.yscale("log")
        lower_limit = counts.max() * 0.01 if density else 0.7
        pyplot.ylim(lower_limit, counts.max() * 1.2)

    pyplot.grid(True, which='major', linestyle='-', linewidth=0.7, alpha=0.7)
    pyplot.grid(True, which='minor', linestyle=':', linewidth=0.4, alpha=0.4)

    pyplot.legend(frameon=True, facecolor='white', framealpha=0.9, fontsize=11)
    pyplot.tight_layout()
    pyplot.show()
