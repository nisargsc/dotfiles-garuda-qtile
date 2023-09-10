import os
import subprocess
from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from typing import List

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')

myTerm = "alacritty" # My terminal of choice


@lazy.function
def lazy_move_mouse_to_current_window(qtile):
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/move-mouse-to-current-window.sh'])

bindings:List[Key|KeyChord] = [
        # SUPER + FUNCTION KEYS

        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod], "v", lazy.spawn('pavucontrol')),
        Key([mod], "d", lazy.spawn('rofi -show drun')),
        Key([mod], "b", lazy.spawn('brave --profile-directory=Default'), desc="Open browser in default profile"),
        #Key([mod], "Escape", lazy.spawn('xkill')),
        Key([mod], "Return", lazy.spawn(myTerm)),
        Key([mod], "KP_Enter", lazy.spawn(myTerm)),
        Key([mod], "x", lazy.shutdown()),
        Key([mod], "period", 
            lazy.next_screen(), 
            lazy_move_mouse_to_current_window(),
            desc='Move Focus to next monitor'
            ),

        # SUPER + SHIFT KEYS

        # Key([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
        # Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
        Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
        # Key([mod, "shift"], "d", lazy.spawn('nwggrid -p -o 0.4')),
        Key([mod, "shift"], "q", lazy.window.kill()),
        Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
        Key([mod, "shift"], "x", lazy.spawn(home + '/.config/qtile/scripts/rofi-power-menu.sh')),

        # SUPER + CONTROL KEYS
        Key([mod, "control"], "r", lazy.reload_config(), desc="reload qtile config"),
        Key([mod, "control"], "Escape", lazy.spawn('betterlockscreen -l blur --time-format "%I:%M %p" --off 60 -q'), desc="Lock the screen"),
        # CONTROL + ALT KEYS

        Key(["mod1", "control"], "space", lazy.widget["keyboardlayout"].next_keyboard(), desc="Change keyboard layout"),
        Key(["mod1", "control"], "o", lazy.spawn(home + '/.config/qtile/scripts/picom-toggle.sh')),
        Key(["mod1", "control"], "t", lazy.spawn('xterm')),
        Key(["mod1", "control"], "u", lazy.spawn('pavucontrol')),

        # ALT + ... KEYS

        Key(["mod1"], "p", lazy.spawn('pamac-manager')),
        Key(["mod1"], "f", lazy.spawn('firedragon')),
        Key(["mod1"], "m", lazy.spawn('pcmanfm')),
        Key(["mod1"], "w", lazy.spawn('garuda-welcome')),
        Key(["mod1"], "space", lazy.spawn('playerctl play-pause')),

    # Music control
        KeyChord(["mod1"], "m", [
            Key([], "j", lazy.spawn("playerctl previous")),
            Key([], "k", lazy.spawn("playerctl play-pause")),
            Key([], "l", lazy.spawn("playerctl next")),
            Key([], ";", lazy.spawn("playerctl stop")),
            ]),


    # CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),


    # SCREENSHOTS

    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),

    # MULTIMEDIA KEYS

    # INCREASE/DECREASE BRIGHTNESS
    Key([], "XF86MonBrightnessUp", lazy.spawn(home+'/.config/qtile/scripts/brightness.sh inc')),
    Key([], "XF86MonBrightnessDown", lazy.spawn(home+'/.config/qtile/scripts/brightness.sh dec')),

    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn(home+'/.config/qtile/scripts/volume.sh mute')),
    Key([], "XF86AudioLowerVolume", lazy.spawn(home+'/.config/qtile/scripts/volume.sh dec')),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(home+'/.config/qtile/scripts/volume.sh inc')),

    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),


    # POWER MENU
    Key([], "XF86Poweroff", lazy.spawn(home + '/.config/qtile/scripts/rofi-power-menu.sh')),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "m", lazy.layout.maximize()),
    Key([mod], "space", lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], "Up", 
        lazy.layout.up(),
        lazy_move_mouse_to_current_window(),
        ),
    Key([mod], "Down", 
        lazy.layout.down(),
        lazy_move_mouse_to_current_window(),
        ),
    Key([mod], "Left", 
        lazy.layout.left(),
        lazy_move_mouse_to_current_window(),
        ),
    Key([mod], "Right", 
        lazy.layout.right(),
        lazy_move_mouse_to_current_window(),
        ),

    Key([mod], "k", 
        lazy.layout.up(),
        lazy_move_mouse_to_current_window(),
        ),
    Key([mod], "j", 
        lazy.layout.down(),
        lazy_move_mouse_to_current_window(),
        ),
    Key([mod], "h", 
        lazy.layout.left(),
        lazy_move_mouse_to_current_window(),
        ),
    Key([mod], "l", 
        lazy.layout.right(),
        lazy_move_mouse_to_current_window(),
        ),


    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

         ### Treetab controls
    Key([mod, "control"], "k",
        lazy.layout.section_up(),
        desc='Move up a section in treetab'
        ),
    Key([mod, "control"], "j",
        lazy.layout.section_down(),
        desc='Move down a section in treetab'
        ),



    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
]
