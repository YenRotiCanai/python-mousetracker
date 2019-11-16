from pynput.mouse import Listener
import logging

# logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")
logging.basicConfig(filename="mouse_log.csv", level=logging.DEBUG, format="%(asctime)s,%(message)s")

def on_move(x, y):
    # logging.info("Mouse moved to ({0}, {1})".format(x, y))
    logging.info("Move,{0},{1}".format(x, y))

# def on_click(x, y, button, pressed):
#     if pressed:
#         logging.info("Mouse clicked at ({0}, {1}) with {2}".format(x, y, button))

def on_scroll(x, y, dx, dy):
    # logging.info("Mouse scrolled at ({0}, {1})({2})".format(x, y, dy))
    print("Mouse scrolled at ({0}, {1})({2})".format(x, y, dy))
    # logging.info('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
    logging.info("Scroll,{0},{1},{2}".format(x, y, dy))

# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()

with Listener(on_move=on_move, on_scroll=on_scroll) as listener:
    listener.join()
