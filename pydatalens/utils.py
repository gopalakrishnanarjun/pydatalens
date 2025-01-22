def save_plot(filename):
    """
    Utility function to save a plot to a file.
    """
    import matplotlib.pyplot as plt
    plt.savefig(filename)
    print(f"Plot saved as {filename}.")
