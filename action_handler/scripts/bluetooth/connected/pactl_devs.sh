export pactl_devs_list2="`pactl list | grep -A2 'Source #' | grep 'Name: ' | cut -d" " -f2`"
echo $pactl_devs_list2 >> 'sinks.txt'
