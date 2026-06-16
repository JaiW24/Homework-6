from graphics import *


def buttonClicked(clickPoint, button):
    x = clickPoint.getX()
    y = clickPoint.getY()

    p1 = button.getP1()
    p2 = button.getP2()

    if p1.getX() <= x <= p2.getX() and p1.getY() <= y <= p2.getY():
        return True

    else:
        return False


def main():
    win = GraphWin("Button Test", 400, 300)

    button = Rectangle(Point(150, 120), Point(250, 180))
    button.draw(win)

    label = Text(Point(200, 150), "Button")
    label.draw(win)

    result = Text(Point(200, 250), "")
    result.draw(win)

    for i in range(10):
        click = win.getMouse()

        if buttonClicked(click, button):
            result.setText("Button clicked!")
        else:
            result.setText("Button NOT clicked!")

    win.close()


main()