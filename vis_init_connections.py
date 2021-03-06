import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

data = []
with open('/home/nick/git/cell_wall_sims/allp.csv',"rb") as f:
    reader = csv.reader(f, delimiter=',')
    headers = reader.next()
    for row in reader:
        data.append(row)


uid_array = np.empty(len(data), dtype=int)
x_array = np.empty(len(data))
y_array = np.empty(len(data))
z_array = np.empty(len(data))
type_array = [None]*len(data)
nlistlen_array = np.empty(len(data), dtype=int)
nlist_array = [None]*len(data)
color_array = [None]*len(data)

ii = 0
for row in data:
    uid_array[ii] = row[0]
    x_array[ii] = row[1]
    y_array[ii] = row[2]
    z_array[ii] = row[3]
    type_array[ii] = row[4]
    if row[4] == ' H2O':
        color_array[ii] = [0, 0.3, 0.9, 0.8]
    elif row[4] == ' FA1':
        color_array[ii] = [0.9, 0.3, 0.3, 0.8]
    elif row[4] == ' FA2':
        color_array[ii] = [0.9, 0.3, 0.3, 0.8]
    elif row[4] == ' HC1':
        color_array[ii] = [0, 0.4, 0, 0.2]
    elif row[4] == ' HC2':
        color_array[ii] = [0, 0.4, 0, 0.2]
    else:
        color_array = 'black'
        print('no col assigned to type')
        
    nlistlen_array[ii] = row[5]
    try:
        nlist_array[ii] = np.array(map(int, (row[6].split(';'))))
    except:
        nlist_array[ii] = np.array(987654321)
        print("warning: element had no connections, setting to 987654321: ",ii)
        pass
    ii = ii + 1


dd = {'uid': uid_array, 'x': x_array, 'y': y_array, 'z': z_array, 'type': type_array, 'nlistlen': nlistlen_array, 'nlist': nlist_array, 'color': color_array}

rgba_colors = np.zeros((len(dd['color']), 4))
rgba_colors = dd['color']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dd['x'], dd['y'], dd['z'], color=rgba_colors)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()

#for ii in range(len(dd['uid'])):
#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
#    ax.scatter(dd['x'], dd['y'], dd['z'], c=dd['color'])
#    ax.set_xlabel("x")
#    ax.set_ylabel("y")
#    ax.set_zlabel("z")
#    try:
#        ml = len(dd['nlist'][ii])
#        for jj in range(0,ml):
#           ax.plot([dd['x'][ii],dd['x'][dd['nlist'][ii][jj]]], [dd['y'][ii],dd['y'][dd['nlist'][ii][jj]]], [dd['z'][ii],dd['z'][dd['nlist'][ii][jj]]], c='red') 
#        plt.show()
#    except:
#        pass



