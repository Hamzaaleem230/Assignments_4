#          ** 02_lists **

# 03_erase_canvas

from graphics import Canvas # type: ignore
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()

    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    for obj in overlapping_objects:
        canvas.set_color(obj, "white")

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw grid of blue cells
    for x in range(0, CANVAS_WIDTH, CELL_SIZE):
        for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
            canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, "blue")

    # Eraser loop
    while True:
        erase_objects(canvas, None)
        canvas.root.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
