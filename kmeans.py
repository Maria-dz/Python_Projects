import math
import scipy
import numpy as np
from pandas import *
import matplotlib.pyplot as plt
import PIL




# функция для определения, к какому кластеру относится точка
def closest(dot, centers):  # dot = (a,b,c,...)
    nearest_center = 0
    min_len = 0
    ind = -1

    for center in centers:
        cur_length = 0
        ind += 1
        for i in range(len(dot)):
            cur_length += (center[i] - dot[i]) ** 2
        cur_length = math.sqrt(cur_length)
        if ind == 0:
            min_len = cur_length

        if cur_length <= min_len:
            min_len = cur_length
            nearest_center = ind
    return nearest_center


# функция для подсчета новых центров
def new_center(labels):
    new_coordinate = []
    coordinate = [0 for _ in range(len(labels[0]))]
    for i in range(len(labels[0])):
        for elem in labels:
            coordinate[i] += elem[i]
        new_coordinate += [coordinate[i]/len(labels)]
    return new_coordinate


class Kmeans:
    def __init__(self, n_clusters=2):
        self.n_clusters = n_clusters

    def fit(self, x):
        np.random.shuffle(x)
        y = DataFrame(x).drop_duplicates().values
        if self.n_clusters > len(y):      # если количество различных элементов в исходных данных меньше, чем n_clusters
            self.n_clusters = len(y)      # то мы уменьшаем число кластеров

        centers = y[:self.n_clusters]     # находим начальные центры

        while True:
            clusters = []
            for i in range(self.n_clusters):
                clusters.append([])

            for dot in x:
                clusters[closest(dot, centers)].append(dot)

            new_centers = []
            for elem in clusters:
                if len(elem) != 0:
                    new_centers += [new_center(elem)]

            check = True                                    # check == True, если новые центры совпадают со старыми

            for ind in range(len(centers)):
                for i in range(x.shape[1]):
                    check = check and (new_centers[ind][i] == centers[ind][i])   # проверяем на совпадение

            if not check:
                centers = np.array([elem for elem in new_centers])
            else:
                break
        return centers

    def labeling(self, x, centers):
        labels = []
        for dot in x:
            labels += [closest(dot, centers)]
        return labels

    def predict(x):
        return None


# обработка картинки
image = PIL.Image.open('C:\duck.jpg')
width = image.size[0]
height = image.size[1]
pix = image.load()

data = []
pix_data = []
for x in range(width//20):
    for y in range(height//20):
        r = pix[x, y][0]  # красный
        g = pix[x, y][1]  # зеленый
        b = pix[x, y][2]  # синий
        data += [[r, g, b, x, y ]]
        pix_data += [[x, y]]
print(pix_data)
pix_data = np.array(pix_data)


X = np.array(data)
a = Kmeans(n_clusters=9)
centers = a.fit(X)
labels = a.labeling(X, centers)

plt.scatter(pix_data[:, 0], pix_data[:, 1], c=labels)
plt.show()