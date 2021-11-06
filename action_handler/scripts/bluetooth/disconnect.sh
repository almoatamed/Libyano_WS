#!/bin/bash

coproc bluetoothctl
echo -e 'disconnect\nexit' >&${COPROC[1]}
output=$(cat <&${COPROC[0]})
echo $output
