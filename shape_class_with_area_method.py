#!/bin/python3

import math
import os
import random
import re
import sys

class Rectangle:
    def _init_(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length

    pass

class Circle:
    def _init_(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    pass
if _name_ == '_main_':