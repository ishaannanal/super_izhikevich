#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:27:11 2021

@author: ishaann
"""

import izhikevich_cells as izh

class cCell (izh.izhCell):
    def __init__(self,stimVal):
        # define Neuron Parameters
        super().__init__(stimVal)
        self.cellType = 'Chattering Cell'
        self.c = 50
        self.vr = -60
        self.vt = -45
        self.k = 1.5
        self.a = 0.03
        self.b = 1
        self.c = -56
        self.d = 150
        self.vpeak = 25

# Creates a new Cell
myCell = cCell(4000)
myCell.simulate()

if __name__ == '__main__':
    # Plot the data
    izh.plotMyData(myCell)