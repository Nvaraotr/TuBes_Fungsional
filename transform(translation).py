

# --------------------------------------------------------------------------------------------------
# transform (translation)
# --------------------------------------------------------------------------------------------------

import tkinter as tk

# Variables to store the coordinates and translation offset
coordinates = []
translation_offset = (0, 0)


def plot_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Plotting {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"Finished plotting {func.__name__}.")
        return result
    return wrapper


@plot_decorator
def handle_click(event):
    global translation_offset

    # Add clicked coordinates to the list
    coordinates.append((event.x, event.y))

    # Draw a line segment on the canvas
    if len(coordinates) >= 2:
        canvas.create_line(coordinates[-2], coordinates[-1])

        # Translate the line
        translated_coordinates = translate_line(
            coordinates[-2], coordinates[-1], translation_offset)

        # Draw the translated line
        canvas.create_line(
            translated_coordinates[0], translated_coordinates[1], fill='red')

        # Display the coordinates
        canvas.create_text(
            coordinates[-2], text=f"({coordinates[-2][0]}, {coordinates[-2][1]})", anchor=tk.SW)
        canvas.create_text(
            coordinates[-1], text=f"({coordinates[-1][0]}, {coordinates[-1][1]})", anchor=tk.SW)
        canvas.create_text(
            translated_coordinates[-2], text=f"({translated_coordinates[-2][0]}, {translated_coordinates[-2][1]})", anchor=tk.SW)
        canvas.create_text(
            translated_coordinates[-1], text=f"({translated_coordinates[-1][0]}, {translated_coordinates[-1][1]})", anchor=tk.SW)

        # Print the original and transformed coordinates in the console
        print("Original Coordinates:")
        print(f"Start: ({coordinates[-2][0]}, {coordinates[-2][1]})")
        print(f"End: ({coordinates[-1][0]}, {coordinates[-1][1]})")

        print("Transformed Coordinates:")
        print(
            f"Start: ({translated_coordinates[0][0]}, {translated_coordinates[0][1]})")
        print(
            f"End: ({translated_coordinates[1][0]}, {translated_coordinates[1][1]})")
        print()

        # Disable further clicks
        canvas.unbind("<Button-1>")

        # Hide the translation buttons
        translate_button1.pack_forget()
        translate_button2.pack_forget()
        translate_button3.pack_forget()
        translate_button4.pack_forget()

        bl = tk.Label(text="black: original line")
        rl = tk.Label(text="red: translated line")
        rl.config(foreground="red")
        rl.pack()
        bl.pack()

    # Translate a line segment by a given offset.


def translate_line(start_point, end_point, offset):

    start_x, start_y = start_point
    end_x, end_y = end_point
    offset_x, offset_y = offset
    translated_start_point = (start_x + offset_x, start_y + offset_y)
    translated_end_point = (end_x + offset_x, end_y + offset_y)
    return (translated_start_point, translated_end_point)


def translate(dx, dy):
    global translation_offset
    translation_offset = (dx, dy)

    # Print the translation in the console
    if dx == 0 and dy < 0:
        print("Translate Up")
    elif dx == 0 and dy > 0:
        print("Translate Down")
    elif dx < 0 and dy == 0:
        print("Translate Left")
    elif dx > 0 and dy == 0:
        print("Translate Right")


# Create the main window
window = tk.Tk()

# Create a canvas for drawing
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()


# Create translation buttons
translate_button1 = tk.Button(
    window, text="Translate Up", command=lambda: translate(0, -40))
translate_button1.pack()
translate_button2 = tk.Button(
    window, text="Translate Down", command=lambda: translate(0, 40))
translate_button2.pack()
translate_button3 = tk.Button(
    window, text="Translate Left", command=lambda: translate(-40, 0))
translate_button3.pack()
translate_button4 = tk.Button(
    window, text="Translate Right", command=lambda: translate(40, 0))
translate_button4.pack()


# Bind the click event to the canvas
canvas.bind("<Button-1>", handle_click)

# Start the main event loop
window.mainloop()
