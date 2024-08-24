import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

service=ctrl.Antecedent(np.arange(1,11,1),'service')
service['low']=fuzzy.trimf(service.universe,[1,1,4])
service['medium']=fuzzy.trapmf(service.universe,[3,4,6,7])
service['high']=fuzzy.trapmf(service.universe,[6,8,10,10])
service.view()
plt.show()