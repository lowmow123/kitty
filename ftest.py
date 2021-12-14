from kittym import *

def test():
  f=funclist('allkeys')
  for i in f:
    print(eval_py(funclist(i)[2]))
  

