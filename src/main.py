#little script to generate Walther-Lieth style Climate diagrams
from matplotlib import axes, figure, pyplot
from tkinter import Tk, Label, Text, Button, Frame

import util
from walter_lieth import walter, lieth

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
    
    # y1.set_aspect(0.2)
    y1.plot(util.NUM, data["Temperatur"], color="red")
    y1.set_yticks([-20, -10, 0, 10, 20, 30, 40])
    y1.set_ylim(0, 40)

    y2 = y1.twinx()
    # y2.set_yscale("function", functions=(walter, lieth))
    y2.set_yticks([0, 20, 40, 60, 80, 100, 200, 300, 500])
    y2.set_ylim(0, 80)
    y2.plot(util.NUM, data["\ufeffNiederschlag"])

    #plot the data

    #plot Candy

    #adding arrid and humid indicators
    for i in enumerate(data["Temperatur"]):
        #arrid
        if i[1] * 2 > data["\ufeffNiederschlag"][i[0]]:
            y1.vlines(x=[i[0] + 1], ymin=data["\ufeffNiederschlag"][i[0]] / 2, ymax=i[1], linestyles="dotted", colors=["red"])
        #humid
        else:
            y2.vlines(x=[i[0] + 1], ymax=data["\ufeffNiederschlag"][i[0]], ymin=i[1] * 2, linestyles="solid")

        pass

    y1.axhline(y=0, xmax=1, xmin=0, color="black", linewidth=1)

    #Months
    y1.set_xticks(util.NUM)
    y1.set_xticklabels(util.MONTHS)



    pyplot.show()
    
    pass

def main():
    gui()
    pass


if __name__ == "__main__":
    # main()
    plot("test/Test.csv")
