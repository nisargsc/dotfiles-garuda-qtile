#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
run lxsession &
run sxhkd &
run nm-applet &
run pamac-tray &
run numlockx on &
run blueman-applet &
run picom --config $HOME/.config/picom/picom-jonaburg.conf --experimental-backends &
run dunst &

#starting user applications at boot time
nitrogen --restore &
$HOME/.config/polybar/launch.sh &

run /usr/lib/kdeconnectd &
