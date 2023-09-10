#!/bin/sh

# Send notification
notify() {
current_brightness=$1
/usr/bin/notify-send "Brightness: $current_brightness%" -h int:value:$current_brightness -r 9990
}

# Decrease the brightness
decrease_brightness() {
  brightness=$(/usr/bin/brightnessctl s 1%- | grep "Current brightness" | awk -F '[(%)]' '{print $2}')
  notify "$brightness"
}

# Increase the brightness
increase_brightness() {
  brightness=$(/usr/bin/brightnessctl s 1%+ | grep "Current brightness" | awk -F '[(%)]' '{print $2}')
  notify "$brightness"
}

# Get current brightness
get_brightness() {
  brightness=$(/usr/bin/brightnessctl i | grep "Current brightness" | awk -F '[(%)]' '{print $2}')
  notify "$brightness"
}

# Main script
case "$1" in
  dec)
    decrease_brightness
    ;;
  inc)
    increase_brightness
    ;;
  get)
    get_brightness
    ;;
  *)
    ;;
esac
