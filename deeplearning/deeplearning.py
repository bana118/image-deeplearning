import os
import numpy as np

from skimage import data, io, filters
import sklearn
from sklearn.datasets import load_svmlight_file
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.externals import joblib


#feature0 = data.imread('./teacher/1-all/0-0-screenshot.png')
#feature0 = feature0.reshape(len(feature0), -1).astype(np.float64)
#print(feature0)
#print(np.shape(feature0))

#feature = np.array([data.imread(f'./teacher/1-all/{path}') for path in os.listdir('./teacher/1-all')])
#feature = feature.reshape(len(feature), -1).astype(np.float64)
#print(feature[0])
#print(np.shape(feature))
#model = KMeans(n_clusters=1).fit(feature)
#print(model.score([feature0]))
feature1 = np.array([data.imread(f'./teacher/1-all/{path}') for path in os.listdir('./teacher/1-all')])
feature1 = feature1.reshape(len(feature1), -1).astype(np.float64)
feature2 = np.array([data.imread(f'./teacher/2-all/{path}') for path in os.listdir('./teacher/2-all')])
feature2 = feature1.reshape(len(feature2), -1).astype(np.float64)
feature25 = np.array([data.imread(f'./teacher/25-all/{path}') for path in os.listdir('./teacher/25-all')])
feature25 = feature25.reshape(len(feature25), -1).astype(np.float64)
feature = []
feature.extend(feature1[0:100])
feature.extend(feature2[0:100])
feature.extend(feature25[0:100])
print(np.shape(feature))

label1 = [1]*400
label2 = [2]*400
label25 = [25]*400
label = []
label.extend(label1[0:100])
label.extend(label2[0:100])
label.extend(label25[0:100])

classifier = OneVsRestClassifier(LinearSVC(), n_jobs=-1)
classifier.fit(feature, label)
joblib.dump(classifier, "svc.pkl.cmp", compress=True)
