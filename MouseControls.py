import pyautogui as gui


class MouseController:
    def __init__(self, width, height):
        self.screen_width = gui.size()[0]
        self.screen_height = gui.size()[1]
        self.window_width = width
        self.window_height = height
        self.start_x = (width*5)/100
        self.start_y = (height*5)/100
        self.end_x = width - self.start_x
        self.end_y = height - self.start_y
        self.controlling = False
        self.curr_x = gui.position()[0]
        self.curr_y = gui.position()[1]
        print("Mouse is at "+str(gui.position()))

    def left_click(self):
        # print("Clicked Left!")
        gui.leftClick(self.curr_x,self.curr_y)

    def right_click(self):
        # print("Clicked Right")
        gui.rightClick(self.curr_x,self.curr_y)

    def double_click(self):
        # print("Did a double click")
        gui.doubleClick(self.curr_x,self.curr_y)

    def set_position(self, index_position, fps):
        if self.controlling is False:
            return
        print("setting initial position")
        self.curr_x = index_position[0]*(self.screen_width)
        self.curr_y = index_position[1]*(self.screen_height)
        print(" currx = "+str(self.curr_x))
        print(" curry = "+str(self.curr_y))
        gui.moveTo(self.curr_x, self.curr_y, duration=1/fps)

    def set_position(self, index_position,):
        if self.controlling is False:
            return
        print("setting initial position")
        self.curr_x = index_position[0]*(self.screen_width)
        self.curr_y = index_position[1]*(self.screen_height)
        print(" currx = "+str(self.curr_x))
        print(" curry = "+str(self.curr_y))
        gui.moveTo(self.curr_x, self.curr_y, duration=1/13)
