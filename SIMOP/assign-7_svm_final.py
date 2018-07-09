

import pandas as pd
from sklearn import svm,preprocessing
import numpy as np
df=pd.read_csv('simop 0-768.csv')
Dataset=np.array(df)

test_size=0.3
TrainData=Dataset[:-int(test_size*(len(Dataset)))]
TestData=Dataset[-int(test_size*(len(Dataset))):]
x_train=TrainData[:,0:-1]
print(x_train)
y_train=TrainData[:,len(TrainData[0])-1]
print(y_train)
x_test=TestData[:,0:-1]
y_test=TestData[:,len(TestData[0])-1]
clf=svm.SVC()
clf.fit(x_train,y_train)
confidence=clf.score(x_test,y_test)
print("confidence:- ",confidence)
