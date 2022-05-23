file=open('mushrooms.csv')

classe=[]
capshape=[]
odor=[]
gillattachment=[]
gillspacing=[]
gillsize=[]d
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

clf = LinearDiscriminantAnalysis(n_components=1)
clf.fit(X,y)

print(clf.predict)