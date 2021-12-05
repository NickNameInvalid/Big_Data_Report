import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import format_string, date_format
from decimal import *
from pyspark.sql.functions import col
import pyspark.sql.functions as func

original_ds_name = 'data-cityofnewyork-us.k397-673e.csv'

COLUMNS = [
    "Fiscal Year",
    "Payroll Number",
    "Agency Name",
    "Last Name",
    "First Name",
    "Mid Init",
    "Agency Start Date",
    "Work Location Borough",
    "Title Description",
    "Leave Status as of June 30",
    "Base Salary",
    "Pay Basis",
    "Regular Hours",
    "Regular Gross Paid",
    "OT Hours",
    "Total OT Paid",
    "Total Other Pay"
]


def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    sim = 0.0 if union == 0 else Decimal(str(intersection * 1.0 / union * 1.0))
    return sim


def parse_overlap_line(line):
    l_line = line.strip('\n').split('\t', 1)
    filename = l_line[0]
    cols = l_line[1].split('\t')
    overlap_cols = []
    for col in cols:
        col_names = col.split(',')
        overlap_cols.append((col_names[0], col_names[1]))
    return filename, overlap_cols


spark = SparkSession.builder.enableHiveSupport().getOrCreate()

overlap = []
file_df = spark.read.text('sim_columns.txt')
file_list = file_df.select('value').collect()

for i in file_list:
    line = i.asDict().get('value')
    if len(line) == 0:
        continue
    overlap.append(parse_overlap_line(line))

schema = StructType([
    StructField("filename", StringType(), True),
    StructField("sim_columns", StringType(), True)])
df_result = spark.createDataFrame([], schema)

for ds in overlap:
    filepath = sys.argv[1] + '/' + ds[0]
    sim_cols = ds[1]
    data_set = spark.read.format('csv').options(header='true', inferschema='false').load(filepath)
    pivot_ds = spark.read.format('csv').options(header='true', inferschema='false').load(sys.argv[1] + '/' + original_ds_name)
    result = ""
    # print(sim_cols)
    for sim_col in sim_cols:
        list1 = data_set.select(data_set[sim_col[0]]).distinct().rdd.flatMap(lambda x: x).collect()
        list2 = pivot_ds.select(pivot_ds[sim_col[1]]).distinct().rdd.flatMap(lambda x: x).collect()
        sim = jaccard_similarity(list1, list2).quantize(Decimal('0.0000'))
        result += "(" + sim_col[0] + '-' + sim_col[1] + '): ' + str(sim) + ' '
        # result = str(jaccard_similarity(list1, list2).quantize(Decimal('0.0000')))
        # list1 = data_set.select(data_set[sim_col[0]]).distinct().flatMap(lambda x: x).collect()
        # list2 = pivot_ds.select(pivot_ds[sim_col[1]]).distinct().flatMap(lambda x: x).collect()
#         result += f"({sim_col[0]}, {sim_col[1]}, {str(jaccard_similarity(list1, list2).quantize(Decimal('0.0000')))}) "
#     new_row = spark.createDataFrame([(ds[0], result)], schema)
#     df_result = df_result.union(new_row)
    if result != "":
        new_row = spark.createDataFrame([(ds[0], result)], schema)
        df_result = df_result.union(new_row)

df_result.select(format_string("%s\t %s", df_result.filename, df_result.sim_columns)).write.save('test.out', format="text")
spark.stop()

