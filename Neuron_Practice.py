#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:32:14 2021

@author: ishaann
"""
import neuron as h
try:
    from neuron.units import ms,mV
except ModuleNotFoundError:
    ms = 1
    mV = 1
#from neuron.units import ms, mV
soma = h.Section(name = 'Soma')

