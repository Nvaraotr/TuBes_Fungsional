import matplotlib.pyplot as plt
import math


def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1
    err = dx - dy

    turns = []
    while x0 != x1 or y0 != y1:
        turns.append((x0, y0))
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return turns


def plot_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Plotting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished plotting {func.__name__}.")
        return result
    return wrapper


@plot_decorator
def plot_line(turns):
    x_values = []
    y_values = []

    fig, ax = plt.subplots()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("Bresenham Line Algorithm")
    ax.grid(True)

    for turn in turns:
        x_values.append(turn[0])
        y_values.append(turn[1])
        ax.plot(turn[0], turn[1], 'go')

    ax.plot(x_values, y_values, 'b-')
    plt.xlim(min(x_values) - 1, max(x_values) + 1)
    plt.ylim(min(y_values) - 1, max(y_values) + 1)
    plt.show()


def plot_using_hof(bresenham_func, x0, y0, x1, y1, plot_func):
    turns = bresenham_func(x0, y0, x1, y1)
    plot_func(turns)


if __name__ == "__main__":
    x0 = int(input("Enter x0: "))
    y0 = int(input("Enter y0: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))

    turns = bresenham_line(x0, y0, x1, y1)
    plot_line(turns)

    plot_using_hof(bresenham_line, x0, y0, x1, y1, plot_line)
