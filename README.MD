# Data Extractor

This is a is a Python script that lets you graph data based on CSV file data points.


```bash
input: CSV Files containing data points
output: PDF files containing plotted graphs 
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install missing libraries.

```bash
pip install matplotlib
pip install pandas
pip install numpy
```

## Usage

Preconditions: CSV files must have "DateTime" , and "Process Value" columns.
DateTime column must have the following data format: "%H:%M:%S.%f %Y-%m-%d"

To use,drop in your CSV files into the same directory of the scripts, and run it as you would run any python script. the results should be pdf files containing graph data.
```bash
 C:\Users\Christian\Documents\IO> python .\platinum_graph_rev1.py
```
