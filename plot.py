import matplotlib.pyplot as plt

def plot_data(title, dataframe, line1, line2=None, line3=None, xlabel=None, ylabel=None):
    #to clarify, line1 simply is the heading of a column in dataframe
    plt.figure(figsize=(15, 8))
    plt.plot(dataframe.index, dataframe[line1], label=line1, color='dodgerblue', alpha=0.7)
    if line2: plt.plot(dataframe.index, dataframe[line2], label=line2, color='darkorange', alpha=0.7)
    if line3: plt.plot(dataframe.index, dataframe[line3], label=line3, color='forestgreen', alpha=0.7)

    plt.title(title, fontsize=14)
    if xlabel: plt.xlabel(xlabel, fontsize=12)
    if ylabel: plt.ylabel(ylabel, fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()
