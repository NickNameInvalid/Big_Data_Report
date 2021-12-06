# import sys
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import format_string, upper, desc
# from pyspark.sql import functions as sf
# from pyspark.sql.functions import udf
# from pyspark.sql.types import BooleanType
#
# COLUMN = 'Park Borough'
#
FILE_NAME = '../project_data/data-cityofnewyork-us.sxmw-f24h.csv'
# #FILE_NAME = '/user/CS-GY-6513/project_data/data-cityofnewyork-us.' + sys.argv[1] + '.csv'
#
# spark = SparkSession.builder.enableHiveSupport().getOrCreate()
#
# ds_full = spark.read.format('csv').options(header='true', inferschema='true').load(FILE_NAME)
#
# res_borough = ds_full.select(ds_full[COLUMN]).groupby(COLUMN).count().withColumnRenamed("count", "number_count").withColumnRenamed(COLUMN, 'borough').distinct()
# res_agency = ds_full.select(ds_full['Agency Name']).groupby('Agency Name').count().withColumnRenamed("count", "number_count").withColumnRenamed('Agency Name', 'agency').distinct().orderBy(desc('number_count'))
# upp = udf(lambda x: x.islower() if x != None else False, BooleanType())
# res_b = ds_full.select(ds_full['Agency Name']).filter(ds_full['Agency Name'].isNull()).count()
# print(res_b)
# # res_borough.show()
# # res_agency.show()
# #res.select(format_string("%s\t%d", res.borough, res.number_count)).write.save("borough_pro.out", format="text")
#
# spark.stop()

import os

from openclean.pipeline import stream

df = stream(FILE_NAME)
dba = df.select('Agency Name').distinct()
print('{} distinct bisiness names (for {} total values)'.format(len(dba), sum(dba.values())))

from openclean.cluster.knn import knn_clusters
from openclean.function.similarity.base import SimilarityConstraint
from openclean.function.similarity.text import LevenshteinDistance
from openclean.function.value.threshold import GreaterThan

# Minimum cluster size. Use ten as default (to limit
# the number of clusters that are printed in the next cell).
minsize = 3

clusters = knn_clusters(
    values=dba,
    sim=SimilarityConstraint(func=LevenshteinDistance(), pred=GreaterThan(0.9)),
    minsize=minsize
)

print('{} clusters of size {} or greater'.format(len(clusters), minsize))

def print_cluster(cnumber, cluster):
    print('Cluster {} (of size {})\n'.format(cnumber, len(cluster)))
    for val, count in cluster.items():
        print('{} ({})'.format(val, count))
    print('\nSuggested value: {}\n\n'.format(cluster.suggestion()))

# Sort clusters by decreasing number of distinct values.
clusters.sort(key=lambda c: len(c), reverse=True)

for i, cluster in enumerate(clusters):
    print_cluster(i + 1, cluster)

from collections import Counter

from openclean.cluster.knn import knn_collision_clusters

clusters = knn_collision_clusters(
    values=dba,
    sim=SimilarityConstraint(func=LevenshteinDistance(), pred=GreaterThan(0.9)),
    minsize=minsize
)

print('{} clusters of size {} or greater'.format(len(clusters), minsize))
# Print resulting clusters.

clusters.sort(key=lambda c: len(c), reverse=True)

for i, cluster in enumerate(clusters):
    print_cluster(i + 1, cluster)
