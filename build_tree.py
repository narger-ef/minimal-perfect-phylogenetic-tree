# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:46:09 2020

@author: loren
"""

import numpy as np
import sys
import laminar_tools as tools
from anytree import Node, RenderTree

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def has_children(node, child_name):
    for el in node.children:
        if child_name in el.name:
            return True
    return False

def get_children_with(node, child_name):
    for el in node.children:
        if child_name in el.name:
            return el
    return None


recursive_state = ""

def fix_problem(root) :
    global recursive_state
    for el in root.children:
        fix_problem(el)
        if '○' in el.name:
            el.name = recursive_state
            recursive_state += " "
            
    return root
            

def generate_leaves(root):
    for el in root.children:
        generate_leaves(el)
        p = list(find_all(el.name, 'fine_'))
        for pos in p:
            pos += len('fine_')
            Node(el.name[pos : pos + 1], parent = el)
        el.name = "○"
        
def build_tree(m):
    root = Node("R")
    
    row_index = 1
    col_index = 1
    
    for row in m:
        current_node = root
        for el in row:
            if el == 1:
                if has_children(current_node, str(col_index)) == False:
                    u = Node("c" + str(col_index), parent=current_node)
                    current_node = u
                else:
                    current_node = get_children_with(current_node, str(col_index))
            col_index += 1
        
        current_node.name += 'fine_' + str(row_index)
       
        row_index += 1
        col_index = 1
    
    generate_leaves(root)
                
    return root
    
def show_tree(tree):
    for pre, fill, node in RenderTree(tree):
        print("%s%s" % (pre, node.name))
    
    
    
    try:
        from anytree.exporter import DotExporter
        # graphviz needs to be installed for the next line!
        # there is a bug in anytree, all the nodes with the same name (in our case the '○' nodes)
        # are all treated as one, therefore we will change these names as backspace strings long 1, 2, etc.

        DotExporter(fix_problem(tree)).to_picture("tree.png")
    except:
        print('Could not draw the tree, make sure graphviz is installed!')

def main():
    if len(sys.argv) == 1:
        raise Exception("Insert a csv matrix as argument")
        
    matrix = np.array(np.loadtxt(open(sys.argv[1], "rb"), delimiter=";", skiprows=1), dtype=int)
    matrix = tools.sort_by_ones_on_columns(matrix)
    
    if not(tools.is_laminar(matrix)):
        raise Exception("Input matrix is not laminar")
        
    tree = build_tree(tools.sort_by_ones_on_columns(matrix))
    show_tree(tree)
    
if __name__ == "__main__":
    main()

