# CS-GY 6513 Big Data Project

## Project Member (Group 6)

* Minghao Shao
* Haozhong Zheng
* Hanqing Zhang

## Project Description

In our daily life, we may encounter a huge number of datasets with different quality. In some datasets, values of certain attributes were missing while in some datasets, some values were incorrect in people's cognition. In which case data profiling and data cleaning
were necessary, which formed two main approaches in our project. In this project, we would use data profiling techniques, a process of validation on the data from available sources [1], to analyze the data structure, check the effectiveness of each data and inspect the defect of the data set hunted and mined by us. And we would apply our strategies to clean the defected data, starting from a specific assigned data set and extending them to multiple data sets we discovered.
We took the dataset "Citywide Payroll Data (Fiscal Year)" as our starting point, and mined the data sets provided by NYC OpenData Profiling and cleaning the potential low quality data and analyzing, visualizing them, and generating useful potential reference data.

In this project, we came up with the problems below:

* Starting from the dataset "Citywide Payroll Data (Fiscal
Year)", how can we find the datasets with overlap fields via
data hunting?
* How can we apply our data clean strategy to the datasets
we found?
* How well does our original data clean strategy work? What
more can we learn from these datasets or what's the differ-
ence between our original dataset and new datasets?
* How can we improve our strategy to increase the effective-
ness of data clean?
* How to generate reference data which could be used for
future data clean tasks?
* How to extend our strategies to all the datasets we may find?

After this project, we may be able to solve these problems.

## Approach

1. Abstracting datasets

First we would generate an abstract from all the datasets from data.cityofnewyork.us on the HPC server, incluing their filename and their columns

2. Hunting overlap datasets

We analysis the dataset abstract generated previously and measure the similarity on columns with our the dataset "Citywide Payroll Data (Fiscal Year)", finding potential datasets with overlap column.

3. Profiling & cleaning the data

We would profile the dataset with overlap we found, apply our data clean strategies. Due to the large scale of the data, we mainly focus on the columns which could generate some reference data, and dataset with high overlap rate with the dataset "Citywide Payroll Data (Fiscal Year)".

4. Analysis and visualise results

Finally we would analysis results of our data clean job, measuring the precision and recall and visualise our data before and after cleaning, by both our orignal strategies and our refined strategies.

## Tools And packages used

We use blend tools to do this project, both spark and jupyter

For spark, we use it to handle large scale of data, especially when we measured the similarity between different datasets. And we use jupyter to perform data profiling, cleaning and visualisation in the experiment. <br>

The platform on this project was spark on NYU PEEL HPC, and python with version 3.8 locally.

Below were the python packages used by us, they should be installed to reproduce the experiment:

1. openclean https://pypi.org/project/openclean/
2. pyspark https://pypi.org/project/pyspark/
3. Pandas https://pypi.org/project/pandas/

## Ways to reproduce

All the code were included in the directory jupyter_notebook and columns_overlap_src. These code should be able to run on HPC server and jupyter notebook with the same environment we used and generate corresponding results.

To generate a reproducable report, you will need the datasets below:

|  Dataset identifier   | Dataset name  |
|  ----  | ----  |
| bty7-2jhb  | Historical DOB Permit Issuance |
| ptev-4hud  | License Applications |
| hy4q-igkk  | 311 Service Requests for 2006 |
| aiww-p3af  | 311 Service Requests for 2007 |
| 3rfa-3xsf  | 311 Service Requests for 2009 |
| m6ad-jy3s  | FY18 BID Trends Report Data |
| emuv-tx7t  | FY17 BID Trends Report Data |
| gt6r-wh7c  | FY19 BID Trends Report Data |
| 8eq5-dtjb  | FY20 BID Trends Report Data |
| xrwg-eczf  | SCOUT CORE |
| un8d-rbed  | SBS ICAP Contract Opportunities - Historical |
| acdt-2zt9  | 2021 Open Data Plan: Future Releases |
| cwy2-px8b  | Local Law 8 of 2020 - Complaints of Illegal Parking of Vehicles Operated on Behalf of the City |
| wye7-nyek  | Interagency Coordination and Construction Permits Data (MOSYS) |

You can obtain these datasets either via PEEL or from NYC OpenData, rename the dataset as we specified in the jupyter notebook. <u>And you also should change the dataset directory in the jupyter notbook to fit your own data path, our suggestion was to create a folder called 'project_data' in the root folder, and put all datasets there.</u>

For jupyter notebook: <br>
You can run all the jupyter notebook programs in jupyter_notebook folder and generate the results we obtained from our experiment.<br>

For spark program: <br>
Though our results were included in the similarity_profiling folder, you can run the spark program in spark_src fold to generate columns abstract for large scale of datasets, you should run this program on NYU HPC server.

## Deliverables:

The Project Report and slides for presentation could be found in the deliverables directory.

## Contribution

The link below was our google drive project directory: <br>

https://drive.google.com/drive/folders/1Gmjduu2zaeupyAYgQPRpstCdkOa6LwVy?usp=sharing

Please request for permission if you want to view this.
