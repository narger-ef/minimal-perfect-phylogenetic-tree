# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:46:09 2020

@author: loren
"""

import numpy as np

def sort_by_ones_on_columns(m):
    m_t = np.transpose(m)
    
    cont = {}
    index = 0
    
    for r in m_t:
        cont[index] = (np.sum(r))
        index += 1
        
    order = sorted(cont, key=cont.get, reverse=True)

    m_t_ordered = []
    
    for row in range(0, np.size(m_t, 0)):
        m_t_ordered.append(m_t[order[row]].tolist())
        
    return np.transpose(m_t_ordered)

def build_auxiliary_matrix(m):
    L = np.zeros((m.shape[0], m.shape[1])).astype(int)
    
    for i in range(0, m.shape[0]):
        k = -1
        for j in range(0, m.shape[1]):
            if m[i][j] == 1:
                L[i][j] = k
                k = j + 1
                
    return L
                
                
def is_laminar(m):
    L = build_auxiliary_matrix(m)
    
    for col in np.transpose(L):
        not_zero = 0
        for el in col:
            if el != 0:
                if not_zero == 0:
                    not_zero = el
                elif not_zero != el:
                    return False
                
    return True