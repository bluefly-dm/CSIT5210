import numpy as np
import pandas as pd
from sklearn import tree
from sklearn import metrics
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

decisionData=pd.read_csv("decisionData.csv")
featureData=decisionData.drop(columns=["Unnamed: 0","start_time","end_time","distance","to_latitude","to_longitude"])
featureData=featureData.drop(featureData[featureData.tripduration >= 20000].index)

inputData=featureData.drop(columns=["to_station_id"])
testX=inputData.iloc[0:10000]
trainX=inputData.iloc[10000:500000]


outputData=featureData["to_station_id"]
testY=outputData.iloc[0:10000]
trainY=outputData.iloc[10000:500000]


# X = [[2.3],[3.5],[1.2],[8.9]]
# y = [3,5,2,9]

clf = RandomForestClassifier(verbose=1,n_estimators=80, max_depth=12,oob_score=True)

# clf = tree.DecisionTreeClassifier(splitter="best",max_depth=11,min_samples_leaf=1)
clf.fit(trainX, trainY)

predictY=clf.predict(testX)
print("test score: "+str(metrics.accuracy_score(testY, predictY)))
#predictY=clf.predict(trainX)
#print("test score: "+str(metrics.accuracy_score(trainY, predictY)))
