import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse


def print_message_decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator: Before function execution")
        result = func(*args, **kwargs)
        print("Decorator: After function execution")
        return result
    return wrapper


@print_message_decorator
def generate_points():
    for _ in range(2):
        point = input("Enter a point (x, y): ")
        yield tuple(map(float, point.split(",")))


def draw_ellipse(points):
    # Extract the coordinates of the two points
    start_x, start_y = next(points)
    end_x, end_y = next(points)

    # Calculate the center coordinates and ellipse dimensions
    center_x = (start_x + end_x) / 2
    center_y = (start_y + end_y) / 2
    width = abs(end_x - start_x)
    height = abs(end_y - start_y)

    # Create the ellipse patch
    ellipse = Ellipse((center_x, center_y), width, height,
                      fill=True, edgecolor='black')

    # Create the plot and add the ellipse patch
    fig, ax = plt.subplots()
    ax.add_patch(ellipse)

    # Draw the focal lines and center point
    ax.axvline(center_x, linestyle='--', color='lightgreen')
    ax.axhline(center_y, linestyle='--', color='lightgreen')
    ax.plot(center_x, center_y, 'ro')

    # Set plot limits and grid
    ax.set_aspect('equal')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.grid(True, linestyle='--')

    # Print ellipse coordinates
    print("Ellipse Coordinates:")
    print(f"Point 1: ({round(start_x)}, {round(start_y)})")
    print(f"Point 2: ({round(end_x)}, {round(end_y)})")
    print(f"Center: ({round(center_x)}, {round(center_y)})")
    print(f"Width: {round(width)}")
    print(f"Height: {round(height)}")

    # Show the plot
    plt.show()


def higher_order_function(generator_function, drawing_function):
    points_generator = generator_function()
    drawing_function(points_generator)


if __name__ == '__main__':
    # Create a generator for points
    higher_order_function(generate_points, draw_ellipse)
