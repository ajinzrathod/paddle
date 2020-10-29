from tkinter import Tk, Canvas
import random
from paddle import Paddle


class Ball:
    def __init__(self, myCanvas, color):
        self.canvas = myCanvas

        # Creating Oval
        self.id = myCanvas.create_oval(0, 0, 15, 15, fill=color)
        """ (15 - 0) = 15
        Thus, the height and width of ball will be 15, 15 respectively
        Half of ball width be 15 // 2 = 7
        Half of ball height be 15 // 2 = 7
        """

        self.y = -1

        tpl = (-2, -1, 0, 1, 2)
        self.x = random.choice(tpl)

        # Getting height and width of current window
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

        # Moving Ball to center
        self.canvas.move(self.id,
                         (self.canvas_width//2)-7, (self.canvas_height//2)-7)

    def draw(self, myPaddle):

        # Moving ball up
        self.canvas.move(self.id, self.x, self.y)

        # Getting current co ordinates of Ball
        ballPos = self.canvas.coords(self.id)  # -> [x1, y1, x2, y2]
        paddlePos = self.canvas.coords(myPaddle.id)

        # If Ball Reaches Extreme Left
        if ballPos[0] <= 0:
            self.x = abs(self.x)

        # If Ball Reaches Extreme Right
        elif ballPos[2] >= self.canvas_width:
            self.x = abs(self.x) * -1

        """In below line `else if` will not come.
        There is a possibility that ball reaches at extreme top and Left
        at same time"""
        # If Ball Reaches Extreme Top
        if ballPos[1] <= 0:
            self.y = 3

        # If Ball Touches Water
        elif ballPos[3] >= waterLevel:
            self.y = 0
            self.x = 0
            self.canvas.create_text(self.canvas_width // 2, 100, text="Game Over")
            return True

        # When Ball Touches Paddle
        if ballPos[2] >= paddlePos[0] and ballPos[0] <= paddlePos[2]:
            if ballPos[3] >= paddlePos[1] and ballPos[3] <= paddlePos[3]:
                self.y = -3
        return False

    # Forever Moving Ball
    def clock(self):
        losed = self.draw(myPaddle)

        root.update_idletasks()
        """Calls all pending idle tasks, without processing any other events.
        This can be used to carry out geometry management
        and redraw widgets if necessary,
        without calling any callbacks."""

        if not losed:
            root.after(10, self.clock)


if __name__ == '__main__':
    # Creating root
    root = Tk()

    # Creating tilte
    root.title("ajinzrathod")

    # Restricting to resize window in both X and Y direction
    root.resizable(False, False)

    # Bring our window in front of all windows
    root.wm_attributes("-topmost", 1)

    # Declaring Height and width of root canvas
    myCanvasW = 500
    myCanvasH = 500

    # Creating Canvas (bd is for border)
    myCanvas = Canvas(root, width=myCanvasW, height=myCanvasH,
                      bd=0, highlightthickness=0)

    # Packing canvas
    myCanvas.pack()

    # Updating
    root.update()

    # Creating Ball
    myBall = Ball(myCanvas, "#ff0000")
    myPaddle = Paddle(myCanvas, "#ffff00", 100, 20)

    # Creating Water
    waterLevel = myCanvasH - 20
    water = myCanvas.create_rectangle(1, waterLevel,
                                      myCanvasW - 1, myCanvasH - 1,
                                      fill="#1eafed")

    # Moving clock for first time
    myBall.clock()

    # Showing window till user does'nt close it
    root.mainloop()
