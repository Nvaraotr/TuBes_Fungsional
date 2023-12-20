# --------------------------------------------------------------------------------------------------
# generate clipping and windowing
# --------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

hor_line = None
ver_line = None


def plot_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Plotting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished plotting {func.__name__}.")
        return result
    return wrapper


@plot_decorator
def clip_line(event):
    global hor_line, ver_line
    # Get the mouse click coordinates
    x, y = event.xdata, event.ydata

    # Update the clipping rectangle coordinates
    clip_x2, clip_y2 = x, y

    # Print the coordinates
    print(f"Clicked at ({x:.2f}, {y:.2f})")

    # Create a new grid based on the clipping rectangle
    # Adjust the grid size here
    new_grid_x = np.linspace(clip_x1, clip_x2, num=5)
    # Adjust the grid size here
    new_grid_y = np.linspace(clip_y1, clip_y2, num=5)

    if hor_line:
        hor_line.remove()
    if ver_line:
        ver_line.remove()

    hor_line = ax.axhline(y=y, color='r', linestyle='--')
    ver_line = ax.axvline(x=x, color='g', linestyle='--')

    plt.draw()

    # Create a new figure and axes for the grid plot
    fig2, ax2 = plt.subplots()

    # Plot the grid lines
    for gx in new_grid_x:
        ax2.axvline(x=gx, color='grey', linestyle='--')
    for gy in new_grid_y:
        ax2.axhline(y=gy, color='grey', linestyle='--')

    # Plot the original line
    ax2.plot(line_x, line_y, 'b-')

    # Set the plot limits
    ax2.set_xlim(clip_x1, clip_x2)
    ax2.set_ylim(clip_y1, clip_y2)
    plt.show()


# Create a figure and axes
fig, ax = plt.subplots()

# Initialize the clipping rectangle coordinates
clip_x1, clip_y1 = 0, 0
clip_x2, clip_y2 = 0, 0

# Define the line vertices
vertices = [(0, 0), (2.5, 2.5)]

# Extract x and y coordinates from the vertices
line_x, line_y = zip(*vertices)

# Plot the original line
ax.plot(line_x, line_y, 'k-')

# Set plot limits
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)

# Connect the mouse click event to the clipping function
plt.connect('button_press_event', clip_line)

# Show the plot
plt.show()
