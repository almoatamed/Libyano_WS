#!/bin/bash

echo $1
coproc bluetoothctl
echo -e 'connect '$1' \n exit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]})
pactl set-sink-volume @DEFAULT_SINK@ 100%
echo $output

