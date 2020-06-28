# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:46:09 2020

@author: loren
"""

import numpy as np
import sys
import laminar_tools as tools
    
def main():
    matrix = np.array(np.loadtxt(open(sys.argv[1], "rb"), delimiter=";", skiprows=1), dtype=int)
    matrix = tools.sort_by_ones_on_columns(matrix)
    
    if not(tools.is_laminar(matrix)):
        raise Exception("Input matrix is not laminar")
    
if __name__ == "__main__":
    main()

