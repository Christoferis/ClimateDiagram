# https://github.com/christoferis
#util functions live here

# outputs a csv as a dictionary
# outputtype : Row or Columns as dictionary keys, "row", "column", "raw"
from tkinter import Frame, Text, Button
from tkinter.filedialog import askopenfile, askopenfilename, asksaveasfile

MONTHS = ["J","F","M","A","M","J","J","A","S","O","N","D"]
NUM = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def nothing():
    return ""


def csv_to_dict(csvpath, output_type):

    out = {}
    raw = []

    with open(csvpath, mode='r', encoding="utf-8") as openobj:
        #compile each row into 2dimensional list
        for line in openobj:
            raw.append(line.split(";"))

    #remove useless vals / convert to numbers or bools
    temp = []
    for line in raw:
        a = []

        for thing in line:
            if thing in ('', '\r\n', '\n'):
                continue

            try:
                thing = float(thing)
            except ValueError:
                pass
            finally: 
                a.append(thing)
        
        temp.append(a)
    
    raw = temp


    #depending on outputtype
    if output_type == "column":
        form = raw.pop(0)
        keys = []

        #create list
        for key in form:
            if type(key) is str:
                key = key.removeprefix("\ufeff")

            keys.append(key)
            out[key] = []        

        for i in raw:
            for j in enumerate(i):
                try:
                    out[keys[j[0]]].append(j[1])
                except IndexError:
                    continue

    elif output_type == "row":
        #create list

        for list in raw:
            out[list[0]] = []
            for i in range(1, len(list)):
                out[list[0]].append(list[i])
    
    else:
        #just output the normal thing
        out = raw

    return out

#custom Exception

class MissingInfoException(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

#error screen


#custom frame that packs a simple gui thingy
class gui_get_file(Frame):

    def __init__(self, master, filetypes, save) -> None:
        super().__init__(master)
        #add the widgets to this
        self.txt = Text(self, state="disabled", height=1, width=50)
        self.txt.pack(side="left")

        if save:
            Button(self, text="Save", command=self.save_file).pack(side="right")
        else:
            Button(self, text="Open", command=self.open_file).pack(side="right")


        self.path = None
        self.filetypes = filetypes

    def open_file(self):
        self.path = askopenfile(filetypes=self.filetypes)
        try:
            self.txt.insert(1.0, self.path)
        except Exception:
            self.txt.insert(1.0, "")

    def save_file(self):
        self.path = asksaveasfile(filetypes=self.filetypes)

        try:
            self.txt.insert(1.0, self.path)
        except Exception:
            self.txt.insert(1.0, "")
    
    def get_path(self):
        return self.path


if __name__ == "__main__":
    #load in example file

    print(csv_to_dict("test/Test.csv", "column"))

    pass
