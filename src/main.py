#little script to generate Walther-Lieth style Climate diagrams
import matplotlib as plt
from tkinter import Tk, Label, Text, Button, Frame
import util

def gui():

    window = Tk()
    window.title("Climate Diagrams by Christoferis")

    #Frame for additional Info + TODO: Radiobutton to activate it
    info = Frame(window)

    #Weather Station
    weather = Frame(info)
    Label(weather, text="Weather Station / Country").pack()
    w_place = Text(weather).pack(side="left")
    w_cou = Text(weather).pack(side="right")
    weather.pack()

    #Coordinates, Elevation
    extra = Frame(info)
    Label(extra, text="Elevation").pack()
    e_ele = Text(extra).pack()
    Label(extra, text="Weather Station Coordinates").pack()
    e_coo = Text(extra).pack()
    extra.pack(side="bottom")

    info.pack()

    #TODO: Options
    #include chart
    #include Temperature, Rainfall Averages






    window.mainloop()

def plot(data):
    pass

def main():
    gui()
    pass


if __name__ == "__main__":
    main()
