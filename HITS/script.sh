 #!/bin/bash
 itr_count=4
 for ((itr=1; itr <= $itr_count; itr++)); do
     echo "Doing iteration $itr of $itr_count..."
      /usr/local/Cellar/hadoop/3.3.1/bin/hadoop jar \
      /usr/local/Cellar/hadoop/3.3.1/libexec/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
       -input /step$((itr))/input -output /step$((itr + 1))/input \
       -file $(pwd)/step$((itr))/Mapper.py -mapper $(pwd)/step$((itr))/Mapper.py \
       -file $(pwd)/step$((itr))/Reducer.py -reducer $(pwd)/step$((itr))/Reducer.py \
 done
 hdfs dfs -cat //step$((4))/input/part-00000

#itr_count=4
#for ((itr=1; itr <= $itr_count; itr++)); do
#    echo "Doing iteration $itr of $itr_count..."
#    cat $(pwd)/step$((itr))/input | python3 $(pwd)/step$((itr))/Mapper.py | \
#    sort | python3 $(pwd)/step$((itr))/Reducer.py > $(pwd)/step$((itr + 1))/input
#done
#cat $(pwd)/step$((1))/input > $(pwd)/step$((5))/update
#cat $(pwd)/step$((5))/input >> $(pwd)/step$((5))/update
#cat $(pwd)/step$((5))/update |sort| \
#python3 $(pwd)/step$((5))/updateMapper.py > $(pwd)/step$((1))/input
#rm -rf $(pwd)/step$((5))/updaten
#
#
