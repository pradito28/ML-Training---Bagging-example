import pandas as pd

df_wine = pd.read_csv("C:/Users/pradi/Self taught ML/Understanding Classifiers/wine.data",
                      header=None)

df_wine.columns = ['Class label', 'Alcohol', 'Malic acid', 'Ash',
                   'Alcalinity of ash', 'Magnesium', 'Total phenols',
                   'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins',
                   'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
                   'Proline']
df_wine = df_wine[df_wine['Class label'] != 1]

y = df_wine['Class label'].values
X = df_wine[['Alcohol', 'OD280/OD315 of diluted wines']].values

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


le = LabelEncoder()
y = le.fit_transform(y)

X_train, X_test, y_train, y_test =            train_test_split(X, y, 
                             test_size=0.2, 
                             random_state=1,
                             stratify=y)

#Next, we are using the BaggingClassifier algorithm from ensemble. Our basic classifier will be a deciison tree and we will create
#an ensemble of 500 decision trees adjusted in different Bootstrap from the training dataset:

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

tree=DecisionTreeClassifier(criterion="entropy", random_state=1, max_depth=None)

bag=BaggingClassifier(base_estimator=tree,
                      n_estimators=500,
                      max_samples=1.0,
                      max_features=1.0,
                      bootstrap=True,
                      bootstrap_features=False,
                      n_jobs=1,
                      random_state=1                    
            
                     )
#Now we compare the Tree wuith the Bagging
from sklearn.metrics import accuracy_score

tree=tree.fit(X_train,y_train)
y_train_pred=tree.predict(X_train)
y_test_pred=tree.predict(X_test)
tree_train=accuracy_score(y_train, y_train_pred)
tree_test=accuracy_score(y_test, y_test_pred)

#Now we check the accuracy scores

print ("TRee train, tree test: %.3f/%.3f" %(tree_train, tree_test))
bag = bag.fit(X_train, y_train)
y_train_pred = bag.predict(X_train)
y_test_pred = bag.predict(X_test)

bag_train = accuracy_score(y_train, y_train_pred) 
bag_test = accuracy_score(y_test, y_test_pred) 
print('Bagging train/test accuracies %.3f/%.3f'
      % (bag_train, bag_test))
