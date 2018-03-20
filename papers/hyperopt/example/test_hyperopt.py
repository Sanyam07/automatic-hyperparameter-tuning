from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn import datasets
from sklearn.preprocessing import normalize, scale
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials
 
 
iris = load_iris()
X = iris.data
y = iris.target
 
def hyperopt_train_test(params):
    X_ = X[:]
 
    if 'normalize' in params:
        if params.has_key('normalize'):
            X_ = normalize(X_)
            del params['normalize']
 
    if 'scale' in params:
        if params.has_key('scale'):
            X_ = scale(X_)
            del params['scale']
 
    clf = KNeighborsClassifier(**params)
    return cross_val_score(clf, X_, y).mean()
 
space4knn = {
    'n_neighbors': hp.choice('n_neighbors', range(1,50)),
    'scale': hp.choice('scale', [0, 1]), 
    'normalize': hp.choice('normalize', [0, 1])
}
 
def f(params):
    acc = hyperopt_train_test(params)
    return {'loss': -acc, 'status': STATUS_OK}
 
trials = Trials()
best = fmin(f, space4knn, algo=tpe.suggest, max_evals=100, trials=trials)
print best

