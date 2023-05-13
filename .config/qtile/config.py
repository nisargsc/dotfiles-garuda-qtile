# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import os
import subprocess
from typing import List
from libqtile import layout, bar, hook, qtile, widget
from libqtile.config import  Drag, DropDown, Group, Key, KeyChord, Match, ScratchPad, Screen 
from libqtile.command import lazy
#from qtile_extras import widget
#from qtile_extras.widget.decorations import PowerLineDecoration
import theme

#mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')


#colors
white="#ffffff"
black="#000000"
#font_color=white
#font_color2="#f4c2c2"
#bg_color="#2F343F"
#shadow_color="#4c566a"

#primary_color="#e75480"
#primary_color="#2aa899"
#primary_color="#abb2bf"
#primary_color="#81a1c1"
#primary_color="#56b6c2"
#primary_color="#b48ead"
#primary_color="#e06c75"
#primary_color="#fb9f7f"
#primary_color="#ffd47e"
#primary_color="#1EA3AA"

#secondary_color="#b48ead"

bg_transparent='#1b2b3400'
bg_color="#383838"
bg_color="#150A0E"
bg_color2="#928374"
bg_color2="#8A4153"
shadow_color="#888888"
#font_color="#d8dee9"
font_color=white
secondary_color="#f07f85"
primary_color="#5fb3b3" if ((theme.primary_color=="") or (theme.primary_color==None)) else theme.primary_color

normal_font="NotoSerif Nerd Font"
bold_font= normal_font + " Bold"

@lazy.function
def primary_colorpicker(qtile):
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/primary_colorpicker.sh'])

def move_mouse_to_current_window():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/move-mouse-to-current-window.sh'])

@lazy.function
def lazy_move_mouse_to_current_window(qtile):
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/move-mouse-to-current-window.sh'])

@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

myTerm = "alacritty" # My terminal of choice

keys:List[Key|KeyChord] = [
        # SUPER + FUNCTION KEYS

        Key([mod], "f", lazy.window.toggle_fullscreen()),
        Key([mod], "q", lazy.window.kill()),
        Key([mod], "t", lazy.spawn('alacritty')),
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

        Key([mod, "shift"], "Return", lazy.spawn('pcmanfm')),
        #    Key([mod, "shift"], "d", lazy.spawn("dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
        #    Key([mod, "shift"], "d", lazy.spawn(home + '/.config/qtile/scripts/dmenu.sh')),
        Key([mod, "shift"], "d", lazy.spawn('nwggrid -p -o 0.4')),
        Key([mod, "shift"], "q", lazy.window.kill()),
        Key([mod, "shift"], "r", lazy.restart(), desc="Restart qtile"),
        Key([mod, "shift"], "x", lazy.spawn(home + '/.config/qtile/scripts/rofi-power-menu.sh')),

        # SUPER + CONTROL KEYS
        Key([mod, "control"], "r", lazy.reload_config(), desc="reload qtile config"),
        Key([mod, "control"], "Escape", lazy.spawn('betterlockscreen -l blur --time-format "%I:%M %p" --off 60 -q'), desc="Lock the screen"),
        Key([mod, "control"], "t", 
            primary_colorpicker(),
            lazy.reload_config(),
            desc="Colorpicker for primary_color"
            ),
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


# CONTROL + SHIFT KEYS

    Key([mod2, "shift"], "Escape", lazy.spawn('lxtask')),


# SCREENSHOTS

    Key([], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
    Key([mod2], "Print", lazy.spawn('flameshot full -p ' + home + '/Pictures')),
#    Key([mod2, "shift"], "Print", lazy.spawn('gnome-screenshot -i')),

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

#    Key([], "XF86AudioPlay", lazy.spawn("mpc toggle")),
#    Key([], "XF86AudioNext", lazy.spawn("mpc next")),
#    Key([], "XF86AudioPrev", lazy.spawn("mpc prev")),
#    Key([], "XF86AudioStop", lazy.spawn("mpc stop")),

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
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]

# FOR AZERTY KEYBOARDS
#group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

#group_labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
group_labels = ["" for _ in range(len(group_names))]
# group_labels = ["" for _ in range(len(group_names))]
#group_labels = ["" for _ in range(len(group_names))]
# group_labels = ["" for _ in range(len(group_names))]
# group_labels = ["" for _ in range(len(group_names))]
#group_labels = [
        #        "Term", #1
        #        "Term", #2
        #        "3", #3
        #        "4", #4
        #        "5", #5
        #        "6", #6
        #        "7", #7
        #        "Media", #8
        #        "Web", #9
        #        "Code", #0
        #]
#group_labels = ["α", "β", "γ", "δ", "ε", "ζ", "η", "θ", "ι", "κa,]
#group_labels = ["", "", "", "", "","",]
#group_labels = ["Web", "Edit/chat", "Image", "Gimp", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall", "monadwide", "monadwide", "matrix", "ratiotile", "max", "max", "max", "max",]
#group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    group = Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
            )

    groups.append(group)


