import pyglet
from window import Window
from settings import Settings


def main():
    window = Window(
        width=800, height=600,
        caption='AstroCraft', resizable=True)
    # Hide the mouse cursor and prevent the mouse from leaving the window.
    window.set_exclusive_mouse(True)
    Settings.setup()
    pyglet.app.run()


if __name__ == '__main__':
    main()
