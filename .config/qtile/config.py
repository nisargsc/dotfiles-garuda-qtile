import os
import subprocess
from typing import List
from libqtile import layout, bar, hook, qtile, widget
from libqtile.config import  Drag, DropDown, Group, Key, KeyChord, Match, ScratchPad, Screen 
from libqtile.command import lazy
import theme
import hotkeys

mod = hotkeys.mod
mod1 = hotkeys.mod1
mod2 = hotkeys.mod2
home = hotkeys.home

def move_mouse_to_current_window():
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

myTerm = hotkeys.myTerm
keys = hotkeys.bindings

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",]
group_labels = ["" for _ in range(len(group_names))]
group_layouts = ["monadtall", "monadtall", "monadwide", "monadwide", "matrix", "ratiotile", "max", "max", "max", "max",]

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
        Key([mod1], "Tab", lazy.screen.next_group(skip_empty=True)),
        Key([mod1, "shift"], "Tab", lazy.screen.prev_group(skip_empty=True)),

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
            "border_focus": theme.primaryColor,
            "border_normal": theme.bgColor
            }

layout_theme = init_layout_theme()


layouts = [
        layout.MonadTall(**layout_theme),
        layout.MonadWide(**layout_theme),
        layout.Matrix(**layout_theme),
        layout.RatioTile(**layout_theme),
        layout.VerticalTile(**layout_theme),
        layout.Max(**layout_theme),
        layout.Floating(**layout_theme),
        ]

paddingSpacer = 5

