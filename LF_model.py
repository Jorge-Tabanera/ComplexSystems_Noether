#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 17:27:30 2019

@author: Jorge Tabanera


In this file we write the model developed in the Ling Feng's article.
"""
from numpy import zeros, ones
from numpy.random import uniform
from pylab import plot, show, hist

# PARAMETERS

n_agents = 50000 #number of agents
TIME = 500 #evolution steps
p = 0.0154 #buy probability (holding p <1)



#ALGORITHMIC EVOLUTION
def generar():
    
    group_sizes_evo = []
    groups = ones(n_agents) #groups of agents with different opinion
    
    for t in range(TIME):
        
        ACTIONS = 0
        
        for i in range(len(groups)):
            
            a = uniform()
            
            if a < p:
                
                ACTIONS = ACTIONS + groups[i] #buy
                
            elif p < a < 2*p:
                
                ACTIONS = ACTIONS - groups[i] #sell
                
        new_groups_size = n_agents/(abs(ACTIONS) + 1) #number of new opinion groups
        
        groups = [ n_agents/int(new_groups_size) for j in range(int(new_groups_size)) ]
        #we define new opinion groups
        
        group_sizes_evo.append(new_groups_size)
        
    return group_sizes_evo
    
    
a = generar()
hist(a, bins = 20, density = True)
