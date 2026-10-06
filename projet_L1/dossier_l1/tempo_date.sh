
while:
do
     date=$(date)  
     temp=$(cat/sys/class/hwmon/hwmon0/temp2_input)
     temp=$(($temp/1000))
     echo $date $temp >> $HOME/log
     sleep1
done

















