import pickle
import network 
import csv
import random
from copy import deepcopy

input = []
output = []
structure = [13, 32, 16, 1]


with open('heart.csv') as data:
    reader = csv.reader(data, delimiter = ",")
    rowcount = 0
    for row in reader:
        if rowcount == 0:
            rowcount+= 1
            continue
        tempin = []
        tempout = []
        for elem in range(len(row)):
            if elem != len(row) - 1:
                tempin.append(float(row[elem]))
            else:
                tempout.append(float(row[elem]))
        input.append(tempin)
        output.append(tempout)


#COMMENT OUT BELOW LINES TO TRAIN THE NETWORK   

# for i in range(10):
#     print(i)
#     random.Random(i).shuffle(input)
#     random.Random(i).shuffle(output)
#     # if i == 0:
#     #     net = deepcopy(network.train(structure, input, output, 0.3, 5000))
#     # else:
#     #     net = deepcopy(network.resume(net, input, output, 0.3, 5000))
#     deepcopy(network.resume(net, input, output, 0.1, 1000))



file = open('network.obj', 'rb')
net = pickle.load(file)
file.close()

wrong = 0
right = 0
for i in range(len(input)):
    out = net.run(input[i])
    if out[0].round() == output[i][0]:
        right += 1
    else:
        wrong += 1
print(right, wrong)
print("Accuracy:", (100 / len(input)) * right)



