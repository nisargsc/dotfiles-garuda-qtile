#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}



#starting utility applications at boot time
lxsession &
run nm-applet &
run pamac-tray &
numlockx on &
blueman-applet &
#picom --config $HOME/.config/picom/picom.conf &
picom --config .config/picom/picom-jonaburg.conf --experimental-backends &
# dunst &

#starting user applications at boot time
run volumeicon &
nitrogen --restore &
run /usr/lib/kdeconnectd &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
