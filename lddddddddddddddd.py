import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn import neighbors, datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

file=open('mushrooms.csv')

file=open('mushrooms.csv')

classe=[]
capshape=[]
capsurface=[]
capcolor=[]
bruises=[]
odor=[]
gillattachment=[]
gillspacing=[]
gillsize=[]
gillcolor=[]
stalkshape=[]
stalkroot=[]
stalksurfaceabovering=[]
stalksurfacebelowring=[]
stalkcolorabovering=[]
stalkcolorbelowring=[]
veiltype=[]
veilcolor=[]
ringnumber=[]
ringtype=[]
sporeprintcolor=[]
population=[]
habitat=[]

for line in file.readlines():
    line=line.replace("\n","")
    input_classe, input_capshape, input_capsurface, input_capcolor, input_bruises, inpur_odor, input_gillattachment, input_gillspacing, input_gillsize, input_gillcolor, input_stalkshape, input_stalkroot, input_stalksurfaceabovering, input_stalksurfacebelowring, input_stalkcolorabovering, input_stalkcolorbelowring, input_veiltype, input_veilcolor, input_ringnumber, input_ringtype, input_sporeprintcolor, input_population, input_habitat = line.split(",")
    classe.append(input_classe)
    capshape.append(input_capshape)
    capsurface.append(input_capcolor)
    capcolor.append(input_capcolor)
    bruises.append(input_bruises)
    odor.append(inpur_odor)
    gillattachment.append(input_gillattachment)
    gillspacing.append(input_gillspacing)
    gillsize.append(input_gillsize)
    gillcolor.append(input_gillcolor)
    stalkshape.append(input_stalkshape)
    stalkroot.append(input_stalkroot)
    stalksurfaceabovering.append(input_stalksurfaceabovering)
    stalksurfaceabovering.append(input_stalksurfaceabovering)
    veiltype.append(input_veiltype)
    veilcolor.append(input_veilcolor)
    ringnumber.append(input_ringnumber)
    ringtype.append(input_ringtype)
    sporeprintcolor.append(input_sporeprintcolor)
    population.append(input_population)
    habitat.append(input_habitat)

    X = []
    for i in range(len(classe)):
        X.append([classe[i], gillsize[i]])
    y = bruises

clf = LinearDiscriminantAnalysis(n_components=2)
clf.fit(X,y)

print(clf.predict)





import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

file=open('mushrooms.csv')

classe=[]
capshape=[]
capsurface=[]
capcolor=[]
bruises=[]
odor=[]
gillattachment=[]
gillspacing=[]
gillsize=[]
gillcolor=[]
stalkshape=[]
stalkroot=[]
stalksurfaceabovering=[]
stalksurfacebelowring=[]
stalkcolorabovering=[]
stalkcolorbelowring=[]
veiltype=[]
veilcolor=[]
ringnumber=[]
ringtype=[]
sporeprintcolor=[]
population=[]
habitat=[]

for line in file.readlines():
    line=line.replace("\n","")
    input_classe, input_capshape, input_capsurface, input_capcolor, input_bruises, inpur_odor, input_gillattachment, input_gillspacing, input_gillsize, input_gillcolor, input_stalkshape, input_stalkroot, input_stalksurfaceabovering, input_stalksurfacebelowring, input_stalkcolorabovering, input_stalkcolorbelowring, input_veiltype, input_veilcolor, input_ringnumber, input_ringtype, input_sporeprintcolor, input_population, input_habitat = line.split(",")
    classe.append(input_classe)
    capshape.append(input_capshape)
    capsurface.append(input_capcolor)
    capcolor.append(input_capcolor)
    bruises.append(input_bruises)
    odor.append(inpur_odor)
    gillattachment.append(input_gillattachment)
    gillspacing.append(input_gillspacing)
    gillsize.append(input_gillsize)
    gillcolor.append(input_gillcolor)
    stalkshape.append(input_stalkshape)
    stalkroot.append(input_stalkroot)
    stalksurfaceabovering.append(input_stalksurfaceabovering)
    stalksurfaceabovering.append(input_stalksurfaceabovering)
    veiltype.append(input_veiltype)
    veilcolor.append(input_veilcolor)
    ringnumber.append(input_ringnumber)
    ringtype.append(input_ringtype)
    sporeprintcolor.append(input_sporeprintcolor)
    population.append(input_population)
    habitat.append(input_habitat)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    mushrooms.csv['data'], mushrooms.csv['target'], random_state=0)
print("X_train: {}".format(X_train.shape))
print("y_train: {}".format(y_train.shape))
print("X_test: {}".format(X_test.shape))
print("y_test: {}".format(y_test.shape))

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train,y_train)

X_new = np.array([[]])

prediction = knn.predict(X_new)

print("name: {}".format(mushrooms.csv['target_name'][prediction]))

y_prediction = knn.predict(X_test)

for i in range(0, len(y_prediction)):
    y = y_prediction[i]
    print("{} : {}".format(X_test[i], mushrooms.csv['target_name']))