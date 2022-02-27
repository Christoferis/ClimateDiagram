# https://github.com/christoferis
#util functions live here

# outputs a csv as a dictionary
# outputtype : Row or Columns as dictionary keys, "row", "column", "raw"
def csv_to_dict(csvpath, output_type):

    out = {}
    raw = []

    with open(csvpath, mode='r', encoding="utf-8") as openobj:
        #compile each row into 2dimensional list
        for line in openobj:
            raw.append(line.split(";"))

    #remove useless vals
    temp = []
    for line in raw:
        a = []

        for thing in line:
            if thing in ('', '\r\n', '\n'):
                continue
            a.append(thing)
        
        temp.append(a)
    
    raw = temp


    #depending on outputtype
    if output_type == "column":
        keys = raw.pop(0)

        #create list
        for key in keys:
            out[key] = []

        for i in raw:
            for j in range(len(i)):
                try:
                    out[keys[j]].append(i[j])
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


if __name__ == "__main__":
    #load in example file

    print(csv_to_dict("test/Test.csv", "column"))

    pass
