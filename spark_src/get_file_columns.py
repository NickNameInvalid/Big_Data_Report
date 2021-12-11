import sys
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
spark = SparkSession.builder.getOrCreate()


if __name__ == '__main__':
    file_list_path = 'file_list.txt'
    file_df = spark.read.text(file_list_path)
    file_list = file_df.select('value').collect()

    file_columns = []

    for i in file_list:
        abs_name = i.asDict().get('value')
        if len(abs_name) == 0:
            continue
        filename = '/user/CS-GY-6513/project_data/' + abs_name
        data_set = spark.read.format('csv').options(header='true', inferschema='false').load(filename).limit(1)
        row = '{}\t{}'.format(abs_name, ','.join(data_set.columns))
        file_columns.append((row,))
    
    df = spark.createDataFrame(file_columns, ['text'])
    df.write.save('file_columns.out', format='text')