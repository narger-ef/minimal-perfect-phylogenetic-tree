# Perfect Phylogenetic tree
This tool helps you to build a simple Perfect Phylogenetic tree given a binary matrix:

## Input files:
- Binary matrix in .csv format with ";" as delimiter (demonstration matrixes given in 'examples' folder) <br />
N.B. First row will be ignored (treated as header)

## How to run - Prepare:
Running the tool is pretty easy, first of all install the dependencies:
```
pip install -r requirements.txt
```

### Optional - Graphwiz
You can install *graphwiz* that is used in order to plot the tree (assuming you are running a Linux system):
```
sudo apt install graphviz
```
Note that this is optional, if you will not install it the tree will only be generated in console, otherwise a file named *tree.png* will be created in the same directory of the script

## How to run - Launch:
After that, run the tool by using this command:
```
python build_tree.py *matrix-file.csv*
```
Of course replace *matrix_file.csv* with the name of your input.
For example you can use a given matrix for demonstration:
```
python build_tree.py examples/laminar.csv
```

## Results
Using an example matrix as input (examples/laminar.csv) the output in the console will be:
```
R
├── ○
│   ├── ○
│   │   ├── ○
│   │   │   └── 2
│   │   └── 4
│   └── 1
└── ○
    ├── ○
    │   └── 5
    └── 3
```