def init_widgets_list():
    widgets_list = [
            widget.Spacer(
                background=theme.bgColor,
                length=paddingSpacer,
                ),

            widget.TextBox(
                fmt="󰌌",
                font = theme.boldFont,
                fontsize = 24,
                background = theme.bgColor,
                foreground = theme.bgColor2,
                mouse_callbacks = {'Button1': lazy.widget["keyboardlayout"].next_keyboard()},
                ),

            widget.KeyboardLayout(
                configured_keyboards=['us','us colemak_dh'],
                font = theme.boldFont,
                fontsize = 12,
                background = theme.bgColor,
                foreground = theme.bgColor2,
                ),
            widget.Spacer(
                length=paddingSpacer,
                ),
            widget.Sep(
                    background= theme.primaryColor,
                    foreground= theme.primaryColor,
                    ),
            widget.CurrentLayoutIcon(
                custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                background = theme.bgColor2,
                padding = 0,
                scale = 0.7,
                ),

            widget.CurrentLayout(
                font = theme.boldFont,
                fontsize = 12,
                background = theme.bgColor2,
                foreground = theme.bgColor,
                # **powerline,
                ),
            widget.Sep(
                    background= theme.primaryColor,
                    foreground= theme.primaryColor,
                    ),
            widget.Spacer(
                #background=theme.shadowColor,
                length=paddingSpacer,
                # **powerline,
                ),
            widget.TaskList(
                background=theme.bgColor,
                font = theme.normalFont,
                highlight_method = 'block', # or block
                max_title_width=150,
                spacing=5,
                rounded=True,
                padding=3,
                margin=2,
                fontsize=14,
                border=theme.primaryColor,
                unfocused_border=theme.bgColor2,
                txt_floating='🗗',
                txt_minimized='>_ ',
                borderwidth = 1,
                foreground=theme.fontColor,
                # **powerline,
                ),

            widget.Spacer(
                    #background=theme.shadowColor,
                    length=paddingSpacer,
                    # **powerline,
                    ),
            widget.Sep(
                    background= "#453841",
                    foreground= "#453841",
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    linewidth=1,
                    ),
            widget.GroupBox(
                    # background= theme.bgColor2,
                    background= theme.primaryColor,
                    foreground= theme.fontColor,
                    font=theme.normalFont,
                    fontsize = 23,
                    center_aligned = True,
                    margin_y = 3,
                    margin_x = 2,
                    padding_y = 5,
                    padding_x = 4,
                    borderwidth = 3,
                    active=theme.fontColor,
                    inactive=theme.bgColor,
                    rounded= True,
                    highlight_method='line',
                    highlight_color=theme.shadowColor,
                    urgent_alert_method='line',
                    urgent_border=theme.secondaryColor,
                    this_current_screen_border=theme.bgColor2,
                    this_screen_border=theme.bgColor2,
                    other_current_screen_border=theme.shadowColor,
                    other_screen_border=theme.shadowColor,
                    disable_drag=True,
                    #hide_unused=True,
                    #visible_groups=['1','2','9','0'],
                    # **powerline,
                    ),
            widget.Sep(
                    background= "#453841",
                    foreground= "#453841",
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    linewidth=1,
                    ),
            widget.Spacer(
                    #background=theme.shadowColor,
                    background= theme.bgColor2,
                    length=paddingSpacer,
                    # **powerline,
                    ),

            widget.CPU(
                    font=theme.boldFont,
                    format = '{freq_current}GHz {load_percent}%',
                    update_interval = 1,
                    fontsize = 12,
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    #**powerline,
                    ),

            widget.TextBox(
                    fmt = '󰻠 ',
                    font = theme.boldFont,
                    fontsize = 28,
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    ),

            widget.Sep(
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    linewidth=2,
                    #    **powerline,
                    ),

            widget.Memory(
                    font=theme.boldFont,
                    format = '{MemUsed: .3f} {mm}',
                    update_interval = 1,
                    fontsize = 12,
                    measure_mem = 'G',
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    ),
            widget.TextBox(
                    fmt = '󰍛',
                    font = theme.boldFont,
                    fontsize = 28,
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e htop')},
                    #**powerline,
                    ),
            widget.Sep(
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    linewidth=2,
                    ),
            widget.TextBox(
                    fmt = '󱊣',
                    font = theme.boldFont,
                    fontsize = 24,
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e battop')},
                    ),
            widget.Battery(
                    font=theme.boldFont,
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    fontsize = 14,
                    format="{percent:2.0%}",
                    mouse_callbacks = {'Button1': lambda : qtile.cmd_spawn(myTerm + ' -e battop')},
                    ),
            widget.Sep(
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    linewidth=2,
                    ),
            widget.Spacer(
                    #background=theme.shadowColor,
                    background= theme.bgColor2,
                    length=paddingSpacer,
                    # **powerline,
                    ),


            widget.Clock(
                    font=theme.boldFont,
                    # background = theme.primaryColor,
                    background= theme.bgColor2,
                    foreground = theme.fontColor,
                    fontsize = 20,
                    format="%I:%M %p",
                    ),
            widget.Clock(
                    font=theme.boldFont,
                    # background = theme.primaryColor,
                    background= theme.bgColor2,
                    foreground = theme.bgColor,
                    fontsize = 14,
                    format="%a %d-%m-%y",
                    # **powerline,
                    #**powerline,
                    ),
            widget.Sep(
                    background= theme.bgColor2,
                    foreground= theme.bgColor,
                    # background= theme.bgColor,
                    # foreground= theme.bgColor2,
                    linewidth=2,
                    ),

            widget.Spacer(
                    #background=theme.shadowColor,
                    background= theme.bgColor2,
                    length=paddingSpacer,
                    # **powerline,
                    ),
            widget.Systray(
                    background= theme.bgColor2,
                    foreground= theme.fontColor,
                    padding = 2,
                    #**powerline,
                    ),

            widget.Spacer(
                    background= theme.bgColor2,
                    foreground= theme.fontColor,
                    length=paddingSpacer,
                    ),

            ]
    return widgets_list

def init_screens():
    return [
            Screen(
                bottom=bar.Bar(
                    widgets=init_widgets_list(), 
                    size=28,
                    margin=[0,20,5,20],
                    opacity=1,
                    background= theme.bgColor,
                    ),
                ),
            Screen(
                bottom=bar.Bar(
                    widgets=init_widgets_list()[:-4],
                    size=28,
                    margin=[0,20,5,20],
                    opacity=1,
                    background= theme.bgColor,
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
        #border_focus= theme.primaryColor,
        #border_normal= theme.bgColor
        )
auto_fullscreen = True

focus_on_window_activation = "focus" # or smart

wmname = "LG3D"