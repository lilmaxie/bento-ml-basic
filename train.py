import bentoml

from sklearn import svm
from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = svm.SVC(gamma='scale')
clf.fit(X, y)

saved_model = bentoml.sklearn.save_model("iris_clf", clf)
print(f"Model saved: {saved_model}")

# iris_clf:542h2zzldw2kuuc2
# it is stored in the local directory as a pickle file (C:Users\user\.bentoml\models\iris_clf\542h2zzldw2kuuc2\model.pkl)