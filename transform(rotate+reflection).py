# --------------------------------------------------------------------------------------------------
# transform (rotate + reflection)
# --------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


def plot_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Plotting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished plotting {func.__name__}.")
        return result
    return wrapper


def draw_line(start_pos, end_pos):
    plt.plot([start_pos[0], end_pos[0]], [
             start_pos[1], end_pos[1]], color='blue')


@plot_decorator
def reflect_line(start_pos, end_pos, x):
    reflected_start_x = 2 * x - start_pos[0]
    reflected_end_x = 2 * x - end_pos[0]
    reflected_start_pos = (reflected_start_x, start_pos[1])
    reflected_end_pos = (reflected_end_x, end_pos[1])
    plt.plot([reflected_start_pos[0], reflected_end_pos[0]], [
             reflected_start_pos[1], reflected_end_pos[1]], color='red')


def rotate_line(start_pos, end_pos, angle):
    # Calculate midpoint
    midpoint = ((start_pos[0] + end_pos[0]) / 2,
                (start_pos[1] + end_pos[1]) / 2)

    # Translate the line to the origin
    translated_start_pos = (
        start_pos[0] - midpoint[0], start_pos[1] - midpoint[1])
    translated_end_pos = (end_pos[0] - midpoint[0], end_pos[1] - midpoint[1])

    # Apply rotation
    rotation_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
    rotated_start_pos = np.dot(rotation_matrix, translated_start_pos)
    rotated_end_pos = np.dot(rotation_matrix, translated_end_pos)

    # Translate back to the original position
    rotated_start_pos = (
        rotated_start_pos[0] + midpoint[0], rotated_start_pos[1] + midpoint[1])
    rotated_end_pos = (
        rotated_end_pos[0] + midpoint[0], rotated_end_pos[1] + midpoint[1])

    # Return the rotated positions
    return rotated_start_pos, rotated_end_pos


# Variables to store line coordinates
start_pos = None
end_pos = None


def onclick(event):
    global start_pos, end_pos
    if start_pos is None:
        start_pos = (event.xdata, event.ydata)
    elif end_pos is None:
        end_pos = (event.xdata, event.ydata)

        # Clear the plot
        plt.clf()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')

        # Draw the line
        draw_line(start_pos, end_pos)

        # Reflect the line
        x = event.xdata
        reflect_line(start_pos, end_pos, x)

        # Rotate the line
        # Example rotation angle of 45 degrees (pi/4 radians)
        angle = np.pi / 4
        rotated_start_pos, rotated_end_pos = rotate_line(
            start_pos, end_pos, angle)

        # Draw the rotated line
        plt.plot([rotated_start_pos[0], rotated_end_pos[0]], [
                 rotated_start_pos[1], rotated_end_pos[1]], color='green')

        # Print the line coordinates
        print("Line Coordinates:")
        print("Start Pos:", start_pos)
        print("End Pos:", end_pos)

        # Calculate the reflected coordinates
        reflected_start_x = 2 * x - start_pos[0]
        reflected_end_x = 2 * x - end_pos[0]
        reflected_start_pos = (reflected_start_x, start_pos[1])
        reflected_end_pos = (reflected_end_x, end_pos[1])

        # Print the transformed coordinates
        print("\nReflected Line Coordinates:")
        print("Reflected Start Pos:", reflected_start_pos)
        print("Reflected End Pos:", reflected_end_pos)

        # Print the rotated coordinates
        print("Rotated Line Coordinates:")
        print("Rotated Start Pos:", rotated_start_pos)
        print("Rotated End Pos:", rotated_end_pos)
        print()

        # Reset the coordinates
        start_pos = None
        end_pos = None

        # Set the aspect ratio to equal
        ax.set_aspect('equal')

        # Show the updated plot
        plt.draw()


# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Connect the mouse click event to the onclick function
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
