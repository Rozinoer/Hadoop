all:
	/usr/local/Cellar/hadoop/3.3.1/bin/hadoop jar /usr/local/Cellar/hadoop/3.3.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
	-file ~/Desktop/MapReduce/stripes/countMap.py -mapper ~/Desktop/MapReduce/stripes/countMap.py \
	-file ~/Desktop/MapReduce/stripes/countReduce.py -reducer ~/Desktop/MapReduce/stripes/countReduce.py \
	-input /MapReduce/file*  -output /MapReduce/output/stripes