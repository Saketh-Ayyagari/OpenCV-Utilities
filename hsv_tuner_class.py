from tkinter import *
'''
Saketh Ayyagari
Class containing GUI for HSV Tuner Window.
Allows for tuning HSV values for OpenCV Contour Detection
'''
#################
# Constants
#################
SLIDER_LENGTH = 300

class HSVTuner():
    def __init__(self):
        # initialzing window and title
        self.tk = Tk() 
        self.title = Label(text="HSV Tuner")

        # initializing lower and upper HSV bounds
        self.hsv_low = (0, 0, 0)
        self.hsv_high = (0, 0, 0)

        # initializing titles BEFORE sliders 
        # (goes for both lower and upper HSV bounds)
        self.lower_title = Label(text="Lower HSV Bound")
        # initializing lower sliders
        self.h_low_scale = Scale(self.tk, from_=0, to=180, orient=HORIZONTAL, length=SLIDER_LENGTH) 
        self.s_low_scale = Scale(self.tk, from_=0, to=255, orient=HORIZONTAL, length=SLIDER_LENGTH)   
        self.v_low_scale = Scale(self.tk, from_=0, to=255, orient=HORIZONTAL, length=SLIDER_LENGTH)
        
        self.higher_title = Label(text="Upper HSV Bound")
        # initializing upper sliders
        self.h_high_scale = Scale(self.tk, from_=0, to=180, orient=HORIZONTAL, length=SLIDER_LENGTH)   
        self.s_high_scale = Scale(self.tk, from_=0, to=255, orient=HORIZONTAL, length=SLIDER_LENGTH)   
        self.v_high_scale = Scale(self.tk, from_=0, to=255, orient=HORIZONTAL, length=SLIDER_LENGTH)   
        # initializing button to return HSV range
        self.return_hsv_values = Button(self.tk, text="Get HSV Range", command=self.get_range)
        
    '''
    Packs all variables in order to appear in GUI
    '''
    def pack_all_components(self):
        self.title.pack()

        # packing titles first followed by sliders
        self.lower_title.pack()
        self.h_low_scale.pack()
        self.s_low_scale.pack()
        self.v_low_scale.pack()

        self.higher_title.pack()
        self.h_high_scale.pack()
        self.s_high_scale.pack()
        self.v_high_scale.pack()

        self.return_hsv_values.pack()
    '''
    Runs/reshreshes GUI and HSV bounds from slider values
    
    NOTE: run() does not permanently run the GUI; it only refreshes it once, 
    so when implementing it, it must be run sequentially after displaying your 
    camera stream.
    '''
    def run(self):
        self.pack_all_components()
        self.update_hsvs()
        self.tk.update()
    '''
    Updates lower and upper hsv bounds based on slider values
    '''
    def update_hsvs(self):
        self.hsv_low = (self.h_low_scale.get(),
                        self.s_low_scale.get(),
                        self.v_low_scale.get())
        self.hsv_high = (self.h_high_scale.get(),
                        self.s_high_scale.get(),
                        self.v_high_scale.get())   
    '''
    Updates hsvs
    Returns pair of tuples specifiying lower and upper HSV value range
    '''
    def get_range(self):
        return (self.hsv_low, self.hsv_high)
    