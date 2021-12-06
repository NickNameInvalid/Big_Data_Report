# CS-GY 6513 Big Data Project

## Project Member (Group 6)

* Minghao Shao
* Haozhong Zheng
* Hanqing Zhang

## Project Description

In our daily life, we may encounter a huge number of datasets with different quality. In some datasets, values of certain attributes were missing while in some datasets, some values were incorrect in people's cognition. In which case data profiling and data cleaning were necessary. In this project, we took the dataset "Citywide Payroll Data (Fiscal Year)" as our starting point, and mining the data privided by data.cityofnewyork.us webpage. Profiling and cleaning the portential low quality data and analysising them. From our data mining procedure, we may achieve the objects below:

1. Finding the dataset which has overlap columns with our starting point with some similarity techniques.

2. Profiling some typical datasets, spoting out the defects of these dataset and applying our data clean methods to them.

3. Compare the data we spoted out with the overlap column in our starting point with some analysising approaches.

4. Generate our own reference data from the starting point and contributing them

5. Create an experiment report, including what we did, what we found in these datasets and described the effectiveness of our data cleaning and try to extend our approaches to all the datasets.

## Approach

1. Abstracting datasets

First we would generate an abstract from all the datasets from data.cityofnewyork.us on the HPC server, incluing their filename and their columns

2. Hunting overlap datasets

We analysis the dataset abstract generated previously and measure the similarity on columns with our the dataset "Citywide Payroll Data (Fiscal Year)", finding potential datasets with overlap column.

3. Profiling & cleaning the data

We would profile the dataset with overlap we found, apply our data clean strategies. Due to the large scale of the data, we mainly focus on the columns which could generate some reference data, and dataset with high overlap rate with the dataset "Citywide Payroll Data (Fiscal Year)".

4. Analysis results

Finally we would analysis results of our data clean job, measure the effectiveness and 

## Ways to reproduce

Since all the datasets was in the HPC server, all of our data in the report was generated with pyspark.
All the code were included in the directory similarity_profiling, data_profiling_src, data_clean_src. All code should be able to run on a spark server and generate corresponding results.

## Deliverables:

The Project Report could be found in the report directory.

LaTeX url:
https://www.overleaf.com/project/61a15af0366826d08ffc386a