for i in groups:
    keys.extend([

        #CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group(skip_empty=True)),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(skip_empty=True)),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, mod2], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
        ])

# Add scratchpad and scratchpad keybindings
dropdown_config = {
        "x":0.15, 
        "y":0.15, 
        "width":0.7, 
        "height":0.7,
        "opacity":1,
        "on_focus_lost_hide":True
        }
groups.append(
        ScratchPad(
            name="scratchpad", 
            dropdowns=[
                DropDown("term1", "alacritty", **dropdown_config),
                DropDown("term2", "alacritty", **dropdown_config),
                ],
        ))
keys.append(
        KeyChord(
            [mod], "s", 
            [
                Key([],"1", lazy.group['scratchpad'].dropdown_toggle('term1')),
                Key([],"2", lazy.group['scratchpad'].dropdown_toggle('term2')),
                Key([],"g", lazy.group['scratchpad'].toscreen()),
                ]
            ))

def init_layout_theme():
    return {
            "margin":7,
            "border_width":2,
            "border_focus": primary_color,
            "border_normal": bg_color
            }

layout_theme = init_layout_theme()


layouts = [
        layout.MonadTall(**layout_theme),
        layout.MonadWide(**layout_theme),
        layout.Matrix(**layout_theme),
        #layout.Bsp(**layout_theme),

        #layout.Columns(**layout_theme),
        #layout.Stack(**layout_theme),
        #layout.Tile(**layout_theme),
        layout.RatioTile(**layout_theme),
        layout.VerticalTile(**layout_theme),

        layout.Max(**layout_theme),
        #layout.Zoomy(**layout_theme)
        #layout.TreeTab(
            #    sections=['1', '2', '3'],
            #    bg_color = bg_color,
            #    active_bg = primary_color,
            #    inactive_bg = shadow_color,
            #    padding_y =5,
            #    section_top =10,
            #    panel_width = 280,
            #),
        layout.Floating(**layout_theme),
        ]

# COLORS FOR THE BAR


def init_colors():
    return [["#2F343F", "#2F343F"], # color 0
            ["#2F343F", "#2F343F"], # color 1
            ["#c0c5ce", "#c0c5ce"], # color 2
            ["#ff5050", "#ff5050"], # color 3
            ["#f4c2c2", "#f4c2c2"], # color 4
            ["#ffffff", "#ffffff"], # color 5
            ["#ffd47e", "#ffd47e"], # color 6
            ["#62FF00", "#62FF00"], # color 7
            ["#000000", "#000000"], # color 8
            ["#c40234", "#c40234"], # color 9
            ["#6790eb", "#6790eb"], # color 10
            ["#ff00ff", "#ff00ff"], #11
            ["#4c566a", "#4c566a"], #12 
            ["#282c34", "#282c34"], #13
            ["#212121", "#212121"], #14
            ["#e75480", "#e75480"], #15 
            ["#2aa899", "#2aa899"], #16 
            ["#abb2bf", "#abb2bf"],# color 17
            ["#81a1c1", "#81a1c1"], #18 
            ["#56b6c2", "#56b6c2"], #19 
            ["#b48ead", "#b48ead"], #20 
            ["#e06c75", "#e06c75"], #21
            ["#fb9f7f", "#fb9f7f"], #22
            ["#ffd47e", "#ffd47e"]] #23

colors = init_colors()

# WIDGETS FOR THE BAR

def init_widgets_defaults():
    return dict(
            font=normal_font,
            fontsize = 9,
            padding = 2,
            )

widget_defaults = init_widgets_defaults()
padding_spacer = 5

