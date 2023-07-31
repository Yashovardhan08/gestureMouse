class DetectClicks:
    def __init__(self, mouse_controller,lock):
        self.palm_vector = None
        self.index_vector = None
        self.middle_vector = None
        self.lock = lock
        self.landmarks_list = []
        self.mouse_controller = mouse_controller
        # self.right_click = False
        # self.left_click = False

    def push_landmark(self, lmk):
        self.landmarks_list.append(lmk)
        print("added landmark")

    def run_detections(self):
        print("STARTING THE THREAD")
        while True:
            # print("LANDMARK LIST LENGTH:"+str(len(self.landmarks_list)))
            if len(self.landmarks_list) > 0:
                self.lock.acquire()
                landmarks = self.landmarks_list.pop(0)
                self.lock.release()
                if len(landmarks) == 0:
                    self.mouse_controller.controlling = False
                    return
                if self.mouse_controller.controlling is False:
                    self.mouse_controller.controlling = True

                self.mouse_controller.set_position(landmarks[5])
                self.set_palm_direction(landmarks)
                self.set_index_direction(landmarks)
                self.set_middle_direction(landmarks)
                dot_product_index = self.index_vector[0] * self.palm_vector[0] + self.index_vector[1] * \
                                    self.palm_vector[1]
                dot_product_middle = self.middle_vector[0] * self.palm_vector[0] + self.middle_vector[1] * \
                                     self.palm_vector[1]

                if dot_product_middle <= 0 and dot_product_index <= 0:# double click
                    print("clicked : Double")
                    self.mouse_controller.double_click()
                elif dot_product_middle <= 0 and dot_product_index > 0 :# right click
                    print("clicked : right")
                    self.mouse_controller.right_click()
                elif dot_product_index <= 0 and dot_product_middle > 0 :# left click
                    print("clicked : left")
                    self.mouse_controller.left_click()

        print("THREAD DIED")


    def set_palm_direction(self, lmks):
        pos0 = lmks[0] * 1000
        pos5 = lmks[5] * 1000
        self.palm_vector = (pos5[0] - pos0[0], pos5[1] - pos0[1])

    def set_index_direction(self, lmks):
        pos7 = lmks[7] * 1000
        pos8 = lmks[8] * 1000
        self.index_vector = (pos8[0] - pos7[0], pos8[1] - pos7[1])

    def set_middle_direction(self,lmks):
        pos11 = lmks[11] * 1000
        pos10 = lmks[10] * 1000
        self.middle_vector = (pos11[0] - pos10[0], pos11[1] - pos10[1])


    # def update(self, landmarks, mouse_controller, fps):
    #     self.landmarks = landmarks
    #     if len(landmarks) == 0:
    #         mouse_controller.controlling = False
    #         return
    #     if mouse_controller.controlling is False:
    #         mouse_controller.controlling = True
    #
    #     mouse_controller.set_position(landmarks[5], fps)
    #     self.set_palm_direction()
    #     self.set_index_direction()
    #     self.set_middle_direction()
    #     dot_product_index = self.index_vector[0]*self.palm_vector[0]+self.index_vector[1]*self.palm_vector[1]
    #     dot_product_middle = self.middle_vector[0]*self.palm_vector[0]+self.middle_vector[1]*self.palm_vector[1]
    #
    #     click_return = ""
    #     if dot_product_middle <= 0 and dot_product_index <= 0 and ((self.left_click and self.right_click) is False):
    #         # double click
    #         self.right_click = True
    #         self.left_click = True
    #         click_return = "double"
    #         print("clicked : Double")
    #         mouse_controller.double_click()
    #     elif dot_product_middle <= 0 and dot_product_index>0 and ((self.right_click and (self.left_click is False)) is False):
    #         # right click
    #         # print( " val in right click : "+ str(((self.right_click and (self.left_click is False)) is False)))
    #         self.right_click = True
    #         self.left_click = False
    #         click_return = "right"
    #         print("clicked : right")
    #         mouse_controller.right_click()
    #     elif dot_product_index <= 0 and dot_product_middle>0 and ((self.left_click and (self.right_click is False)) is False):
    #         # left click
    #         self.right_click = False
    #         self.left_click = True
    #         click_return = "left"
    #         print("clicked : left")
    #         mouse_controller.left_click()
    #     return click_return
    #
    # def set_palm_direction(self):
    #     pos0 = self.landmarks[0] * 1000
    #     pos5 = self.landmarks[5] * 1000
    #     self.palm_vector = (pos5[0] - pos0[0], pos5[1] - pos0[1])
    #
    # def set_index_direction(self):
    #     pos7 = self.landmarks[7] * 1000
    #     pos8 = self.landmarks[8] * 1000
    #     self.index_vector = (pos8[0] - pos7[0], pos8[1] - pos7[1])
    #
    # def set_middle_direction(self):
    #     pos11 = self.landmarks[11] * 1000
    #     pos10 = self.landmarks[10] * 1000
    #     self.middle_vector = (pos11[0] - pos10[0], pos11[1] - pos10[1])
