import matplotlib.pyplot as plt
import math

def import_data(filename):
    data = open(filename)
    data = data.read()
    data = data.split("\n")
    for i in range(1,len(data)):
        data[i] = data[i].split(",")
        for j in range(len(data[i])):
            data[i][j] = float(data[i][j])
    return data

def sort_data(index, data):
    collection= {}

    if index in [1,2]:
        for i in data[1:]:
            if euclidean_distance([i[1],i[2]],[i[6],i[7]]) in collection:
                collection[euclidean_distance([i[1],i[2]],[i[6],i[7]])][0] += 1
                collection[euclidean_distance([i[1],i[2]],[i[6],i[7]])][1] += i[4]
            else:
                collection[euclidean_distance([i[1],i[2]],[i[6],i[7]])] = [1,i[4]]
    else:
        for i in data[1:]:
            if i[index] in collection:
                collection[i[index]][0] += 1
                collection[i[index]][1] += i[4]
            else:
                collection[i[index]] = [1,i[4]]
    

    
    return collection

def pythagoras(p_1, p_2):
    return math.sqrt(math.pow(p_1,2)+math.pow(p_2,2))

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)


def lower_resolution(values,keys, res):
    new_key = []
    new_values = []
    for i in range(int(len((keys))/res)):
        print(i)
        new_key.append(keys[i*res] +" - "+ keys[i*res +res-1])
        new_values.append(sum(values[i*res:i*res+res-1]))
    return [new_key, new_values]


def plot_data(data_dict, res="full"):
        sorted_keys = sorted(data_dict.keys())
        sorted_data = {key: data_dict[key] for key in sorted_keys}
        keys = list(sorted_data.keys())
        values = list(sorted_data.values())
        
        
        
        for i in range(len(keys)):
            
            keys[i] = str(keys[i])
        for i in range(len(values)):
            
            values[i] = values[i][1]/values[i][0]
        
        if res != "full":
            print(values)
            print(len(keys))
            x = lower_resolution(values,keys,res)
            values = x[1]
            keys = x[0]
        print(values)
        print(keys)
        plt.bar(keys, values)
        plt.show()

plot_data(sort_data(-5, import_data("siren_data_train.csv")))