def init_widgets_list():
    widgets_list = [
            widget.Spacer(
                background=bg_color,
                length=padding_spacer,
                # **powerline,
                ),

            widget.TextBox(
                fmt="󰌌",
                font = bold_font,
                fontsize = 24,
                background = bg_color,
                foreground = bg_color2,
                mouse_callbacks = {'Button1': lazy.widget["keyboardlayout"].next_keyboard()},
                ),

            widget.KeyboardLayout(
                configured_keyboards=['us','us colemak_dh'],
                font = bold_font,
                fontsize = 12,
                background = bg_color,
                foreground = bg_color2,
                #**powerline,
                ),
            widget.Spacer(
                length=padding_spacer,
                # **powerline,
                ),
            widget.Sep(
                    background= primary_color,
                    foreground= primary_color,
                    ),
            widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                background = bg_color2,
                padding = 0,
                scale = 0.7,
                ),

            widget.CurrentLayout(
                font = bold_font,
                fontsize = 12,
                background = bg_color2,
                foreground = bg_color,
                # **powerline,
                ),
            widget.Sep(
                    background= primary_color,
                    foreground= primary_color,
                    ),
            widget.Spacer(
                #background=shadow_color,
                length=padding_spacer,
                # **powerline,
                ),
            widget.TaskList(
                background=bg_color,
                font = normal_font,
                highlight_method = 'block', # or block
                max_title_width=150,
                spacing=5,
                rounded=True,
                padding=3,
                margin=2,
                fontsize=14,
                border=primary_color,
                unfocused_border=bg_color2,
                txt_floating='🗗',
                txt_minimized='>_ ',
                borderwidth = 1,
                foreground=font_color,
                # **powerline,
                ),

            widget.Spacer(
                    #background=shadow_color,
                    length=padding_spacer,
                    # **powerline,
                    ),
            widget.Sep(
                    background= "#453841",
                    foreground= "#453841",
                    # background= bg_color,
                    # foreground= bg_color2,
                    linewidth=1,
                    ),
            widget.GroupBox(
                    # background= bg_color2,
                    background= primary_color,
                    foreground= font_color,
                    font=normal_font,
                    fontsize = 23,
                    center_aligned = True,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,
                    active=font_color,
                    inactive=bg_color,
                    rounded= True,
                    highlight_method='text',
                    highlight_color=shadow_color,
                    urgent_alert_method='line',
                    urgent_border=secondary_color,
                    this_current_screen_border=bg_color2,
                    this_screen_border=bg_color2,
                    other_current_screen_border=shadow_color,
                    other_screen_border=shadow_color,
                    disable_drag=True,
                    #hide_unused=True,
                    #visible_groups=['1','2','9','0'],
                    # **powerline,
                    ),
            widget.Sep(
                    background= "#453841",
                    foreground= "#453841",
                    # background= bg_color,
                    # foreground= bg_color2,
                    linewidth=1,
                    ),
            widget.Spacer(
                    #background=shadow_color,
                    background= bg_color2,
                    length=padding_spacer,
                    # **powerline,
                    ),

            widget.CPU(
                    font=bold_font,
                    format = '{freq_current}GHz {load_percent}%',
                    update_interval = 1,
                    fontsize = 12,
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    #**powerline,
                    ),

            widget.TextBox(
                    fmt = '󰻠 ',
                    font = bold_font,
                    fontsize = 28,
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    ),

            widget.Sep(
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    linewidth=2,
                    #    **powerline,
                    ),

            widget.Memory(
                    font=bold_font,
                    format = '{MemUsed: .3f} {mm}',
                    update_interval = 1,
                    fontsize = 12,
                    measure_mem = 'G',
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    ),
            widget.TextBox(
                    fmt = '󰍛',
                    font = bold_font,
                    fontsize = 28,
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    #**powerline,
                    ),
            widget.Sep(
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    linewidth=2,
                    ),
            widget.TextBox(
                    fmt = '󱊣',
                    font = bold_font,
                    fontsize = 24,
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e battop')},
                    ),
            widget.Battery(
                    font=bold_font,
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    fontsize = 14,
                    format="{percent:2.0%}",
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e battop')},
                    ),
            widget.Sep(
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    linewidth=2,
                    ),
            widget.Spacer(
                    #background=shadow_color,
                    background= bg_color2,
                    length=padding_spacer,
                    # **powerline,
                    ),


            widget.Clock(
                    font=bold_font,
                    # background = primary_color,
                    background= bg_color2,
                    foreground = font_color,
                    fontsize = 20,
                    format="%I:%M %p",
                    ),
            widget.Clock(
                    font=bold_font,
                    # background = primary_color,
                    background= bg_color2,
                    foreground = bg_color,
                    fontsize = 14,
                    format="%a %d-%m-%y",
                    # **powerline,
                    #**powerline,
                    ),
            widget.Sep(
                    background= bg_color2,
                    foreground= bg_color,
                    # background= bg_color,
                    # foreground= bg_color2,
                    linewidth=2,
                    ),

            widget.Spacer(
                    #background=shadow_color,
                    background= bg_color2,
                    length=padding_spacer,
                    # **powerline,
                    ),
            widget.Systray(
                    background= bg_color2,
                    foreground= font_color,
                    padding = 2,
                    #**powerline,
                    ),

            widget.Spacer(
                    background= bg_color2,
                    foreground= font_color,
                    length=padding_spacer,
                    ),

            ]
    return widgets_list


