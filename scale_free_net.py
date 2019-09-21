# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import networkx as nx
import numpy as np
from numpy.random import uniform
from pylab import plot, show


N = 10
m = 2


topo = 1 #ratio de ganancia de confianza topológica
anchura = 0.1 #anchura sigmoide

    
################# FUNCIONES DEL ALGORITMO ##############
    
def sigmoide(anchura,x):
    
    return 1/(1+np.exp(-anchura*x))

class RED():
    
    
    def __init__(self, N, m):

        self.G = nx.barabasi_albert_graph(N, m)
        
        self.grupos = np.linspace(0,N,N)
        
        for node in range(N):
            self.G.nodes[node]['group'] = self.grupos[np.random.randint(0, len(self.grupos))]
            self.G.nodes[node]['Psi'] = np.random.choice([0,1])
            
            #Los grupos se están asignando aleatoriamente
                       
    def avanzar_red(self,topo, p, q, N):
        
        #definimos un diccionario grupo : siguiente Psi
        self.diccionario = {}
        for grupo in self.grupos:
            
            random = np.random.uniform()
            
            if  random <  p:
            
                self.diccionario[grupo] = 1
                
            elif random < q:
                
                self.diccionario[grupo] = -1
                
            elif random > q:
                
                self.diccionario[grupo] = 0
                
                
        #reasignamos los Psi según los valores del diccionario
                
        for node in range(N):
            
            self.G.nodes[node]['Psi'] = self.diccionario[self.G.nodes[node]['group']]
            
        #asignamos los r
        
        for node in range(N):
            
            self.G.nodes[node]['r'] = topo* sum( [self.G.nodes[vecino]['Psi'] for vecino in self.G.neighbors(node)] )
       
        #cada nodo elige un vecino al azar y elige si asignar su grupo
        
        for node in range(N):
            
            lista = list(self.G.neighbors(node))
            
            vecino = np.random.choice(lista)

            if np.random.uniform() < sigmoide(anchura, self.G.nodes[node]['r']):
                
                self.G.nodes[node]['group'] = self.G.nodes[vecino]['group']
            
