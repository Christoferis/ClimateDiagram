#little script to generate Walther-Lieth style Climate diagrams
from matplotlib import axes, figure, pyplot
from numpy import arange
from tkinter import Tk, Label, Text, Button, Frame

import util

#vars

def compile():
    pass

def gui():
    diagram_info = {}

    window = Tk()
    window.title("Climate Diagrams by Christoferis")


    #Diagram, output and everything
    data = Frame(window)
    Label(data, text="Dataset").pack()
    dataset = util.gui_get_file(master=data, filetypes=[("CSV-File", "*.csv")], save=False)
    dataset.pack()

    data.pack()

    #Frame for additional Info + TODO: Radiobutton to activate it
    info = Frame(window)

    #Weather Station
    weather = Frame(info)
    Label(weather, text="Weather Station / Country").pack()
    w_place = Text(weather)
    w_place.pack(side="left")
    w_cou = Text(weather)
    w_cou.pack(side="right")
    weather.pack()

    #Coordinates, Elevation
    extra = Frame(info)
    Label(extra, text="Elevation").pack()
    e_ele = Text(extra)
    e_ele.pack()
    Label(extra, text="Weather Station Coordinates").pack()
    e_coo = Text(extra)
    e_coo.pack()
    extra.pack(side="bottom")

    info.pack()

    #TODO: Options
    #include chart
    #include Temperature, Rainfall Averages

    window.mainloop()

def plot(diagram_info):

    data = util.csv_to_dict(csvpath=diagram_info, output_type="column")
    fig, y1 = pyplot.subplots()

    print(data)

    y1.plot(util.NUM, data["\ufeffNiederschlag"])
    #TODO Rewrite https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html#sphx-glr-gallery-subplots-axes-and-figures-two-scales-py
    #build the initial figure
    #y1

    #x


    #plot the data
    # y1.plot(util.NUM, data["Temperatur"])


    pyplot.show()
    
    pass

def main():
    gui()
    pass


if __name__ == "__main__":
    # main()
    plot("test/Test.csv")
