"""Make specific plots."""
import matplotlib.pyplot as plt
import numpy as np


def plot_sensor(x, y):
    """Make a fancy plot for sensor values."""
    fig, ax = plt.subplots()
    ax.grid()

    # Make fiducial lines
    x_fiducial = np.arange(100)
    y_upper = 5 * x_fiducial
    y_lower = 2 * x_fiducial
    ax.plot(x_fiducial, y_upper, color='tab:red', linewidth=2)
    ax.plot(x_fiducial, y_lower, color='tab:blue', linewidth=2)
    ax.plot(x, y, color='#ED1C24')
    # Tuple of RGB (250, 125, 30)
    ax.set_xlabel('Seconds')
    ax.set_ylabel('Sensor Reading')
    return fig, ax
