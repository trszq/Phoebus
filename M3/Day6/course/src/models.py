#_*_coding:utf-8_*_

import os
import pickle

class BaseModel:
    def save(self):
        pickle.dump(self,open())
    def