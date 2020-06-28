# Perfect Phylogenetic tree
This tool helps you to build a simple Perfect Phylogenetic tree given a binary matrix:

## Input files:
- Binary matrix in .csv format with ";" as delimiter (demonstration matrixes given in 'examples' folder)

## How to run:
Running the tool is pretty easy, first of all install the dependencies:
```
pip install -r requirements.txt
```
This will install 'numpy' and 'anytree' packages.

After that, run the tool by using this command:
```
python build_tree.py *matrix-file.csv*
```
Of course replace *matrix_file.csv* with the name of your input.
For example you can use a given matrix for demonstration:
```
python build_tree.py examples/laminar.csv
```
