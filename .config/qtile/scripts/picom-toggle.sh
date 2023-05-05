#!/bin/bash
if pgrep -x "picom" > /dev/null
then
	killall picom
else
	#picom -b --config ~/.config/picom/picom-ibhagwan.conf
	picom -b --config ~/.config/picom/picom-jonaburg.conf
	#picom -b --config ~/.config/picom/picom-pijulius.conf
fi
