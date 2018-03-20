from hyperopt import hp
list_space = [
    hp.uniform('a', 0, 1),
    hp.loguniform('b', 0, 1)
]
tuple_space = (
    hp.uniform('a', 0, 1),
    hp.loguniform('b', 0, 1)
)
dict_space = {
    'a': hp.uniform('a', 0, 1),
    'b': hp.loguniform('b', 0, 1)
}

space = list_space
import hyperopt.pyll.stochastic
print hyperopt.pyll.stochastic.sample(space)

print hyperopt.pyll.stochastic.sample(tuple_space)


print hyperopt.pyll.stochastic.sample(dict_space)
from hyperopt.pyll import scope
def foo(x):
    return str(x) * 3

expr_space = {
    'a': 1 + hp.uniform('a', 0, 1),
    'b': scope.minimum(hp.loguniform('b', 0, 1), 10),
    'c': scope.call(foo, args=(hp.randint('c', 5),)),
}
print hyperopt.pyll.stochastic.sample(expr_space)

space = {"n_iter":hp.choice("n_iter",range(30,50)),
         "eta":hp.uniform("eta",0.05,0.5)}

print hyperopt.pyll.stochastic.sample(space)
