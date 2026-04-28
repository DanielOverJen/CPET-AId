import numpy as np 
import pandas as pd

####Hent af data ####

<<<<<<< HEAD
df = pd.read_csv("CPET-AId/Model selection/CPET_ProcessedDataMed154Rykket.csv")
=======
df = pd.read_csv("Model selection/CPET_ProcessedData.csv")
>>>>>>> origin/AdaBoost


df = df.iloc[:,3:] #Fjerner de 2 første søjler med patient ID og køn. Iloc gør at alle rækker starter fra søjle 3 og frem 


#Vi har fjernet de første 3 søjler, så for at hente labels skal det være mellem 5 og 9.
y = df.iloc[:, 5:9].values #søjler til supervised learning
<<<<<<< HEAD
# print(y)

classification_names = df.columns[5:9] #henter søjlenavne
# print(classification_names)


# print(y.shape[0]) #Her printer vi antallet af observationer, som gerne burde være 217
=======
#print(y)

classification_names = df.columns[5:9] #henter søjlenavne
#print(classification_names)


#print(y.shape[0]) #Her printer vi antallet af observationer, som gerne burde være 217
>>>>>>> origin/AdaBoost

y = np.argmax(y, axis= 1) #Samler søjlerne i 1 søjle med 0,1,2,3 værdier.
#0: hjerte, 1: Lunge, 2: muskulært/andet, 3: rask

<<<<<<< HEAD
# print(classification_names[y])
=======
#print(classification_names[y])
>>>>>>> origin/AdaBoost


# Features: resten af kolonnerne efter labels
X = df.iloc[:, 9:].values

feature_names = df.columns[9:]
#Vi shuffler rækkerne og inddeler til træning og test

np.random.seed(42)
indices = np.random.permutation(len(X))

X = X[indices] #Meget vigtigt at X og Y shuffles til de samme rækker. 
y = y[indices]

#80% til træning
split = int(0.8 * len(X))

X_train = X[:split]
X_test = X[split:]

y_train = y[:split]
y_test = y[split:]
