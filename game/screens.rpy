# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    default side_image = None
    default two_window = False
    zorder 100
    
    add "UI/messagebox.png":
        yanchor 1.0 ypos 1.0

    # Decide if we want to use the one-window or two-window varaint.
    if not two_window:

        window:
            id "window"
            
            has frame:
                background None
                ysize 380
                ypos -220

                if who:
                    
                    if who != " ":
                        add "UI/nametag.png" xpos -155 ypos -90

                        text who:
                            id "who"
                            size 70
                            xpos -50
                            ypos -146
                            font "NotoSansCJKsc-Regular.otf"
                            outlines [ (3, "#0a0a0a", 0, 0) ] 

                if _preferences.language == None:

                    text what:
                        id "what"
                        size 50
                        xpos 0
                        ypos -60
                        xmaximum 1640
                        font "Fonts/ShareTech-Regular.ttf"
                        outlines [(4, "#000000", 2, 2),(1, "#272727", 0, 0) ] 
                    
                if _preferences.language == "japanese":
                    
                    text what:
                        id "what"
                        size 50
                        xpos 0
                        ypos -60
                        xmaximum 1640
                        font "Fonts/NotoSansCJKjp-Medium.otf"
                        outlines [(4, "#000000", 2, 2),(1, "#272727", 0, 0) ] 
                        
                if _preferences.language == "Chinese":
 
                    text what:
                        id "what"
                        size 50
                        xpos 0
                        ypos -60
                        xmaximum 1640
                        font "NotoSansCJKsc-Regular.otf"
                        outlines [(4, "#000000", 2, 2),(1, "#272727", 0, 0) ] 
                                            
