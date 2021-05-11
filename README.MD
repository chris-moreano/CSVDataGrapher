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
 An Example of a CSV file: 
DateTime,Process Value,Process Setpoint,PID 1,PID 2,Setpoint 1,Setpoint 2
11:12:52.192 2021-02-24,68.67416,68.88333,3.904791,2.091675,162,162
11:12:53.175 2021-02-24,68.68855,68.98053,4.835285,3.029022,162,162
11:12:54.176 2021-02-24,68.75063,69.07773,4.845632,3.27095,162,162
11:12:55.192 2021-02-24,68.77075,69.17493,5.409329,4.041748,162,162
11:12:56.193 2021-02-24,68.7926,69.28185,5.676832,4.576721,162,162
11:12:57.193 2021-02-24,68.8271,69.37904,6.348334,5.422211,162,162
11:12:58.194 2021-02-24,68.8576,69.47624,7.036153,6.307678,162,162
11:12:59.173 2021-02-24,68.95073,69.56372,6.832502,6.348419,162,162
11:13:00.967 2021-02-24,69.04156,69.73868,7.259057,6.97113,162,162
11:13:01.309 2021-02-24,69.09273,69.76784,6.958975,6.751099,162,162
 
```