def init_screens():
    return [
            Screen(
                bottom=bar.Bar(
                    widgets=init_widgets_list(), 
                    size=28,
                    margin=[0,20,0,20],
                    opacity=1,
                    background= bg_color,
                    #    border_color = shadow_color,
                    #   border_width = 2,
                    ),
                ),
            Screen(
                bottom=bar.Bar(
                    widgets=init_widgets_list()[:-2],
                    size=28,
                    margin=[0,20,0,20],
                    opacity=1,
                    background= bg_color,
                    #border_color = shadow_color,
                    #border_width = 2,
                    )
                )
            ]
screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(),
             start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(),
             start=lazy.window.get_size())
        ]

dgroups_key_binder = None
dgroups_app_rules = []

# send the window to a perticular group
@hook.subscribe.client_new
def send_to_group(window):
    wm_class = window.window.get_wm_class()[0]

    # Assign window with wm_class to groups
    grp = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [
                "obs", "nitrogen",
                ],
            "8": [
                "vlc", "spotify", "Spotify",
                ],
            "9": [
                "brave", "brave-browser", "Brave", "Brave-browser",
                ],
            "0": [
                "code-oss", "code", "Code-oss", "Code", "vscodium", "VSCodium",
                ],
            } 

    for grp_name in grp:
        if (wm_class in grp[grp_name]):
            window.togroup(grp_name, switch_group=True)

# Send to group fix
# Spotify doesn't move to the group useing `client_new` hook
@hook.subscribe.client_managed
def send_to_group_fix(window):
    wm_class = window.window.get_wm_class()[0]

    # Assign window with wm_class to groups
    grp = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
            "5": [],
            "6": [],
            "7": [],
            "8": [
                "spotify", "Spotify",
                ],
            "9": [],
            "0": [],
            } 

    for grp_name in grp:
        if (wm_class in grp[grp_name]):
            window.togroup(grp_name, switch_group=True)


main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(['xsetroot', '-cursor_name', 'left_ptr'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types):
        window.floating = True


# Move mouse on new window
@hook.subscribe.client_managed
def move_mouse_to_new_window(window):
    move_mouse_to_current_window()

# Move mouse on focued window
@hook.subscribe.focus_change
def move_mouse_to_focued_window(window):
    move_mouse_to_current_window()

floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
        float_rules=[
            *layout.Floating.default_float_rules,
            Match(wm_class='confirm'),
            Match(wm_class='dialog'),
            Match(wm_class='download'),
            Match(wm_class='error'),
            Match(wm_class='file_progress'),
            Match(wm_class='notification'),
            Match(wm_class='splash'),
            Match(wm_class='toolbar'),
            Match(wm_class='confirmreset'),
            Match(wm_class='makebranch'),
            Match(wm_class='maketag'),
            Match(wm_class='Arandr'),
            Match(wm_class='feh'),
            Match(wm_class='Galculator'),
            Match(title='branchdialog'),
            Match(title='Open File'),
            Match(title='pinentry'),
            Match(title='Brave'),
            Match(title='Brave'),
            Match(role='pop-up'),
            #Match(wm_instance_class='crx_nkbihfbeogaeaoehlefnkodbefgpgknn'), # MetaMask Pop-up
            Match(wm_class='ssh-askpass'),
            Match(wm_class='lxpolkit'),
            Match(wm_class='Lxpolkit'),
            Match(wm_class='yad'),
            Match(wm_class='Yad'),
            Match(wm_class='Cairo-dock'),
            Match(wm_class='cairo-dock'),
            ],  
        fullscreen_border_width = 0, 
        border_width=0,
        #border_width=2,
        #border_focus= primary_color,
        #border_normal= bg_color
        )
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"
