import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import format_string, date_format
from decimal import *


def jaccard_similarity(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return intersection, union, list(set(list1).intersection(list2))

ds_name = 'k397-673e'

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

file_list_path = 'file_list.txt'

spark = SparkSession.builder.enableHiveSupport().getOrCreate()

schema = StructType([
    StructField("filename", StringType(), True),
    StructField("num_intersection", IntegerType(), True),
    StructField("num_union", IntegerType(), True),
    StructField("similarity", StringType(), True),
    StructField("intersection_columns", StringType(), True)])
df_result = spark.createDataFrame([], schema)

file_df = spark.read.text(file_list_path)
file_list = file_df.select('value').collect()

for i in file_list:
    abs_name = i.asDict().get('value')
    if len(abs_name) == 0:
        continue
    filename = sys.argv[1] + '/' + abs_name
    data_set = spark.read.format('csv').options(header='true', inferschema='false').load(filename).limit(1)
    inter, uni, cols = jaccard_similarity(COLUMNS, data_set.columns)
    sim = Decimal(str(inter * 1.0 / uni * 1.0))
    if sim > 0.0:
        newRow = spark.createDataFrame([(abs_name, inter, uni, str(sim.quantize(Decimal('0.0000'))), '|'.join(cols))], schema)
        df_result = df_result.union(newRow)

df_result.select(format_string("%s\t %d, %d, %s, %s", df_result.filename, df_result.num_intersection, df_result.num_union, df_result.similarity, df_result.intersection_columns)).write.save('similarity_result.out', format="text")
# df_result.select("*").write.save('similarity_result.out', format="csv")

spark.stop()
