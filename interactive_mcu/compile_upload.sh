cd $HOME/catkin_ws/src/interactive_mcu/src/interactive_mcu/.
$HOME/catkin_ws/src/third_party/Arduino/arduino-cli compile -b arduino:sam:arduino_due_x_dbg --build-path $HOME/catkin_ws/src/interactive_mcu/build/. 
# export arduino_due=`find /dev/serial/by-id  -maxdepth 1 -name "*Due*" -print | head -n 1`
# $HOME/catkin_ws/src/third_party/Arduino/arduino-cli upload -b arduino:sam:arduino_due_x_dbg --input-dir $HOME/catkin_ws/src/interactive_mcu/build/. -p `readlink -f $arduino_due` 
