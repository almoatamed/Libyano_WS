cd $HOME/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/.
$HOME/catkin_ws/src/third_party/Arduino/arduino-cli compile -b arduino:avr:uno  --build-path $HOME/catkin_ws/src/interactive_mcu_2/build/. 
export arduino_due=`find /dev/serial/by-id  -maxdepth 1 -name "*__0043_55834323832351A0E1A2*" -print | head -n 1`
$HOME/catkin_ws/src/third_party/Arduino/arduino-cli upload -b arduino:avr:uno  --input-dir $HOME/catkin_ws/src/interactive_mcu_2/build/. -p `readlink -f $arduino_due` 
