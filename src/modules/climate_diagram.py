#this is part of ClimateDiagrams by Christoferis
#this module offers the most common visualisations of Climate Diagrams, Walter Lieth and Köppen Geiger

import util
from matplotlib import pyplot


def walter_lieth(diagram_info : dict):

    data = util.csv_to_dict(csvpath=diagram_info["path"], output_type="column" if diagram_info["read-mode"] == "per Column" else "row")
    fig, y1 = pyplot.subplots()

    print(data)

    #scale the data -_-
    for i in enumerate(data["Niederschlag"]):
        if i[1] > 100:
            new = 100 + (i[1] / 20)
            data["Niederschlag"][i[0]] = new
    
    
    # y1.set_aspect(0.2)
    y1.plot(util.NUM, data["Temperatur"], color="red")
    y1.set_yticks([-20, -10, 0, 10, 20, 30, 40])
    y1.set_ylim(-20, 120 / 2)

    y2 = y1.twinx()
    y2.set_yticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
    y2.set_yticklabels([0, 20, 40, 60, 80, 100, 200, 300, 400])
    y2.set_ylim(-40, 120)
    y2.plot(util.NUM, data["Niederschlag"])

    #plot the data

    #plot Candy
    #adding arrid and humid indicators
    for i in enumerate(data["Temperatur"]):
        #arrid double the points
        if i[1] * 2 > data["Niederschlag"][i[0]]:
            y1.vlines(x=[i[0] + 1], ymin=data["Niederschlag"][i[0]] / 2, ymax=i[1], linestyles="dotted", colors=["red"])
        #humid
        else:
            y2.vlines(x=[i[0] + 1], ymax=data["Niederschlag"][i[0]], ymin=i[1] * 2, linestyles="solid")

        pass

    y1.axhline(y=0, xmax=1, xmin=0, color="black", linewidth=1)

    #fill top
    x_vals = []
    rain = []

    prev = None
    # get points that cut the 100 line
    for i in enumerate(data["Niederschlag"]):
        #pre
        if prev and prev <= 100 and i[1] >= 100 and prev < i[1]:
            diff = i[1] - prev
            diff100 = i[1] - 100
            #the intersection -> percentage and apply to one
            point = 1 - (diff100 / diff)
            x_vals.append(i[0] + point)
            rain.append(100)

        #this
        if i[1] >= 100:
            #see the intersection
            x_vals.append(i[0] + 1)
            rain.append(i[1])
        #after
        if prev and prev >= 100 and i[1] <= 100 and prev > i[1]:
            diff = prev - i[1]
            diff100 = prev - 100
            #the intersection -> percentage and apply to one
            point = (diff100 / diff)

            x_vals.append(i[0] + point)
            rain.append(100)

        prev = i[1]
        print(prev)
    
    y2.fill_between(x=x_vals, y2=rain, y1=100)
    print(x_vals)
    print(rain)


    #Months
    y1.set_xticks(util.NUM)
    y1.set_xticklabels(util.MONTHS)


    #All other stuff that has to be mentioned
    y1.set_title(f"{diagram_info['city']} / {diagram_info['country']} \n {diagram_info['coords'] if diagram_info['coords'] != None else util.nothing()}")
    y1.set_ylabel("Temperature in °C")
    y1.set_xlabel("Months")
    y2.set_ylabel("Rainfall in mm")

    if diagram_info["preview"]:
        pyplot.show()
    else:
        pyplot.savefig(diagram_info["output"])
    
    pass

def koppen_geiger(diagram_info : dict):

    data = util.csv_to_dict(csvpath=diagram_info["path"], output_type="column" if diagram_info["read-mode"] == "per Column" else "row")
    fig, y1 = pyplot.subplots()

    print(data)
    
    
    # y1.set_aspect(0.2)
    y1.plot(util.NUM, data["Temperatur"], color="red")
    y1.set_yticks([-20, -10, 0, 10, 20, 30, 40])
    y1.set_ylim(-20, 120 / 2)

    y2 = y1.twinx()
    y2.set_yticks([0, 20, 40, 60, 80, 100, 120, 140, 160])
    y2.set_yticklabels([0, 20, 40, 60, 80, 100, 200, 300, 400])
    y2.set_ylim(-40, 120)
    y2.bar(util.NUM, data["Niederschlag"])

    #plot the data

    #plot Candy

    y1.axhline(y=0, xmax=1, xmin=0, color="black", linewidth=1)

    #fill top
    x_vals = []
    rain = []

    prev = None
    
    y2.fill_between(x=x_vals, y2=rain, y1=100)
    print(x_vals)
    print(rain)


    #Months
    y1.set_xticks(util.NUM)
    y1.set_xticklabels(util.MONTHS)


    #All other stuff that has to be mentioned
    y1.set_title(f"{diagram_info['city']} / {diagram_info['country']} \n {diagram_info['coords'] if diagram_info['coords'] != None else util.nothing()}")
    y1.set_ylabel("Temperature in °C")
    y1.set_xlabel("Months")
    y2.set_ylabel("Rainfall in mm")

    if diagram_info["preview"]:
        pyplot.show()
    else:
        pyplot.savefig(diagram_info["output"])
    
    pass
