import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import format_string, upper

COLUMN = 'Borough Location'

FILE_NAME = '../project_data/data-cityofnewyork-us.xeg4-ic28.csv'
#FILE_NAME = '/user/CS-GY-6513/project_data/data-cityofnewyork-us.' + sys.argv[1] + '.csv'

spark = SparkSession.builder.enableHiveSupport().getOrCreate()

ds_full = spark.read.format('csv').options(header='true', inferschema='true').load(FILE_NAME)

res = ds_full.select("*").withColumn(COLUMN, upper(col=COLUMN)).fillna(subset=COLUMN, value='OTHER')
# a = res.filter(res[COLUMN] == 'BRONX')
# a.show()
# res.show()
#res.select(format_string("%s\t%d", res.borough, res.number_count)).write.save("borough_pro.out", format="text")

spark.stop()