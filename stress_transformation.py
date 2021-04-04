'''
2019-05-3
Author: Sam Joshua 

Class for transforming stress & strain states for a 2d case
'''

import numpy as np
from math import radians,sqrt
import matplotlib.pyplot as plt

class StressTransformation:

    '''
    Class for transforming stress in 2D
    '''

    def __init__(self, stress_state, angle, angle_type=None):
        # [sig1, sig2, sig12] # order of defining the stress vector
        if angle_type == None or angle_type.startswith('d'):
            self.angle = np.degrees(angle)
        else:
            self.angle = angle
        self.sig1 = stress_state[0][0]
        self.sig2 = stress_state[0][1]
        self.sig12 = stress_state[0][2]
        #
        self.stress_state = np.array([[self.sig1, self.sig12],
                                     [self.sig12, self.sig2]])
        self.angle = radians(angle)

    def transform_stress(self):
        c = np.cos(self.angle)
        s = np.sin(self.angle)
        self.q = np.array([[c,s],
                        [-s, c]])
        self.transformed_state = np.matmul(self.q, self.stress_state)
        self.transformed_state = np.matmul(self.transformed_state, np.transpose(self.q))
        return self.transformed_state

    


if __name__ == "__main__":
    theta = 30
    stress_state = [[-8, 12, -6]]
    load = StressTransformation(np.array(stress_state), theta)
    load.transform_stress()
