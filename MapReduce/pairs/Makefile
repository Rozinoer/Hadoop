all:
	/usr/local/Cellar/hadoop/3.3.1/bin/hadoop jar /usr/local/Cellar/hadoop/3.3.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
	-file ~/Desktop/MapReduce/pairs/countMap.py -mapper ~/Desktop/MapReduce/pairs/countMap.py \
	-file ~/Desktop/MapReduce/pairs/countReduce.py -reducer ~/Desktop/MapReduce/pairs/countReduce.py \
	-input /MapReduce/file*  -output /MapReduce/output/pairs