screen decision:
    
    modal True
    zorder 100
            
    imagebutton at tr_decision(0):
        xanchor 0.5
        ypos 0.35
        idle "UI/choice_base.png"
        hover tr_hoverglow("UI/choice_base.png")
        
        activate_sound "sound/button1.ogg"
        action (Hide("decision"),Jump(choice1_jump))
        
    imagebutton at tr_decision(0.2):
        xanchor 0.5
        ypos 0.5
        idle "UI/choice_base.png"
        hover tr_hoverglow("UI/choice_base.png")
        
        activate_sound "sound/button1.ogg"
        action (Hide("decision"),Jump(choice2_jump))
        
    if decision_extra == True:
        
        imagebutton at tr_decision(0.4):
            xanchor 0.5
            ypos 0.65
            idle "UI/choice_base.png"
            hover tr_hoverglow("UI/choice_base.png")
            
            activate_sound "sound/button1.ogg"
            action (Hide("decision"),Jump(choice2_jump))
                
    text choice1_text at tr_decision(0):
        text_align 0.5 xanchor 0.5 ypos 0.39
        size 40
        outlines [ (4, "#282828", 0, 0) ]     
        
    text choice2_text at tr_decision(0.2):
        text_align 0.5 xanchor 0.5 ypos 0.54
        size 40
        outlines [ (4, "#282828", 0, 0) ]    
        
    if decision_extra == True:

        text choice3_text at tr_decision(0.4):
            text_align 0.5 xanchor 0.5 ypos 0.69
            size 40
            outlines [ (4, "#282828", 0, 0) ]    


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    zorder 1000

    add "UI/black.jpg"

    add "UI/mainmenu_back.jpg" at tr_fadein(0.2)


    text "[config.name] V[config.version]" font "Fonts/SourceCodePro-Regular.ttf" xpos 50 ypos 25 size 15 color "F7F7F7"

    if CENSOR == False:

        text 'DENPA EDITION' font "Fonts/SourceCodePro-Regular.ttf" xpos 50 ypos 50 size 15 color "F7F7F7"

    if CENSOR == True:

        text 'STEAM EDITION' font "Fonts/SourceCodePro-Regular.ttf" xpos 50 ypos 50 size 15 color "F7F7F7"
        
    imagebutton at tr_menubutton(0.5,1920):
        xpos 2820 ypos 422 xanchor 810
        idle "UI/mainmenu_button.png"
        hover tr_hoverglow("UI/mainmenu_button.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action Hide("main_menu"),Show("history")
    add "UI/mainmenu_start.png" at tr_menubutton(0.5,1920):
        xpos 2300 ypos 422 xanchor 531

    imagebutton at tr_menubutton(0.6,1920):
        xpos 2820 ypos 496 xanchor 810
        idle "UI/mainmenu_button.png"
        hover tr_hoverglow("UI/mainmenu_button.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action Show("load")
    add "UI/mainmenu_load.png" at tr_menubutton(0.6,1920):
        xpos 2300 ypos 496 xanchor 531

    imagebutton at tr_menubutton(0.7,1920):
        xpos 2820 ypos 570 xanchor 810
        idle "UI/mainmenu_button.png"
        hover tr_hoverglow("UI/mainmenu_button.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action Show("preferences")
    add "UI/mainmenu_options.png" at tr_menubutton(0.7,1920):
        xpos 2300 ypos 570 xanchor 531

    imagebutton at tr_menubutton(0.8,1920):
        xpos 2820 ypos 644 xanchor 810
        idle "UI/mainmenu_button.png"
        hover tr_hoverglow("UI/mainmenu_button.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action Show("gallery_back")
    add "UI/mainmenu_bonus.png" at tr_menubutton(0.8,1920):
        xpos 2300 ypos 644 xanchor 531

    imagebutton at tr_menubutton(0.9,1920):
        xpos 2820 ypos 718 xanchor 810
        idle "UI/mainmenu_button.png"
        hover tr_hoverglow("UI/mainmenu_button.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action Quit()
    add "UI/mainmenu_quit.png" at tr_menubutton(0.9,1920):
        xpos 2300 ypos 718 xanchor 531   

    add "UI/mainmenu_ava.png" xpos -200 at tr_menubutton(0.5,0)
    add "UI/mainmenu_sola.png" xpos -200 at tr_menubutton(0.6,0)
    add "UI/mainmenu_claude.png" xpos -200 at tr_menubutton(0.8,0)
    add "UI/mainmenu_cosette.png" xpos -200 at tr_menubutton(0.7,0)
    add "UI/mainmenu_chigara.png" xpos -200 at tr_menubutton(0.9,0)
    add "UI/mainmenu_kryscari.png" xpos -200 at tr_menubutton(1,0)
    add "UI/mainmenu_asaga.png" xpos -200 at tr_menubutton(1.1,0)
    add "UI/mainmenu_logo.png" xpos -200 ypos 0 at tr_menubutton(0.3,0)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.
screen save():

    zorder 1200
    modal True
    
    drag:

        drag_name "drag_save"
        drag_handle (0,0,450,44)
        xpos 100 ypos 200
        drag_offscreen False

        fixed at tr_fadein(0):
            xmaximum 1196 ymaximum 630

            add "UI/save_base.png"

            imagebutton:
                xpos 565 ypos 50
                idle "UI/load_default.png"
                hover tr_hoverglow("UI/load_default.png")            
                action FilePage(1)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None
                
            imagebutton:
                xpos 754 ypos 50
                idle "UI/load_auto.png"
                hover tr_hoverglow("UI/load_auto.png")            
                action FilePage("auto")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None
                
            imagebutton:
                xpos 943 ypos 50
                idle "UI/load_quick.png"
                hover tr_hoverglow("UI/load_quick.png")            
                action FilePage("quick")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None

            imagebutton:
                xpos 1133 ypos 50
                idle "UI/load_cancel.png"
                hover tr_hoverglow("UI/load_cancel.png")            
                action (Hide("save"),SetVariable("show_save",False))
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None

            style "file_picker_frame"

            $ columns = 4
            $ rows = 50
            hbox:
                area (26, 92, 1148, 517)
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    child_size (1100,5000)
                                
                    grid columns rows:
                        transpose False
                        xfill True
                        style_group "file_picker"
                        xpos 40
                        ypos 190
                        
                        for i in range(1, rows * columns + 1):
                            
                            frame:
                                xmaximum 265
                                ymaximum 165
                                background None
                            
                                button:
                                    background None
                                    focus_mask None
                                    
                                    has vbox

                                    $ description = "% 2s. %s\n%s" % (
                                        FileSlotName(i, rows*columns),
                                        FileTime(i, empty=_("Empty Slot.")),
                                        FileSaveName(i))
                                    
                                    text description ysize 10 color "F7F7F7" font "Fonts/SourceCodePro-Regular.ttf" size 13
                                    add FileScreenshot(i) size(227,127) ypos -15

                                imagebutton:
                                    idle "UI/saveload_slot_base.png"
                                    hover "UI/saveload_slot_hover.png"
                                    hover_sound "sound/hover1.ogg"
                                    activate_sound "sound/button1.ogg"
                                    focus_mask None
                                    action FileAction(i)

                                imagebutton:
                                    idle "UI/savedelete_base.png"
                                    hover "UI/savedelete_hover.png"
                                    insensitive "UI/savedelete_inactive.png"
                                    activate_sound "sound/cancel.ogg"
                                    xpos 184
                                    action FileDelete(i)         
screen load:

    zorder 1200
    modal True
    
    drag:
        
        drag_name "drag_load"
        drag_raise True
        drag_handle (0,0,450,44)
        xpos 100 ypos 200
        drag_offscreen False
        
        fixed at tr_fadein(0):
            xmaximum 1196 ymaximum 630

            add "UI/load_base.png"

            imagebutton:
                xpos 565 ypos 50
                idle "UI/load_default.png"
                hover tr_hoverglow("UI/load_default.png")            
                action FilePage(1)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None
                
            imagebutton:
                xpos 754 ypos 50
                idle "UI/load_auto.png"
                hover tr_hoverglow("UI/load_auto.png")            
                action FilePage("auto")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None
                
            imagebutton:
                xpos 943 ypos 50
                idle "UI/load_quick.png"
                hover tr_hoverglow("UI/load_quick.png")            
                action FilePage("quick")
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None

            imagebutton:
                xpos 1133 ypos 50
                idle "UI/load_cancel.png"
                hover tr_hoverglow("UI/load_cancel.png")            
                action (Hide("load"),SetVariable("show_load",False))
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                focus_mask None

            style "file_picker_frame"

            $ columns = 4
            $ rows = 50

            hbox:
                area (26, 92, 1148, 517)
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    child_size (1100,5000)
                                
                    grid columns rows:
                        transpose False
                        xfill True
                        style_group "file_picker"
                        xpos 40
                        ypos 190
                        
                        for i in range(1, rows * columns + 1):
                            
                            frame:
                                xmaximum 265
                                ymaximum 165
                                background None
                            
                                button:
                                    background None
                                    focus_mask None
                                    
                                    has vbox

                                    $ description = "% 2s. %s\n%s" % (
                                        FileSlotName(i, rows*columns),
                                        FileTime(i, empty=_("Empty Slot.")),
                                        FileSaveName(i))
                                    
                                    text description ysize 10 color "F7F7F7" font "Fonts/SourceCodePro-Regular.ttf" size 13
                                    add FileScreenshot(i) size(227,127) ypos -15

                                imagebutton:
                                    idle "UI/saveload_slot_base.png"
                                    hover "UI/saveload_slot_hover.png"
                                    hover_sound "sound/hover1.ogg"
                                    activate_sound "sound/button1.ogg"
                                    focus_mask None
                                    action FileAction(i)
                            
                                imagebutton:
                                    idle "UI/savedelete_base.png"
                                    hover "UI/savedelete_hover.png"
                                    insensitive "UI/savedelete_inactive.png"
                                    activate_sound "sound/cancel.ogg"
                                    xpos 184
                                    action FileDelete(i)

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:
    zorder 1200
    modal True
    
    drag:

        drag_name "drag_prefs"
        drag_handle (0,0,450,44)
        xpos 100 ypos 200
        drag_offscreen False
    
        fixed at tr_fadein(0):
            xmaximum 1196 ymaximum 630

            add "UI/options_base.png"

            imagebutton:
                xpos 565 ypos 50
                idle "UI/options_main.png"
                hover tr_hoverglow("UI/options_main.png")
                selected_idle "UI/options_main_select.png"
                selected_hover tr_hoverglow("UI/options_main_select.png")
                action SetVariable("option_show",1)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            imagebutton:
                xpos 754 ypos 50
                idle "UI/options_audio.png"
                hover tr_hoverglow("UI/options_audio.png")
                selected_idle "UI/options_audio_select.png"
                selected_hover tr_hoverglow("UI/options_audio_select.png")
                action SetVariable("option_show",2)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            imagebutton:
                xpos 943 ypos 50
                idle "UI/options_gameplay.png"
                hover tr_hoverglow("UI/options_gameplay.png")
                selected_idle "UI/options_gameplay_select.png"
                selected_hover tr_hoverglow("UI/options_gameplay_select.png")
                action SetVariable("option_show",3)
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"

            imagebutton:
                xpos 1133 ypos 52
                idle "UI/load_cancel.png"
                hover tr_hoverglow("UI/load_cancel.png")            
                action (Hide("preferences"),Hide("option_main"),Hide("option_audio"),Hide("option_gameplay"),SetVariable("show_preference",False))
                hover_sound "sound/hover1.ogg"
                activate_sound "sound/button1.ogg"
                
            if option_show == 1:
                
                add "UI/options_main_text.png"
                
                imagebutton:
                    xpos 86 ypos 165
                    idle "UI/options_main_fullscreen.png"
                    hover tr_hoverglow("UI/options_main_fullscreen.png")
                    selected_idle "UI/options_main_fullscreen_select.png"
                    selected_hover tr_hoverglow("UI/options_main_fullscreen_select.png")
                    action Preference("display", "fullscreen")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 294 ypos 165
                    idle "UI/options_main_window.png"
                    hover tr_hoverglow("UI/options_main_window.png")
                    selected_idle "UI/options_main_window_select.png"
                    selected_hover tr_hoverglow("UI/options_main_window_select.png")
                    action [ Preference("display", "window"), SelectedIf(not _preferences.fullscreen) ]
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 86 ypos 360
                    idle "UI/options_main_skipall.png"
                    hover tr_hoverglow("UI/options_main_skipall.png")
                    selected_idle "UI/options_main_skipall_select.png"
                    selected_hover tr_hoverglow("UI/options_main_skipall_select.png")
                    action Preference("skip", "all")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 294 ypos 360
                    idle "UI/options_main_skipseen.png"
                    hover tr_hoverglow("UI/options_main_skipseen.png")
                    selected_idle "UI/options_main_skipseen_select.png"
                    selected_hover tr_hoverglow("UI/options_main_skipseen_select.png")
                    action Preference("skip", "seen")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 86 ypos 428
                    idle "UI/options_main_keepskipping.png"
                    hover tr_hoverglow("UI/options_main_keepskipping.png")
                    selected_idle "UI/options_main_keepskipping_select.png"
                    selected_hover tr_hoverglow("UI/options_main_keepskipping_select.png")
                    action Preference("after choices", "skip")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 294 ypos 428
                    idle "UI/options_main_stop.png"
                    hover tr_hoverglow("UI/options_main_stop.png")
                    selected_idle "UI/options_main_stop_select.png"
                    selected_hover tr_hoverglow("UI/options_main_stop_select.png")
                    action Preference("after choices", "stop")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 590 ypos 460
                    idle "UI/usa_base.jpg"
                    hover "UI/usa_hover.jpg"
                    selected_idle "UI/usa_select.jpg"
                    selected_hover "UI/usa_select_hover.jpg"
                    action Language(None)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 720 ypos 460
                    idle "UI/japan_base.jpg"
                    hover "UI/japan_hover.jpg"
                    selected_idle "UI/japan_select.jpg"
                    selected_hover "UI/japan_select_hover.jpg"
                    action Language("japanese")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 850 ypos 460
                    idle "UI/usa_base.jpg"
                    hover "UI/usa_hover.jpg"
                    selected_idle "UI/usa_select.jpg"
                    selected_hover "UI/usa_select_hover.jpg"
                    action Language("Chinese")
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                bar:
                    xpos 600
                    ypos 165
                    xmaximum 300
                    value Preference("text speed")
                bar:
                    xpos 600
                    ypos 350
                    xmaximum 300
                    value Preference("auto-forward time")
                    
            if option_show == 2:
                
                add "UI/options_audio_text.png"
                
                bar:
                    xpos 60
                    ypos 160
                    xmaximum 300
                    value Preference("music volume")
                bar:
                    xpos 60
                    ypos 250
                    xmaximum 300
                    value Preference("sound volume")
                bar:
                    xpos 60
                    ypos 340
                    xmaximum 300
                    value Preference("voice volume")
                    
                imagebutton:
                    xpos 450 ypos 250
                    idle "UI/options_audio_test.png"
                    hover tr_hoverglow("UI/options_audio_test.png")
                    selected_idle "UI/options_audio_test_select.png"
                    selected_hover tr_hoverglow("UI/options_audio_test_select.png")
                    action Play("sound", "sound/explosion1.ogg", selected=True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 450 ypos 340
                    idle "UI/options_audio_test.png"
                    hover tr_hoverglow("UI/options_audio_test.png")
                    selected_idle "UI/options_audio_test_select.png"
                    selected_hover tr_hoverglow("UI/options_audio_test_select.png")
                    action Play("voice", "sound/Voice/asa_Sel_07.ogg", selected=True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                #english battle voices
                imagebutton:
                    xpos 690 ypos 175
                    idle "UI/options_audio_libdayvoice.png"
                    hover tr_hoverglow("UI/options_audio_libdayvoice.png")
                    selected_idle "UI/options_audio_libdayvoice_selected.png"
                    selected_hover tr_hoverglow("UI/options_audio_libdayvoice_selected.png")
                    action SetField(BM,'english_battle_voices',False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 690 ypos 225
                    idle "UI/options_audio_moavoice.png"
                    hover tr_hoverglow("UI/options_audio_moavoice.png")
                    selected_idle "UI/options_audio_moavoice_selected.png"
                    selected_hover tr_hoverglow("UI/options_audio_moavoice_selected.png")
                    action SetField(BM,'english_battle_voices',True)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                #dialogue voicing
                imagebutton:
                    xpos 690 ypos 340
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(config, 'auto_voice',true_value='sound/Voice/{id}.ogg', false_value=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                    
                    
                    
            if option_show == 3:
                
                add "UI/options_gameplay_text.png"
                
                default tt = Tooltip("")
                
                imagebutton:
                    xpos 90 ypos 170
                    idle "UI/options_gameplay_waifu.png"
                    hover tr_hoverglow("UI/options_gameplay_waifu.png")
                    selected_idle "UI/options_gameplay_waifu_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_waifu_select.png")
                    hovered tt.Action("Reduces the difficulty to near nill\nfor a stress free experience."),SetVariable("tty",170)
                    unhovered SetVariable("tty",-5000)
                    action SetVariable("Difficulty", 0)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 90 ypos 220
                    idle "UI/options_gameplay_casual.png"
                    hover tr_hoverglow("UI/options_gameplay_casual.png")
                    selected_idle "UI/options_gameplay_casual_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_casual_select.png")
                    hovered tt.Action("Easy for newcomers and people not\ninterested in strategy."),SetVariable("tty",220)
                    unhovered SetVariable("tty",-5000)
                    action SetVariable("Difficulty", 1)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 270
                    idle "UI/options_gameplay_ensign.png"
                    hover tr_hoverglow("UI/options_gameplay_ensign.png")
                    selected_idle "UI/options_gameplay_ensign_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_ensign_select.png")
                    hovered tt.Action("Average difficulty for people who want\na reasonable challenge."),SetVariable("tty",270)
                    unhovered SetVariable("tty",-5000)
                    action SetVariable("Difficulty", 2)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 320
                    idle "UI/options_gameplay_captain.png"
                    hover tr_hoverglow("UI/options_gameplay_captain.png")
                    selected_idle "UI/options_gameplay_captain_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_captain_select.png")
                    action SetVariable("Difficulty", 3)
                    hovered tt.Action("Challenging but fair. Your mistakes\nwill be punished without mercy."),SetVariable("tty",320)
                    unhovered SetVariable("tty",-5000)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 370
                    idle "UI/options_gameplay_admiral.png"
                    hover tr_hoverglow("UI/options_gameplay_admiral.png")
                    selected_idle "UI/options_gameplay_admiral_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_admiral_select.png")
                    hovered tt.Action("For people who are good at this game."),SetVariable("tty",370)
                    unhovered SetVariable("tty",-5000)
                    action SetVariable("Difficulty", 4)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 90 ypos 420
                    idle "UI/options_gameplay_spacewhale.png"
                    hover tr_hoverglow("UI/options_gameplay_spacewhale.png")
                    selected_idle "UI/options_gameplay_spacewhale_select.png"
                    selected_hover tr_hoverglow("UI/options_gameplay_spacewhale_select.png")
                    hovered tt.Action("Why would you do this to yourself..."),SetVariable("tty",420)
                    unhovered SetVariable("tty",-5000)
                    action SetVariable("Difficulty", 5)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 600 ypos 168
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM, 'show_tooltips',true_value=True, false_value=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 600 ypos 274
                    idle "UI/checkbox.png"
                    hover tr_hoverglow("UI/checkbox.png")
                    selected_idle "UI/checkbox_select.png"
                    selected_hover tr_hoverglow("UI/checkbox_select.png")
                    action ToggleField(BM, 'edgescroll',true_value=(20,1000), false_value=(0,0))
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                frame:
                    
                    xpos 360
                    ypos tty
                    background "#000000"
                    
                    text tt.value:
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#F7F7F7"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    zorder 10000
    modal True
    fixed at tr_fadein(0):
        add "UI/yesno_base.png"
                    
        imagebutton:
            xpos 0.4 ypos 0.58 xanchor 0.5 yanchor 0.5
            idle "UI/yesno_yes.png"
            hover tr_hoverglow("UI/yesno_yes.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/button1.ogg"
            action yes_action
            
        imagebutton:
            xpos 0.6 ypos 0.58 xanchor 0.5 yanchor 0.5
            idle "UI/yesno_no.png"
            hover tr_hoverglow("UI/yesno_no.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/button1.ogg"
            action no_action

        frame:
            background None
            text message font "Fonts/SourceCodePro-Regular.ttf" size 20 color "#F7F7F7"
            xalign 0.5
            yalign 0.45


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Back") action Rollback()
        if BM.phase == 'Player':
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
        textbutton _("Skip") action Skip()
        textbutton _("F.Skip") action Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Prefs") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

screen history():
    
    zorder 500
    
    add "UI/mainmenu_back.jpg"
    
    add "UI/input_back.png" at tr_fadein(1):
        xpos 375 ypos 107
        
    default htt = Tooltip("")
    
    imagebutton at tr_fadein(1):
        xpos 1300 ypos 125
        idle "UI/back.png"
        hover tr_hoverglow("UI/back.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action Show("main_menu"),Hide("history")
    
    imagebutton at tr_fadein(1):
        xpos 1110 ypos 125
        idle "UI/import.png"
        hover tr_hoverglow("UI/import.png")
        hover_sound "sound/hover1.ogg"
        activate_sound "sound/button1.ogg"
        action SetVariable("customstat",False),Start()
    
    frame at tr_fadein(1):
        area (425, 207, 2000, 740)
        background None

        viewport id "history_box":
            draggable False
            mousewheel True
            child_size (1800,1380)
            
            frame at tr_fadein(1):
                
                background None
                        
                imagebutton:
                    xpos 10 ypos 10
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"瑟拉沦陷后，你选择采用怎样的旗帜？"),SetVariable("httx",10),SetVariable("htty",10)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 10
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你告诉艾瓦太阳骑士号永远采用瑟拉军的旗帜。"),SetVariable("httx",430),SetVariable("htty",10)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_ceraflag",True)
                    activate_sound "sound/button1.ogg"                    
                    
                imagebutton:
                    xpos 740 ypos 10
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你告诉艾瓦当一艘海盗船也不错。"),SetVariable("httx",740),SetVariable("htty",10)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_ceraflag",False)
                    activate_sound "sound/button1.ogg"                        
                        
                imagebutton:
                    xpos 10 ypos 50
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"十年后的再会，你如何对待艾瓦？"),SetVariable("httx",10),SetVariable("htty",50)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 50
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你用正式的态度对待她。"),SetVariable("httx",430),SetVariable("htty",50)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_professionalreunion",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 50
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你告诉艾瓦就像昨日重现。"),SetVariable("httx",740),SetVariable("htty",50)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_professionalreunion",False)
                    activate_sound "sound/button1.ogg"
                        
                imagebutton:
                    xpos 10 ypos 90
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"阿萨嘉登船时你支持了谁？"),SetVariable("httx",10),SetVariable("htty",90)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 90
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你让阿萨嘉不必拘谨。"),SetVariable("httx",430),SetVariable("htty",90)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_loosenrule",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 90
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你同意艾瓦遵守规章。"),SetVariable("httx",740),SetVariable("htty",90)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_loosenrule",False)
                    activate_sound "sound/button1.ogg"
                        
                imagebutton:
                    xpos 10 ypos 130
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"第一次额外任务你选择了哪里？"),SetVariable("httx",10),SetVariable("htty",130)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 130
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你攻击了PACT通讯中枢。"),SetVariable("httx",430),SetVariable("htty",130)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_pactspire",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 130
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你阻止了人贩子。"),SetVariable("httx",740),SetVariable("htty",130)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_pactspire",False)
                    activate_sound "sound/button1.ogg"
                        
                if his_pactspire == False:
                        
                    imagebutton:
                        xpos 10 ypos 170
                        idle "UI/input_plotback.png"
                        hover "UI/input_plotback.png"
                        action NullAction()
                        hovered htt.Action(u"你如何处置那些人贩子？"),SetVariable("httx",10),SetVariable("htty",170)
                        unhovered SetVariable("htty",-5000)
                        activate_sound "sound/button1.ogg"
                    
                    imagebutton:
                        xpos 430 ypos 170
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        hovered htt.Action(u"你把他们捉住交给了当局。"),SetVariable("httx",430),SetVariable("htty",170)
                        unhovered SetVariable("htty",-5000)
                        action SetVariable("his_capturetraffickers",True)
                        activate_sound "sound/button1.ogg"

                    imagebutton:
                        xpos 740 ypos 170
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        hovered htt.Action(u"你让他们漂流至死。"),SetVariable("httx",740),SetVariable("htty",170)
                        unhovered SetVariable("htty",-5000)
                        action SetVariable("his_capturetraffickers",False)
                        activate_sound "sound/button1.ogg"

                if his_pactspire != False:
                        
                    imagebutton:
                        xpos 10 ypos 170
                        idle "UI/input_plotback.png"
                        hover "UI/input_plotback.png"
                        action None
                        unhovered SetVariable("htty",-5000)
                        activate_sound "sound/button1.ogg"
                    
                    imagebutton:
                        xpos 430 ypos 170
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        unhovered SetVariable("htty",-5000)
                        action None
                        activate_sound "sound/button1.ogg"
                        
                    imagebutton:
                        xpos 740 ypos 170
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        unhovered SetVariable("htty",-5000)
                        action None
                        activate_sound "sound/button1.ogg"
                            
                imagebutton:
                    xpos 10 ypos 210
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"联盟沃尔斯塔的外交官们怎样了？"),SetVariable("httx",10),SetVariable("htty",210)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 210
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你救了那些外交官。"),SetVariable("httx",430),SetVariable("htty",210)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_diplomatssaved",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 210
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"阿伽门农号沉没了。"),SetVariable("httx",740),SetVariable("htty",210)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_diplomatssaved",False)
                    activate_sound "sound/button1.ogg"
                      
                imagebutton:
                    xpos 10 ypos 250
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"解救年糕号时候的战术是？"),SetVariable("httx",10),SetVariable("htty",250)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 250
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"太空骑士突击解救年糕号。"),SetVariable("httx",430),SetVariable("htty",250)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_mochirescue",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 250
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"太空骑士保护太阳骑士号。"),SetVariable("httx",740),SetVariable("htty",250)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_mochirescue",False)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 10 ypos 290
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"发现科洛特是个骗子后你怎么做的？"),SetVariable("httx",10),SetVariable("htty",290)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 290
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你放了科洛特。"),SetVariable("httx",430),SetVariable("htty",290)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_claudesupport",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 290
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你把她关了起来。"),SetVariable("httx",740),SetVariable("htty",290)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_claudesupport",False)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 10 ypos 330
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"对切嘉拉隐瞒阿萨嘉真实身份的行为你如何对待？"),SetVariable("httx",10),SetVariable("htty",330)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 330
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你原谅了切嘉拉因为她想保护阿萨嘉。"),SetVariable("httx",430),SetVariable("htty",330)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_chigaraforgive",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 330
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你斥责了切嘉拉因为她让战舰处于危险。"),SetVariable("httx",740),SetVariable("htty",330)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_chigaraforgive",False)
                    activate_sound "sound/button1.ogg"                    
                    
                imagebutton:
                    xpos 10 ypos 370
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"阿萨嘉被带走后与索拉的对话你怎么说的？"),SetVariable("httx",10),SetVariable("htty",370)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 370
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你告诉索拉别做什么危险的事情。"),SetVariable("httx",430),SetVariable("htty",370)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_solacareful",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 370
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你告诉索拉干掉PACT。"),SetVariable("httx",740),SetVariable("htty",370)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_solacareful",False)
                    activate_sound "sound/button1.ogg"                         
                    
                imagebutton:
                    xpos 10 ypos 410
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"伊卡莉和科莉斯卡争论“凤凰”违反安全规范时你支持了谁？"),SetVariable("httx",10),SetVariable("htty",410)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 410
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持了伊卡莉，告诉科莉斯卡联盟的安全规范在这里不适用。"),SetVariable("httx",430),SetVariable("htty",410)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_noallianceregulations",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 410
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持了科莉斯卡，要求伊卡莉把“凤凰”改装得符合规范。"),SetVariable("httx",740),SetVariable("htty",410)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_noallianceregulations",False)
                    activate_sound "sound/button1.ogg"   
                    
                imagebutton:
                    xpos 10 ypos 450
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"切嘉拉因为阿卡迪乌斯而紧张的时候，你支持了谁？"),SetVariable("httx",10),SetVariable("htty",450)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 450
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持了阿萨嘉，让切嘉拉勇敢些。"),SetVariable("httx",430),SetVariable("htty",450)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_cafeteriaasaga",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 450
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持了切嘉拉，告诉阿萨嘉不是每个人都那么勇敢。"),SetVariable("httx",740),SetVariable("htty",450)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_cafeteriaasaga",False)
                    activate_sound "sound/button1.ogg"                       
                    
                imagebutton:
                    xpos 10 ypos 490
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"当和伊卡莉讨论名声的时候，你怎么想的？"),SetVariable("httx",10),SetVariable("htty",490)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 490
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你对名声没有兴趣。"),SetVariable("httx",430),SetVariable("htty",490)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_notinterestedinfame",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 490
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你要利用这名声集结力量对抗PACT。"),SetVariable("httx",740),SetVariable("htty",490)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_notinterestedinfame",False)
                    activate_sound "sound/button1.ogg"                          
                    
                imagebutton:
                    xpos 10 ypos 530
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"远地港战斗前，你怎么看待联盟？"),SetVariable("httx",10),SetVariable("htty",530)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 530
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你怀疑联盟。"),SetVariable("httx",430),SetVariable("htty",530)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_beforefarportsuspectalliance",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 530
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你信任联盟。"),SetVariable("httx",740),SetVariable("htty",530)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_beforefarportsuspectalliance",False)
                    activate_sound "sound/button1.ogg"      
                    
                imagebutton:
                    xpos 10 ypos 570
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"和切嘉拉讨论到悖论核心的时候你是怎么说的？"),SetVariable("httx",10),SetVariable("htty",570)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 570
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你说这种科技被滥用很危险。"),SetVariable("httx",430),SetVariable("htty",570)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_techdangerous",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 570
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你说这种科技用处很大。"),SetVariable("httx",740),SetVariable("htty",570)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_techdangerous",False)
                    activate_sound "sound/button1.ogg"                          
                    
                imagebutton:
                    xpos 10 ypos 610
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"你在海滩和谁聊了？"),SetVariable("httx",10),SetVariable("htty",570)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 610
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    action SetVariable("his_beach1",1)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 610
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    action SetVariable("his_beach1",2)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 430 ypos 650
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    action SetVariable("his_beach1",3)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 650
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    action SetVariable("his_beach1",4)
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 430 ypos 690
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    action SetVariable("his_beach1",5)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 690
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    action SetVariable("his_beach1",6)
                    activate_sound "sound/button1.ogg"

                imagebutton:
                    xpos 10 ypos 730
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"你在海滩和谁聊了？"),SetVariable("httx",10),SetVariable("htty",730)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                if his_beach1 != 1:
                
                    imagebutton:
                        xpos 430 ypos 730
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach2",1)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 2:
                        
                    imagebutton:
                        xpos 740 ypos 730
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach2",2)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 3:
                        
                    imagebutton:
                        xpos 430 ypos 770
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach2",3)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 4:
                        
                    imagebutton:
                        xpos 740 ypos 770
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach2",4)
                        activate_sound "sound/button1.ogg"

                if his_beach1 != 5:

                    imagebutton:
                        xpos 430 ypos 810
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach2",5)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 6:
                        
                    imagebutton:
                        xpos 740 ypos 810
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach2",6)
                        activate_sound "sound/button1.ogg"
                        
                imagebutton:
                    xpos 10 ypos 850
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"你在海滩和谁聊了？"),SetVariable("httx",10),SetVariable("htty",850)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                if his_beach1 != 1 and his_beach2 != 1:
                
                    imagebutton:
                        xpos 430 ypos 850
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach3",1)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 2 and his_beach2 != 2:
                        
                    imagebutton:
                        xpos 740 ypos 850
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach3",2)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 3 and his_beach2 != 3:
                        
                    imagebutton:
                        xpos 430 ypos 890
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach3",3)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 4 and his_beach2 != 4:
                        
                    imagebutton:
                        xpos 740 ypos 890
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach3",4)
                        activate_sound "sound/button1.ogg"

                if his_beach1 != 5 and his_beach2 != 5:

                    imagebutton:
                        xpos 430 ypos 930
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach3",5)
                        activate_sound "sound/button1.ogg"
                        
                if his_beach1 != 6 and his_beach2 != 6:
                        
                    imagebutton:
                        xpos 740 ypos 930
                        idle "UI/input_decision.png"
                        hover "UI/input_decision.png"
                        selected_idle "UI/input_decision_select.png"
                        selected_hover "UI/input_decision_select.png"
                        action SetVariable("his_beach3",6)
                        activate_sound "sound/button1.ogg"
                        
                        
                imagebutton:
                    xpos 10 ypos 970
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"索拉告诉你她母亲的故事时，你怎么说的？"),SetVariable("httx",10),SetVariable("htty",970)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 970
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"她母亲相信王子会娶她太幼稚了。"),SetVariable("httx",430),SetVariable("htty",970)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_mothernaive",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 970
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你很同情她母亲。"),SetVariable("httx",740),SetVariable("htty",970)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_mothernaive",False)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 10 ypos 1010
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"索拉告诉你她的身世后，你怎么说的？"),SetVariable("httx",10),SetVariable("htty",1010)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1010
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你发誓永远不会牺牲她。"),SetVariable("httx",430),SetVariable("htty",1010)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_solaprotect",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1010
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你说她为了人民牺牲非常勇敢。"),SetVariable("httx",740),SetVariable("htty",1010)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_solaprotect",False)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 10 ypos 1050
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"你如何处置成为了海盗的前瑟拉军成员？"),SetVariable("httx",10),SetVariable("htty",1050)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1050
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你接纳了他们，让他们在太阳骑士号上工作。"),SetVariable("httx",430),SetVariable("htty",1050)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_acquitteddeserters",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1050
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你军法处置了他们。"),SetVariable("httx",740),SetVariable("htty",1050)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_acquitteddeserters",False)
                    activate_sound "sound/button1.ogg"                    
                    
                imagebutton:
                    xpos 10 ypos 1090
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"你留下了愿望机吗？"),SetVariable("httx",10),SetVariable("htty",1090)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1090
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你卖了10 000元。"),SetVariable("httx",430),SetVariable("htty",1090)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_soldwishall",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1090
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你保留了愿望机。"),SetVariable("httx",740),SetVariable("htty",1090)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_soldwishall",False)
                    activate_sound "sound/button1.ogg"
                                        
                imagebutton:
                    xpos 10 ypos 1130
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"联盟选举你支持谁？"),SetVariable("httx",10),SetVariable("htty",1130)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1130
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持格雷上将。"),SetVariable("httx",430),SetVariable("htty",1130)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_backgrey",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1130
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你希望权力留在平民政府手中。"),SetVariable("httx",740),SetVariable("htty",1130)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_backgrey",False)
                    activate_sound "sound/button1.ogg"                            
                    
                imagebutton:
                    xpos 10 ypos 1170
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"视察昂格斯的贫民窟后，你支持谁？"),SetVariable("httx",10),SetVariable("htty",1170)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1170
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持联盟的救济计划。"),SetVariable("httx",430),SetVariable("htty",1170)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_supportrelief",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1170
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持中立星缘的独立。"),SetVariable("httx",740),SetVariable("htty",1170)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_supportrelief",False)
                    activate_sound "sound/button1.ogg"                      
                    
                imagebutton:
                    xpos 10 ypos 1210
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"对解救你造成的平民伤亡你如何反应？"),SetVariable("httx",10),SetVariable("htty",1210)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1210
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你向媒体披露了这次事件。"),SetVariable("httx",430),SetVariable("htty",1210)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_gotopress",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1210
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你隐瞒了这次事件。"),SetVariable("httx",740),SetVariable("htty",1210)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_gotopress",False)
                    activate_sound "sound/button1.ogg"                            
                    
                imagebutton:
                    xpos 10 ypos 1250
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"昂格斯事件后你支持联盟吗？"),SetVariable("httx",10),SetVariable("htty",1250)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1250
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持联盟。"),SetVariable("httx",430),SetVariable("htty",1250)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_backalliance",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1250
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你认为联盟不能信任。"),SetVariable("httx",740),SetVariable("htty",1250)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_backalliance",False)
                    activate_sound "sound/button1.ogg"                        
                    
                imagebutton:
                    xpos 10 ypos 1290
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"格雷上将向方特纳威胁夷平昂格斯时你如何反应？"),SetVariable("httx",10),SetVariable("htty",1290)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1290
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你支持上将。"),SetVariable("httx",430),SetVariable("htty",1290)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_suppportnuke",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1290
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你反对上将。"),SetVariable("httx",740),SetVariable("htty",1290)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_suppportnuke",False)
                    activate_sound "sound/button1.ogg"                              
                    
                imagebutton:
                    xpos 10 ypos 1330
                    idle "UI/input_plotback.png"
                    hover "UI/input_plotback.png"
                    action NullAction()
                    hovered htt.Action(u"你让艾瓦去发射先锋火炮了吗？"),SetVariable("httx",10),SetVariable("htty",1330)
                    unhovered SetVariable("htty",-5000)
                    activate_sound "sound/button1.ogg"
                
                imagebutton:
                    xpos 430 ypos 1330
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"艾瓦发射了先锋火炮，击沉了军团号。"),SetVariable("httx",430),SetVariable("htty",1330)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_legionsank",True)
                    activate_sound "sound/button1.ogg"
                    
                imagebutton:
                    xpos 740 ypos 1330
                    idle "UI/input_decision.png"
                    hover "UI/input_decision.png"
                    selected_idle "UI/input_decision_select.png"
                    selected_hover "UI/input_decision_select.png"
                    hovered htt.Action(u"你让艾瓦留在舰桥，军团号存活。"),SetVariable("httx",740),SetVariable("htty",1330)
                    unhovered SetVariable("htty",-5000)
                    action SetVariable("his_legionsank",False)
                    activate_sound "sound/button1.ogg"    


                    
            frame at tr_fadein(0):

                background None
                xpos 25 ypos 6
                
                text u"旗帜":
                    xpos 10 ypos 10
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"瑟拉军":
                    xpos 430 ypos 10
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"海盗船":
                    xpos 740 ypos 10
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"与艾瓦重逢":
                    xpos 10 ypos 50
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"公事公办":
                    xpos 430 ypos 50
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"回忆往昔":
                    xpos 740 ypos 50
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"军事规章":
                    xpos 10 ypos 90
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"适当通融":
                    xpos 430 ypos 90
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"严格执行":
                    xpos 740 ypos 90
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"第一次任务":
                    xpos 10 ypos 130
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"PACT通讯中枢":
                    xpos 430 ypos 130
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"人贩子":
                    xpos 740 ypos 130
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                if his_pactspire == False:

                    text u"人贩子的处置":
                        xpos 10 ypos 170
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#F7F7F7"
                    
                    text u"活捉":
                        xpos 430 ypos 170
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                    text u"杀死":
                        xpos 740 ypos 170
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                if his_pactspire != False:

                    text u"（跳过）":
                        xpos 10 ypos 170
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#F7F7F7"
                        
                text u"沃尔斯塔外交官":
                    xpos 10 ypos 210
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"救出":
                    xpos 430 ypos 210
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"死亡":
                    xpos 740 ypos 210
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"                        

                text u"解救年糕号":
                    xpos 10 ypos 250
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"全军突击":
                    xpos 430 ypos 250
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"稳固防守":
                    xpos 740 ypos 250
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"        

                text u"医疗事故":
                    xpos 10 ypos 290
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"放了科洛特":
                    xpos 430 ypos 290
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"关押科洛特":
                    xpos 740 ypos 290
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"        

                text u"切嘉拉的道歉":
                    xpos 10 ypos 330
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"原谅切嘉拉":
                    xpos 430 ypos 330
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"批评切嘉拉":
                    xpos 740 ypos 330
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"        

                text u"与索拉的对话":
                    xpos 10 ypos 370
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"注意安全":
                    xpos 430 ypos 370
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"干掉PACT":
                    xpos 740 ypos 370
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"        

                text u"安全规章":
                    xpos 10 ypos 410
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"支持伊卡莉":
                    xpos 430 ypos 410
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"支持科莉斯卡":
                    xpos 740 ypos 410
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"        

                text u"餐厅谈话":
                    xpos 10 ypos 450
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"支持阿萨嘉":
                    xpos 430 ypos 450
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"支持切嘉拉":
                    xpos 740 ypos 450
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"        

                text u"关于名声":
                    xpos 10 ypos 490
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"不在乎":
                    xpos 430 ypos 490
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"用来对抗PACT":
                    xpos 740 ypos 490
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    

                text u"关于联盟":
                    xpos 10 ypos 530
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"不信任":
                    xpos 430 ypos 530
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"信任":
                    xpos 740 ypos 530
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    

                text u"悖论计划":
                    xpos 10 ypos 570
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"危险":
                    xpos 430 ypos 570
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"有用":
                    xpos 740 ypos 570
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    

                text u"海滩事件1":
                    xpos 10 ypos 610
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"阿萨嘉":
                    xpos 430 ypos 610
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"切嘉拉":
                    xpos 740 ypos 610
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"艾瓦":
                    xpos 430 ypos 650
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"伊卡莉和科莉斯卡":
                    xpos 740 ypos 650
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"科洛特":
                    xpos 430 ypos 690
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"索拉":
                    xpos 740 ypos 690
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"海滩事件2":
                    xpos 10 ypos 730
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                if his_beach1 != 1:
                
                    text u"阿萨嘉":
                        xpos 430 ypos 730
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                if his_beach1 != 2:
                        
                    text u"切嘉拉":
                        xpos 740 ypos 730
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"    
                        
                if his_beach1 != 3:
                        
                    text u"艾瓦":
                        xpos 430 ypos 770
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                if his_beach1 != 4:
                        
                    text u"伊卡莉和科莉斯卡":
                        xpos 740 ypos 770
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"    
                        
                if his_beach1 != 5:
                        
                    text u"科洛特":
                        xpos 430 ypos 810
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                if his_beach1 != 6:
                        
                    text u"索拉":
                        xpos 740 ypos 810
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"  
                    
                text "海滩事件3":
                    xpos 10 ypos 850
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                    
                if his_beach1 != 1 and his_beach2 != 1:
                
                    text u"阿萨嘉":
                        xpos 430 ypos 850
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                if his_beach1 != 2 and his_beach2 != 2:
                        
                    text u"切嘉拉":
                        xpos 740 ypos 850
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"    
                        
                if his_beach1 != 3 and his_beach2 != 3:
                        
                    text u"艾瓦":
                        xpos 430 ypos 890
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                if his_beach1 != 4 and his_beach2 != 4:
                        
                    text u"伊卡莉和科莉斯卡":
                        xpos 740 ypos 890
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"    
                        
                if his_beach1 != 5 and his_beach2 != 5:
                        
                    text u"科洛特":
                        xpos 430 ypos 930
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"

                if his_beach1 != 6 and his_beach2 != 6:

                    text u"索拉":
                        xpos 740 ypos 930
                        font "NotoSansCJKsc-Regular.otf"
                        size 20
                        color "#000000"
                        
                text u"索拉的母亲":
                    xpos 10 ypos 970
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"幼稚":
                    xpos 430 ypos 970
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"同情":
                    xpos 740 ypos 970
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"索拉的过去":
                    xpos 10 ypos 1010
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"保护她":
                    xpos 430 ypos 1010
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"她很勇敢":
                    xpos 740 ypos 1010
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"瑟拉逃兵":
                    xpos 10 ypos 1050
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"接纳":
                    xpos 430 ypos 1050
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"处决":
                    xpos 740 ypos 1050
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"愿望机":
                    xpos 10 ypos 1090
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"用掉":
                    xpos 430 ypos 1090
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"保留":
                    xpos 740 ypos 1090
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"联盟选举":
                    xpos 10 ypos 1130
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"格雷上将":
                    xpos 430 ypos 1130
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"平民政府":
                    xpos 740 ypos 1130
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"关于昂格斯贫民窟":
                    xpos 10 ypos 1170
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"联盟救济":
                    xpos 430 ypos 1170
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"独立自主":
                    xpos 740 ypos 1170
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"死伤事件":
                    xpos 10 ypos 1210
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"披露":
                    xpos 430 ypos 1210
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"隐瞒":
                    xpos 740 ypos 1210
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"关于联盟":
                    xpos 10 ypos 1250
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"信任":
                    xpos 430 ypos 1250
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"怀疑":
                    xpos 740 ypos 1250
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"格雷的赌博":
                    xpos 10 ypos 1290
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"支持":
                    xpos 430 ypos 1290
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"反对":
                    xpos 740 ypos 1290
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"    
                    
                text u"军团号":
                    xpos 10 ypos 1330
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"
                
                text u"沉没":
                    xpos 430 ypos 1330
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
                text u"存活":
                    xpos 740 ypos 1330
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#000000"
                    
            frame:
                
                background "#000000"
                xpos httx+200 ypos htty-history_box+20
            
                text htt.value:
                    font "NotoSansCJKsc-Regular.otf"
                    size 20
                    color "#F7F7F7"

        vbar value YScrollValue("history_box") xpos 1070
        
    if his_ceraflag != None and his_professionalreunion != None and his_loosenrule != None and his_pactspire == True and his_diplomatssaved != None and his_mochirescue != None and his_claudesupport != None and his_chigaraforgive != None and his_solacareful != None and his_noallianceregulations != None and his_cafeteriaasaga != None and his_notinterestedinfame != None and his_beforefarportsuspectalliance != None and his_techdangerous != None and his_beach1 != None and his_beach2 != None and his_beach3 != None and his_mothernaive != None and his_solaprotect != None and his_acquitteddeserters != None and his_soldwishall != None and his_backgrey != None and his_supportrelief != None and his_gotopress != None and his_backalliance != None and his_suppportnuke != None and his_legionsank != None and validate_beach_decision():
        
        imagebutton at tr_fadein(0):
            xpos 805 ypos 125
            idle "UI/confirm.png"
            hover tr_hoverglow("UI/confirm.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/ButtonClick.ogg"
            action SetVariable("customstat",True),Start()

    if his_ceraflag != None and his_professionalreunion != None and his_loosenrule != None and his_pactspire == False and his_capturetraffickers != None and his_diplomatssaved != None and his_mochirescue != None and his_claudesupport != None and his_chigaraforgive != None and his_solacareful != None and his_noallianceregulations != None and his_cafeteriaasaga != None and his_notinterestedinfame != None and his_beforefarportsuspectalliance != None and his_techdangerous != None and his_beach1 != None and his_beach2 != None and his_beach3 != None and his_mothernaive != None and his_solaprotect != None and his_acquitteddeserters != None and his_soldwishall != None and his_backgrey != None and his_supportrelief != None and his_gotopress != None and his_backalliance != None and his_suppportnuke != None and his_legionsank != None and validate_beach_decision():
        
        imagebutton at tr_fadein(0):
            xpos 805 ypos 125
            idle "UI/confirm.png"
            hover tr_hoverglow("UI/confirm.png")
            hover_sound "sound/hover1.ogg"
            activate_sound "sound/ButtonClick.ogg"
            action SetVariable("customstat",True),Start()
    
screen prolog:
    
    frame:
        
        background None
        xpos 200 xmaximum 1520 yalign 0.5
        text what id "what" font "NotoSansCJKsc-Regular.otf" size 35
    
screen quick_menu:
    if not hasattr(BM,'supress_menu'):
        $BM.supress_menu = False
    if (BM.phase == 'Player' or BM.phase == 'formation') and (BM.battlemode == False or BM.supress_menu == False):
        key "mouseup_3" action If(True,true=(FileTakeScreenshot(),If(show_sidemenu, true=(Hide("sidebuttons"),SetVariable("show_sidemenu", False)), false=(Show("sidebuttons"),SetVariable("show_sidemenu", True)))),false=NullAction())
    elif BM.supress_menu and BM.selected is None:
        key "mouseup_3" action SetField(BM,'supress_menu',False)
    
    zorder 350
    imagebutton:
        xpos 1755
        idle "UI/menu.png"
        hover tr_hoverglow("UI/menu.png")
        
        activate_sound "sound/button1.ogg"
        action If((BM.phase == 'Player' or BM.phase == 'formation'),[FileTakeScreenshot(),If(show_sidemenu, true=(Hide("sidebuttons"),SetVariable("show_sidemenu", False)), false=(Show("sidebuttons"),SetVariable("show_sidemenu", True)))],NullAction())
    
screen sidebuttons:
    
    zorder 300
    
    if show_sidemenu == True:
        imagebutton:
            idle "UI/menu_qsave.png"
            hover tr_hoverglow("UI/menu_qsave.png")
            
            activate_sound "sound/button1.ogg"
            action (QuickSave(message='                                   Quick save complete.', newest=False),Hide("sidebuttons"),SetVariable("show_sidemenu", False))
            at tr_sidemenu(100)
        imagebutton:
            idle "UI/menu_save.png"
            hover tr_hoverglow("UI/menu_save.png")
            
            activate_sound "sound/button1.ogg"
            action If(show_save, true=(Hide("save"),SetVariable("show_save",False)), false=(Show("save"),SetVariable("show_save",True)))
            at tr_sidemenu(150)
        imagebutton:
            idle "UI/menu_load.png"
            hover tr_hoverglow("UI/menu_load.png")
            
            activate_sound "sound/button1.ogg"
            action If(show_load, true=(Hide("load"),SetVariable("show_load",False)), false=(Show("load"),SetVariable("show_load",True)))
            at tr_sidemenu(200)
        imagebutton:
            idle "UI/menu_options.png"
            hover tr_hoverglow("UI/menu_options.png")
            
            activate_sound "sound/button1.ogg"
            action If(show_preference, true=(Hide("preferences"),SetVariable("show_preference",False)), false=(Show("preferences"),SetVariable("show_preference",True)))
            at tr_sidemenu(250)
        
        $hideui_action = NullAction() if (BM.battlemode or 'victory2' in renpy.get_showing_tags('screens')) else HideInterface()
        imagebutton:
            idle "UI/menu_hideui.png"
            hover tr_hoverglow("UI/menu_hideui.png")
            
            activate_sound "sound/button1.ogg"
            action hideui_action
            at tr_sidemenu(300)
        
        imagebutton:
            idle "UI/menu_auto.png"
            hover tr_hoverglow("UI/menu_auto.png")
            
            activate_sound "sound/button1.ogg"
            action Preference("auto-forward", "toggle")
            at tr_sidemenu(350)
        
        $screenshot_action = Screenshot() if (BM.battlemode or 'victory2' in renpy.get_showing_tags('screens')) else (HideInterface(),Screenshot())
        imagebutton:
            idle "UI/menu_screenshot.png"
            hover tr_hoverglow("UI/menu_screenshot.png")
            
            activate_sound "sound/button1.ogg"
            action screenshot_action
            at tr_sidemenu(400)
            
        imagebutton:
            idle "UI/menu_quit.png"
            hover tr_hoverglow("UI/menu_quit.png")
            
            activate_sound "sound/button1.ogg"
            action MainMenu(confirm=True)
            at tr_sidemenu(450)
            
screen leftbuttons:
    
    if not 'ship_map' in renpy.get_showing_tags():
        add "UI/circle.png":
            xpos 0 ypos 5
        
        imagebutton:
            xpos 10 ypos 25
            idle "UI/button_research.png"
            hover tr_hoverglow("UI/button_research.png")
            activate_sound "sound/beep1.ogg"
            action ShowUpgrades()
        imagebutton:
            xpos 10 ypos 92
            idle "UI/button_store.png"
            hover tr_hoverglow("UI/button_store.png")
            activate_sound "sound/beep1.ogg"
            action ShowStore()
            
screen wishall_cosettedead:
    
    zorder 300
    xpos 1520
    ypos 300
                
    imagebutton:
        idle tr_hoverglow("UI/usewishall.png")
        hover tr_hoverglow("UI/usewishall.png")
        activate_sound "sound/battle.ogg"
        action SetVariable("wishall_kill",False),SetVariable("wishall",False),Hide("wishall_cosettedead")
    text "SPARE COSETTE":
        xpos 160 ypos 90
        font "NotoSansCJKsc-Regular.otf"
        size 20
        color "#F7F7F7"
            
screen battlewarning:
    
    modal True
    
    add "UI/battlestations_bar.png" at tr_fadein(0.5):
        ypos 400 xalign 0.5
    
    add "UI/battlestations_menuback.png" at tr_fadein(0.5):
        ypos 500 xalign 0.5
        
    add "UI/battlestations.png" at tr_battlestations
    
    imagebutton at tr_menubutton(0.55,807):
        ypos 550
        idle "UI/battlestations_quicksave.png"
        hover tr_hoverglow("UI/battlestations_quicksave.png")
        activate_sound "sound/beep1.ogg"
        action QuickSave(message='Quick save complete.', newest=False)
    
    imagebutton at tr_menubutton(0.6,807):
        ypos 620
        idle "UI/battlestations_research.png"
        hover tr_hoverglow("UI/battlestations_research.png")
        activate_sound "sound/beep1.ogg"
        action ShowUpgrades()

    imagebutton at tr_menubutton(0.65,807):
        ypos 690
        idle "UI/battlestations_store.png"
        hover tr_hoverglow("UI/battlestations_store.png")
        activate_sound "sound/beep1.ogg"
        action ShowStore()

    imagebutton at tr_menubutton(0.7,807):
        ypos 760
        idle "UI/battlestations_proceed.png"
        hover tr_hoverglow("UI/battlestations_proceed.png")
        activate_sound "sound/drum.ogg"
        action Return('continue')

screen gallery_back:
    
    zorder 1200
    modal True

    add "UI/bonus_back.png":
        xalign 0.5 yalign 0.5
    vbox:

        xpos 1260 ypos 250
        xsize 470
        ysize 740
        
        
        if renpy.seen_label("postcredits") == True:
            if show_charactercg == False:

                imagebutton:
                    idle "UI/bonus_charactercg_base.png"
                    hover "UI/bonus_charactercg_hover.png"
                    action If(show_charactercg, true=(Hide("gallery_charactercg")), false=(Show("gallery_charactercg"))),ToggleVariable("show_charactercg",true_value=True, false_value=False),SetVariable("show_mechacg",False),SetVariable("show_backgrounds",False),SetVariable("show_music",False),SetVariable("show_chivos",False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                    
            if show_charactercg == True:
                    
                imagebutton:
                    idle "UI/bonus_charactercg_selected.png"
                    hover "UI/bonus_charactercg_selected_hover.png"
                    action If(show_charactercg, true=(Hide("gallery_charactercg")), false=(Show("gallery_charactercg"))),ToggleVariable("show_charactercg",true_value=True, false_value=False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                    
            if show_mechacg == False:
                    
                imagebutton:
                    idle "UI/bonus_mechacg_base.png"
                    hover "UI/bonus_mechacg_hover.png"
                    action If(show_mechacg, true=(Hide("gallery_mechacg")), false=(Show("gallery_mechacg"))),ToggleVariable("show_mechacg",true_value=True, false_value=False),SetVariable("show_charactercg",False),SetVariable("show_backgrounds",False),SetVariable("show_music",False),SetVariable("show_chivos",False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                    
            if show_mechacg == True:
                
                imagebutton:
                    idle "UI/bonus_mechacg_selected.png"
                    hover "UI/bonus_mechacg_selected_hover.png"
                    action If(show_mechacg, true=(Hide("gallery_mechacg")), false=(Show("gallery_mechacg"))),ToggleVariable("show_mechacg",true_value=True, false_value=False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"

            if show_backgrounds == False:
                
                imagebutton:
                    idle "UI/bonus_backgrounds_base.png"
                    hover "UI/bonus_backgrounds_hover.png"
                    action If(show_backgrounds, true=(Hide("gallery_backgrounds")), false=(Show("gallery_backgrounds"))),ToggleVariable("show_backgrounds",true_value=True, false_value=False),SetVariable("show_mechacg",False),SetVariable("show_charactercg",False),SetVariable("show_music",False),SetVariable("show_chivos",False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                    
            if show_backgrounds == True:
                
                imagebutton:
                    idle "UI/bonus_backgrounds_selected.png"
                    hover "UI/bonus_backgrounds_selected_hover.png"
                    action If(show_backgrounds, true=(Hide("gallery_backgrounds")), false=(Show("gallery_backgrounds"))),ToggleVariable("show_backgrounds",true_value=True, false_value=False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"

                    
            if show_music == False:
                    
                imagebutton:
                    idle "UI/bonus_music_base.png"
                    hover "UI/bonus_music_hover.png"
                    action If(show_music, true=(Hide("gallery_music")), false=(Show("gallery_music"))),ToggleVariable("show_music",true_value=True, false_value=False),SetVariable("show_charactercg",False),SetVariable("show_mechacg",False),SetVariable("show_backgrounds",False),SetVariable("show_chivos",False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"

            if show_music == True:
                    
                imagebutton:
                    idle "UI/bonus_music_selected.png"
                    hover "UI/bonus_music_selected_hover.png"
                    action If(show_music, true=(Hide("gallery_music")), false=(Show("gallery_music"))),ToggleVariable("show_music",true_value=True, false_value=False)
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                    
        if renpy.seen_label("postcredits") == False:
            
            add "UI/bonus_charactercg_locked.png"
            add "UI/bonus_mechacg_locked.png"
            add "UI/bonus_backgrounds_locked.png"
            add "UI/bonus_music_locked.png"
                
        if show_chivos == False:
            
            imagebutton:
                idle "UI/bonus_achievements_base.png"
                hover "UI/bonus_achievements_hover.png"
                action If(show_chivos, true=(Hide("gallery_achievements")), false=(Show("gallery_achievements"))),ToggleVariable("show_chivos",true_value=True, false_value=False),SetVariable("show_charactercg",False),SetVariable("show_mechacg",False),SetVariable("show_music",False),SetVariable("show_backgrounds",False)
                hover_sound "Sound/hover1.ogg"
                activate_sound "Sound/button1.ogg"
                
        if show_chivos == True:
            
            imagebutton:
                idle "UI/bonus_achievements_selected.png"
                hover "UI/bonus_achievements_selected_hover.png"
                action If(show_chivos, true=(Hide("gallery_achievements")), false=(Show("gallery_achievements"))),ToggleVariable("show_chivos",true_value=True, false_value=False)
                hover_sound "Sound/hover1.ogg"
                activate_sound "Sound/button1.ogg"
                
        imagebutton:
            idle "UI/bonus_back_base.png"
            hover "UI/bonus_back_hover.png"

            action Hide("gallery_back"),Hide("gallery_achievements"),Hide("page"),SetVariable("show_charactercg",False),SetVariable("show_chivos",False),SetVariable("show_mechacg",False),SetVariable("show_backgrounds",False),SetVariable("show_music",False)
            hover_sound "Sound/hover1.ogg"
            activate_sound "Sound/button1.ogg"

screen gallery_music:
    
    tag page
    
    zorder 1300
    
    frame:
        area (245,265,980,700)
        background None
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (920,1015)
            
            grid 3 6:
                
                xfill True
                yfill True
                        
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Anguish.ogg")
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Camino.ogg")
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Colors_of_an_Orchestra_II.ogg")
                    hover_sound "Sound/hover1.ogg"
                    activate_sound "Sound/button1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Cracking_the_Code.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Danger.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Destinys_Path.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Epic_Action_Hero.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Fallen_Angel.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Gore_and_Sand.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Love_Theme.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/MarduksWrath.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Monkeys_Spinning_Monkeys.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Posthumus_Regnum.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/Riding_With_the_Wind.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/The_Bladed_Druid.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/The_Final_Battle.ogg")
                    hover_sound "Sound/hover1.ogg"
                imagebutton:
                    idle "UI/bonus_song_base.png"
                    hover "UI/bonus_song_hover.png"
                    insensitive "CG/thumbs/locked.jpg"
                    selected_idle "UI/bonus_song_baseplay.png"
                    selected_hover "UI/bonus_song_hoverplay.png"
                    action mr.Play("Music/VolatileReaction.ogg")
                    hover_sound "Sound/hover1.ogg"
                text " "
                
            grid 3 6:
                
                xfill True
                yfill True
                        
                text "Anguish" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Camino" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Colors of an Orchestra II" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                
                text "Cracking the Code" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Danger" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Destinys Path" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                
                text "Epic Action Hero" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Fallen Angel" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Gore and Sand" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                
                text "Love Theme" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Marduks Wrath" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Monkeys Spinning Monkeys" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                
                text "Posthumus Regnum" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "Riding With the Wind" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "The Bladed Druid" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                
                text "The Final Battle" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text "VolatileReaction" ysize 10 color "#000000" font "Fonts/SourceCodePro-Regular.ttf" size 15 xalign 0.5 ypos 100
                text " "

screen gallery_charactercg:
    
    tag page
    
    zorder 1300
    
    frame:
        area (245,265,980,700)
        background None
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (920,2200)
        
            grid 3 13:
                
                xfill True
                yfill True

                # Call make_button to show a particular button.
                
                if CENSOR == True:
                
                    add gallery.make_button("chcg1", "CG/thumbs/intro_helion.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg2", "CG/thumbs/chigara_cockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg3", "CG/thumbs/lynn_cockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    
                    add gallery.make_button("chcg4", "CG/thumbs/cosette_attack.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg5", "CG/thumbs/asagacockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg7", "CG/thumbs/shower1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    
                    add gallery.make_button("chcg6", "CG/thumbs/lynn_brig1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg8", "CG/thumbs/cosette_jail.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg9", "CG/thumbs/ava_sickbay1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    
                    add gallery.make_button("chcg10", "CG/thumbs/asaga_reflection1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg11", "CG/thumbs/lynn_interrogation1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg12", "CG/thumbs/chigara_tea1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg13", "CG/thumbs/hangar_celebration.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg14", "CG/thumbs/asaga_jealous.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg15", "CG/thumbs/messhallparty1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg16", "CG/thumbs/chigaralap1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg17", "CG/thumbs/icaricockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg18", "CG/thumbs/claudecockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg19", "CG/thumbs/solacockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg20", "CG/thumbs/chigarah1c.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg21", "CG/thumbs/asaga_fall.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg22", "CG/thumbs/chigarah2c.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg23", "CG/thumbs/fight1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg24", "CG/thumbs/kryska_cockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg25", "CG/thumbs/chigaramindstream1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg26", "CG/thumbs/chigaramindstream2.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg27", "CG/thumbs/alice_cockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg28", "CG/thumbs/over.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg29", "CG/thumbs/twist1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg30", "CG/thumbs/dronedrop1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg31", "CG/thumbs/ondrone1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg32", "CG/thumbs/kaytokiss1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg33", "CG/thumbs/dead1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg34", "CG/thumbs/swornenemies1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg35", "CG/thumbs/swornenemies2.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg36", "CG/thumbs/standoff1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg37", "CG/thumbs/kaytoend1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg39", "CG/thumbs/helives.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg38", "CG/thumbs/despair.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)


                if CENSOR == False:
                    
                    add gallery.make_button("chcg1", "CG/thumbs/intro_helion.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg2", "CG/thumbs/chigara_cockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg3", "CG/thumbs/lynn_cockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    
                    add gallery.make_button("chcg4", "CG/thumbs/cosette_attack.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg5", "CG/thumbs/asagacockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg7", "Censored/thumbs/shower1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    
                    add gallery.make_button("chcg6", "CG/thumbs/lynn_brig1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg8", "CG/thumbs/cosette_jail.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg9", "CG/thumbs/ava_sickbay1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    
                    add gallery.make_button("chcg10", "CG/thumbs/asaga_reflection1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg11", "CG/thumbs/lynn_interrogation1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg12", "CG/thumbs/chigara_tea1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg13", "CG/thumbs/hangar_celebration.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg14", "CG/thumbs/asaga_jealous.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg15", "CG/thumbs/messhallparty1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg16", "CG/thumbs/chigaralap1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg17", "CG/thumbs/icaricockpit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg18", "CG/thumbs/claudecockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg19", "CG/thumbs/solacockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg20", "Censored/thumbs/chigarah.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg21", "CG/thumbs/asaga_fall.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg22", "Censored/thumbs/chigarah2.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg23", "CG/thumbs/fight1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg24", "CG/thumbs/kryska_cockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg25", "CG/thumbs/chigaramindstream1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg26", "CG/thumbs/chigaramindstream2.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg27", "CG/thumbs/alice_cockpit1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg28", "CG/thumbs/over.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg29", "CG/thumbs/twist1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg30", "CG/thumbs/dronedrop1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg31", "CG/thumbs/ondrone1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg32", "CG/thumbs/kaytokiss1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg33", "CG/thumbs/dead1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg34", "CG/thumbs/swornenemies1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg35", "CG/thumbs/swornenemies2.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg36", "CG/thumbs/standoff1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                    add gallery.make_button("chcg37", "CG/thumbs/kaytoend1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg38", "CG/thumbs/despair.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                    add gallery.make_button("chcg39", "CG/thumbs/helives.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
            
screen gallery_mechacg:
    
    tag page
    
    zorder 1300
    
    frame:
        area (245,265,980,700)
        background None
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (920,2370)
    
            grid 3 14:

                xfill True
                yfill True
                
                add gallery.make_button("mccg1", "3DCG/thumbs/piratesapproach.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/havochit.jpg"
                    hover "3DCG/thumbs/havochit_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_havochit",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/havocfly.jpg"
                    hover "3DCG/thumbs/havocfly_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_havochitfly",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/havocattack.jpg"
                    hover "3DCG/thumbs/havocattack_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_havocattack",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/blackjack_hit.jpg"
                    hover "3DCG/thumbs/blackjack_hit_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_blackjackhit",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/blackjack_fly.jpg"
                    hover "3DCG/thumbs/blackjack_fly_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_blackjackfly",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/blackjacklaser.jpg"
                    hover "3DCG/thumbs/blackjacklaser_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_blackjacklaser",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/havochitlaser.jpg"
                    hover "3DCG/thumbs/havochitlaser_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_havochitlaser",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                    
                if renpy.seen_label("prologue_cosettedead") == True:
                    imagebutton:
                        xpos 13
                        idle "3DCG/thumbs/blackjack_pulse.jpg"
                        hover "3DCG/thumbs/blackjack_pulse_hover.jpg"
                        insensitive "CG/thumbs/locked.jpg"
                        action Replay("replay_blackjack_pulse",locked=False)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                else:
                    imagebutton:
                        xpos 13
                        idle "3DCG/thumbs/blackjack_pulse.jpg"
                        hover "3DCG/thumbs/blackjack_pulse_hover.jpg"
                        insensitive "CG/thumbs/locked.jpg"
                        action Replay("replay_blackjack_pulse",locked=True)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg2", "3DCG/thumbs/havoc_dead.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/titlecard.jpg"
                    hover "3DCG/thumbs/titlecard_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_titlecard",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg3", "3DCG/thumbs/coreexplode1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/sunrider_warp.jpg"
                    hover "3DCG/thumbs/sunrider_warp_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_sunrider_warp",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg4", "3DCG/thumbs/diode.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg5", "3DCG/thumbs/returntocera.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg6", "3DCG/thumbs/cera_pactfleet.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg7", "3DCG/thumbs/cera_pactryders.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg8", "3DCG/thumbs/battleshipapproach.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg9", "3DCG/thumbs/pactelite_attack1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg10", "3DCG/thumbs/liberty_sniped.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/seraphim_snipe.jpg"
                    hover "3DCG/thumbs/seraphim_snipe_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_seraphim_snipe",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg11", "3DCG/thumbs/ryderslaunch.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg12", "3DCG/thumbs/blackjack_attack.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg13", "3DCG/thumbs/bjbiancastop_back.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg14", "3DCG/thumbs/bianca_damaged1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/nightmare_approach.jpg"
                    hover "3DCG/thumbs/nightmare_approach_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_nightmareattack",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg15", "3DCG/thumbs/alliancefleet_damaged.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/vanguard_cut.jpg"
                    hover "3DCG/thumbs/vanguard_cut_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_vanguardcut",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg16", "3DCG/thumbs/nightmare_damaged.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg17", "3DCG/thumbs/nightmare_fire.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/blackjack_attack2.jpg"
                    hover "3DCG/thumbs/blackjack_attack2_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_blackjacknightmare",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                add gallery.make_button("mccg18", "3DCG/thumbs/goodvevil.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg19", "3DCG/thumbs/allshipsfire1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg20", "3DCG/thumbs/sunrider_hit.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg22", "3DCG/thumbs/blackjackseraphim.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg21", "3DCG/thumbs/collison.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("mccg23", "3DCG/thumbs/abyss.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                if renpy.seen_label("ava_sickbay") == True:
                    imagebutton:
                        xpos 13
                        idle "3DCG/thumbs/vanguard_eyepatch.jpg"
                        hover "3DCG/thumbs/vanguard_eyepatch_hover.jpg"
                        insensitive "CG/thumbs/locked.jpg"
                        action Replay("replay_vanguard_eyepatch",locked=False)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                else:
                    imagebutton:
                        xpos 13
                        idle "3DCG/thumbs/vanguard_eyepatch.jpg"
                        hover "3DCG/thumbs/vanguard_eyepatch_hover.jpg"
                        insensitive "CG/thumbs/locked.jpg"
                        action Replay("replay_vanguard_eyepatch",locked=True)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                if renpy.seen_label("ava_hallway") == True:
                    imagebutton:
                        xpos 13
                        idle "3DCG/thumbs/vanguard.jpg"
                        hover "3DCG/thumbs/vanguard_hover.jpg"
                        insensitive "CG/thumbs/locked.jpg"
                        action Replay("replay_vanguard_nopatch",locked=False)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                else:
                    imagebutton:
                        xpos 13
                        idle "3DCG/thumbs/vanguard.jpg"
                        hover "3DCG/thumbs/vanguard_hover.jpg"
                        insensitive "CG/thumbs/locked.jpg"
                        action Replay("replay_vanguard_nopatch",locked=True)
                        hover_sound "sound/hover1.ogg"
                        activate_sound "sound/button1.ogg"
                imagebutton:
                    xpos 13
                    idle "3DCG/thumbs/op.jpg"
                    hover "3DCG/thumbs/op_hover.jpg"
                    insensitive "CG/thumbs/locked.jpg"
                    action Replay("replay_op",locked=False)
                    hover_sound "sound/hover1.ogg"
                    activate_sound "sound/button1.ogg"
                text ""
                text ""


screen gallery_backgrounds:
    
    tag page
    
    zorder 1300
    
    frame:
        area (245,265,980,700)
        background None
        
        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"
            child_size (920,1185)
        
            grid 3 7:
                
                xfill True
                yfill True
                
                add gallery.make_button("bg1", "Background/thumbs/bridge.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg2", "Background/thumbs/assaultcarrierbridge.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg3", "Background/thumbs/sickbay.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                add gallery.make_button("bg4", "Background/thumbs/messhallwindows.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg5", "Background/thumbs/hallway.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg6", "Background/thumbs/crewcabin.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                add gallery.make_button("bg7", "Background/thumbs/controlroom.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg8", "Background/thumbs/office.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg9", "Background/thumbs/captainscabin.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                add gallery.make_button("bg10", "Background/thumbs/hangar.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg11", "Background/thumbs/stateroom.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg12", "Background/thumbs/messhall.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                add gallery.make_button("bg13", "Background/thumbs/clonelab.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg14", "Background/thumbs/brig.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg15", "Background/thumbs/awardhall.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                add gallery.make_button("bg16", "Background/thumbs/awardhall_fire.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg17", "Background/thumbs/airlock.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg18", "Background/thumbs/escapepod.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)

                add gallery.make_button("bg19", "Background/thumbs/cargohangar.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg20", "Background/thumbs/mindstream1.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
                add gallery.make_button("bg21", "Background/thumbs/desert.jpg", locked="CG/thumbs/locked.jpg",hover_border="CG/thumbs/hover.png", idle_border=None, hover_sound="Sound/hover1.ogg",activate_sound="Sound/button1.ogg", background=None)
