#!/bin/bash

poweroff_text="[1]  Power Off"
reboot_text="[2]  Restart"
lock_text="[3]  Lock"
logout_text="[4] 﫼 Log Out"

chosen=$(echo -e "$poweroff_text\n$reboot_text\n$lock_text\n$logout_text" | rofi -dmenu -i -p "Power Menu:")

if [[ $chosen = $poweroff_text ]]; then
	shutdown now
elif [[ $chosen = $reboot_text ]]; then
	reboot
elif [[ $chosen = $lock_text ]]; then
	betterlockscreen -l blur
elif [[ $chosen = $logout_text ]]; then
	pkill -KILL -u $USER
fi

