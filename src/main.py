#little script to generate Walther-Lieth style Climate diagrams
from tkinter import BooleanVar, Button, Checkbutton, Frame, Label, Text, Tk
from tkinter.ttk import Combobox
from sys import argv

from matplotlib import axes, figure, pyplot

import util

from modules.climate_diagram import walter_lieth

nieder_scale = 120
temp = "Temperatur"
nieder = "Niederschlag"

def gui():
    window = Tk()
    window.title("Climate Diagrams by Christoferis")

    #Diagram, output and everything
    data = Frame(window)
    io = Frame(data)
    Label(io, text="Dataset").pack()
    dataset = util.gui_get_file(master=io, filetypes=[("CSV-File", "*.csv")], save=False)
    dataset.pack()

    Label(io, text="Output").pack()
    output = util.gui_get_file(master=io, save=True, filetypes=[("PDF-Document", "*.pdf"), ("Scalable Vector Graphics", "*.svg")] )
    output.pack()
    io.pack()

    #add in more stuff
    spec = Frame(data)
    #add in Spinbox for Column Checkboxes preview
    Label(spec, text="Read in").pack()
    rw = Combobox(spec, state="readonly")
    rw["values"] = ("per Column", "per Row")
    rw.pack()

    pr = BooleanVar()

    prev = Checkbutton(spec, text="Preview", variable=pr)
    prev.pack()

    spec.pack(side="bottom")
    data.pack()

    #Frame for additional Info + TODO: Radiobutton to activate it
    info = Frame(window)

    #Weather Station
    weather = Frame(info)
    Label(weather, text="Weather Station / Country").pack()
    w_place = Text(weather, height=1, width=25)
    w_place.pack(side="left", expand=0, fill="x")
    w_cou = Text(weather, height=1, width=25)
    w_cou.pack(side="right", expand=0, fill="x")
    weather.pack()

    #Coordinates, Elevation
    extra = Frame(info)
    Label(extra, text="Elevation").pack()
    e_ele = Text(extra, height=1, width=50)
    e_ele.pack()
    Label(extra, text="Weather Station Coordinates").pack()
    e_coo = Text(extra, height=1, width=50)
    e_coo.pack()
    extra.pack(side="bottom")

    info.pack()

    # button and other stuff
    end = Frame(window)
    Button(end, text="Create a Diagram", command=lambda: validate(dataset=dataset.get_path(), output=output.get_path(), read=rw.get(), city=w_place.get(1.0, "end"), country=w_cou.get(1.0, "end"), coords=e_coo.get(1.0, "end"), elevation=e_ele.get(1.0, "end"), prev=pr.get())).pack()

    end.pack()

    #TODO: Options
    #include chart
    #include Temperature, Rainfall Averages

    window.mainloop()

#compile and validate certain parts
def validate(dataset, output, read, prev, city, coords, country, elevation):

    #validate all of those things
    if dataset in (None, "", "\n"):
        raise util.MissingInfoException("Input Dataset is Missing!")

    if output in (None, "", "\n"):
        if prev is False:
            output = dataset.removesuffix(".csv") + ".svg"
    
    if read in (None, "", "\n"):
        raise util.MissingInfoException("Please choose a Read in Type. If you are unsure please Choose 'per Column' Read in Type")

    #plot the thingy

    print({"path": dataset, "output": output, "read-mode": read, "preview": prev, "city": city, "coords": coords, "country": country, "elevation": elevation})

    walter_lieth({"path": dataset, "output": output, "read-mode": read, "preview": prev, "city": city, "coords": coords, "country": country, "elevation": elevation})

    pass


def main():
    try:
        gui()
    except Exception as e:
        print(e)
        pass


if __name__ == "__main__":
    main()
