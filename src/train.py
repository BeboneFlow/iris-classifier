from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
print(iris.feature_names, iris.target_names)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
model_predictions = model.predict(X_test)
print("Predictions:", model_predictions[:5])
print("True labels:", y_test[:5])
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, model_predictions)
print("Accuracy:", accuracy)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
model2 = KNeighborsClassifier(n_neighbors=5)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
print("k-NN accuracy:", accuracy_score(y_test, y_pred2))
from sklearn.neighbors import KNeighborsClassifier
model2 = KNeighborsClassifier(n_neighbors=5)
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
print("k-NN accuracy:", accuracy_score(y_test, y_pred2))
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
pruned_accuracy = accuracy_score(y_test, model.predict(X_test))
print("Pruned Decision Tree Accuracy:", pruned_accuracy)
y_true = [1,0,2,1,1]
y_pred = [1,0,2,1,1]
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
cm = confusion_matrix(y_true, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Class 0', 'Class 1', 'Class 2'])
disp.plot()
disp.figure_.savefig('confusion_matrix.png', dpi=300, bbox_inches='tight')