#!/bin/sh

# Send Notification
notify() {
  case "$2" in
    off)
      /usr/bin/notify-send "Volume: $1% [Mute]" -h int:value:$1 -r 9991
      ;;
    on)
      /usr/bin/notify-send "Volume: $1%" -h int:value:$1 -r 9991
      ;;
    *)
      /usr/bin/notify-send "Volume: $1%" -h int:value:$1 -r 9991
      ;;
  esac
}

# Decrease the volume by 5%
decrease_vol() {
  mixer_out=$(/usr/bin/amixer set Master 1%-)
  vol=$(echo "$mixer_out" | grep "Front Left:" | awk -F '[][%]' '{print $2}')
  status=$(echo "$mixer_out" | grep "Front Left:" | awk -F '[][]' '{print $4}')
  notify "$vol" "$status"
}

# Increase the brightness by 5%
increase_vol() {
  mixer_out=$(/usr/bin/amixer set Master 1%+)
  vol=$(echo "$mixer_out" | grep "Front Left:" | awk -F '[][%]' '{print $2}')
  status=$(echo "$mixer_out" | grep "Front Left:" | awk -F '[][]' '{print $4}')
  notify "$vol" "$status"
}

toggle_mute() {
  mixer_out=$(/usr/bin/amixer set Master toggle)
  vol=$(echo "$mixer_out" | grep "Front Left:" | awk -F '[][%]' '{print $2}')
  status=$(echo "$mixer_out" | grep "Front Left:" | awk -F '[][]' '{print $4}')
  notify "$vol" "$status"
}

# Main script
case "$1" in
  dec)
    decrease_vol
    ;;
  inc)
    increase_vol
    ;;
  mute)
    toggle_mute
    ;;
  *)
    ;;
esac
