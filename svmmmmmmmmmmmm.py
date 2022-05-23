import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
from sklearn import neighbors, datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

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
y=bruises

k_fold=2
new_X=[[] for i in range(k_fold)]
new_y=[[] for i in range(k_fold)]

edible_count=0
group=0
for i in range(len(classe)):
    if(y[i]=="t"):
        edible_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(edible_count==int(len(classe)/2/k_fold)):
            edible_count=0
            group+=1

poisonous_count=0
group=0
for i in range(len(classe)):
    if(y[i]=="f"):
        poisonous_count+=1
        new_X[group].append(X[i])
        new_y[group].append(y[i])
        if(poisonous_count==int(len(classe)/2/k_fold)):
            poisonous_count=0
            group+=1

total_percentage=0
for test_group in range(k_fold):
    train_X=[]
    train_y=[]
    test_X=[]
    test_y=[]
    for target_group in range(k_fold):
        if(target_group==test_group):
            test_X=new_X[target_group]
            test_y=new_y[target_group]
        elif(target_group!=test_group):
            train_X=train_X+new_X[target_group]
            train_y=train_y+new_y[target_group]
    print(train_X)
    print(train_y)
    n_neighbors = 15
    clf=neighbors.KNeighborsClassifier(n_neighbors,'distance')
    #clf=LinearDiscriminantAnalysis(n_components=1)
    clf.fit(train_X,train_y)
    model_answer=clf.predict(test_X)

    total_count=0
    correct_count=0
    for i in range(len(model_answer)):
        total_count+=1
        if(model_answer[i]==test_y[i]):
            correct_count+=1
    percentage=correct_count/total_count*100
    total_percentage+=percentage
    print("test_group: "+str(test_group))
    print("Correct percentage: "+str(percentage)+",   "+str(correct_count)+"/"+str(total_count)+"\n")
total_percentage/=k_fold
print("Cross validation accuracy: "+str(total_percentage))