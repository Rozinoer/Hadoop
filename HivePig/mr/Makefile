all:
	/usr/local/Cellar/hadoop/3.3.1/bin/hadoop jar /usr/local/Cellar/hadoop/3.3.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
	-file /Users/evgenii/Desktop/HivePig/mr/countMap.py -mapper /Users/evgenii/Desktop/HivePig/mr/countMap.py \
	-file /Users/evgenii/Desktop/HivePig/mr/countReduce.py -reducer /Users/evgenii/Desktop/HivePig/mr/countReduce.py \
	-input /user/hive/warehouse/creditdata/creditData.txt  -output /user/hive/output