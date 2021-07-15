#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:27:12 2021

@author: ishaann
"""

import izhikevich_cells as izh

class ibCell (izh.izhCell):
    def __init__ (self,stimval):
        #define Neuron Parameters
        super().__init__(stimval)
        self.celltype = 'Intrinsically Bursting'
        self.c = 150
        self.vr = -75
        self.vt = -45
        self.k = 1.2
        self.a = 0.01
        self.b = 5
        self.c = -56
        self.d = 130
        self.vpeak = 50

#Creates a new cell
myCell = ibCell(4000)
myCell.simulate()

if __name__ == '__main__':
    # Plot the data
    izh.plotMyData(myCell)