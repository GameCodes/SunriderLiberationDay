init -1 python:
    
    CENSOR = True
    menu_hover = 0
    config.auto_voice = "sound/Voice/{id}.ogg"
    difficulty = 3
    tty = -5000
    httx = 0
    htty = -5000
    history_box = 0
    customstat = False
    mp = MultiPersistent("Sunrider")
    
    config.keymap['game_menu'].remove('K_ESCAPE')
    # config.keymap['game_menu'].remove('mouseup_3')
    
    show_load = False
    show_preference = False
    show_sidemenu = False
    option_show = 1
    show_save = False
    
    his_ceraflag = None
    his_professionalreunion = None
    his_loosenrule = None
    his_pactspire = None
    his_capturetraffickers = None
    his_diplomatssaved = None
    his_mochirescue = None
    his_claudesupport = None
    his_chigaraforgive = None
    his_solacareful = None
    his_noallianceregulations = None
    his_cafeteriaasaga = None
    his_notinterestedinfame = None
    his_beforefarportsuspectalliance = None
    his_techdangerous = None
    his_beach1 = None
    his_beach2 = None
    his_beach3 = None
    his_mothernaive = None
    his_solaprotect = None
    his_acquitteddeserters = None
    his_soldwishall = None
    his_backgrey = None
    his_supportrelief = None
    his_gotopress = None
    his_backalliance = None
    his_suppportnuke = None
    his_legionsank = None
    
    captain_prince = 0
    captain_moralist = 0
    
    affection_ava = 0
    affection_asaga = 0
    affection_chigara = 0
    affection_icari = 0
    affection_claude = 0
    affection_sola = 0
    affection_cosette = 0
    affection_kryska = 0
    
    bcheck1 = False
    bcheck2 = False
    bcheck3 = False
    bcheck4 = False
    bcheck5 = False
    bcheck6 = False
    bcheck7 = False
    bcheck8 = False
    bcheck9 = False
    
    renpy.music.register_channel("movie", "sfx")
    
    wishall = None
    Saveddiplomats = None
    OngessTruth = None
    legion_destroyed = None
    discoverfalcon = False
    havoc_save = True
    
    wishall_kill = None
    
    decision_extra = False
    choice1_text = 0
    choice1_jump = 0
    
    choice2_text = 0
    choice2_jump = 0
    
    debugbuttons = False
    
    show_charactercg = False
    show_mechacg = False
    show_backgrounds = False
    show_music = False
    show_chivos = False
    
    cmap_firstavatalk = False
    cmap_chigarawindows = False
    cmap_firstcaptainslog = False
    cmap_icarikryeating = False
    cmap_avaprotodiscovery = False
    cmap_hangarlecture = False
    cmap_chigaratea = False
    
    ava_location = None
    asa_location = None
    chi_location = None
    ica_location = None
    cla_location = None
    sol_location = None
    kry_location = None
    pro_location = None
    cal_location = "captainsloft"
    res_location = "lab"
    gal_location = None
    
    ava_event = None
    asa_event = None
    chi_event = None
    ica_event = None
    cla_event = None
    sol_event = None
    kry_event = None
    pro_event = None
    gal_event = None
    
    galaxymission1 = False
    galaxymission2 = False
    galaxymission3 = False
    mission1 = None
    mission2 = None
    mission3 = None
    mission1_name = None
    mission2_name = None
    mission3_name = None
    
    warpto_tydaria = True
    warpto_occupiedcera = True
    warpto_astralexpanse = True
    warpto_pactstation1 = False
    warpto_versta = True
    warpto_nomodorn = True
    warpto_ryuvia = True
    warpto_farport = True
    warpto_ongess = True
    warpto_pacemus = True
    
    ########## GALLERY

    gallery = Gallery()
    
    #########CHARACTER CGS
        
    gallery.button("chcg1")
    gallery.unlock_image("intro_helion")
    gallery.transform(tr_center)
    
    gallery.button("chcg2")
    gallery.unlock_image("chigara_shock")
    gallery.unlock_image("chigara_cockpit_lightning")
    gallery.unlock_image("chigara_cockpit_orb")
    gallery.unlock_image("cockpit_chigara")

    gallery.button("chcg3")
    gallery.unlock_image("lynn_cockpit")
    gallery.unlock_image("lynn_cockpit_lightning")
    gallery.unlock_image("lynn_cockpit_space1")
    gallery.unlock_image("lynn_cockpit_space2")

    gallery.button("chcg4")
    gallery.unlock_image("cosette_attack")
    gallery.unlock_image("cosette_attack_lines")
    gallery.unlock_image("cosette_attack_blood")
    gallery.unlock_image("cosette_attack_bloodlaugh")
    gallery.unlock_image("cosette_attack_bloodcry")
    gallery.unlock_image("cosette_escape")

    gallery.button("chcg5")
    gallery.unlock_image("asagacockpit")
    gallery.unlock_image("asagacockpit_awaken")
    gallery.unlock_image("asagacockpit_awaken_sun")
    gallery.unlock_image("asagacockpitsurprise")
    gallery.unlock_image("asagacockpit_lightning")
    gallery.unlock_image("asagacockpit2_lightning")
    gallery.unlock_image("asagacockpit_orb")
    gallery.unlock_image("asagacockpit3")
    gallery.unlock_image("asagacockpit4")
    gallery.unlock_image("asagacockpit5")
    gallery.unlock_image("asagacockpit6")
    gallery.unlock_image("asagacockpit7")
    gallery.unlock_image("asagacockpitsurprise_space")

    gallery.button("chcg6")
    gallery.unlock_image("lynn_brig1")
    gallery.unlock_image("lynn_brig2")
    gallery.unlock_image("lynn_escapepod1")
    gallery.unlock_image("lynn_escapepod2")

    if CENSOR == False:

        gallery.button("chcg7")
        gallery.unlock_image("h_shower1")
        gallery.transform(tr_center)
        gallery.unlock_image("h_shower2")
        gallery.transform(tr_center)
        gallery.unlock_image("h_shower3")
        gallery.transform(tr_center)
        gallery.unlock_image("h_shower4")
        gallery.transform(tr_center)
        gallery.unlock_image("h_shower5")
        gallery.transform(tr_center)
        
    if CENSOR == True:
        
        gallery.button("chcg7")
        gallery.unlock_image("shower1")
        gallery.transform(tr_center)
        gallery.unlock_image("shower2")
        gallery.transform(tr_center)
        gallery.unlock_image("shower3")
        gallery.transform(tr_center)
        gallery.unlock_image("shower4")
        gallery.transform(tr_center)
        gallery.unlock_image("shower5")
        gallery.transform(tr_center)

    gallery.button("chcg8")
    gallery.unlock_image("cosette_jail")

    gallery.button("chcg9")
    gallery.unlock_image("ava_sickbay1")
    gallery.unlock_image("ava_sickbay2")

    gallery.button("chcg10")
    gallery.unlock_image("asaga_reflection1")
    gallery.unlock_image("asaga_reflection2")

    gallery.button("chcg11")
    gallery.unlock_image("lynn_interrogation1")
    gallery.unlock_image("lynn_interrogation2")
    gallery.unlock_image("lynn_interrogation3")
    gallery.unlock_image("lynn_interrogation1glove")
    gallery.unlock_image("lynn_interrogation2glove")
    gallery.unlock_image("lynn_interrogation3glove")

    gallery.button("chcg12")
    gallery.unlock_image("chigara_tea1")
    gallery.unlock_image("chigara_tea2")
    gallery.unlock_image("chigara_tea3")
    gallery.unlock_image("chigara_tea4")
    gallery.unlock_image("chigara_tea5")
    gallery.unlock_image("chigara_tea6")

    gallery.button("chcg13")
    gallery.unlock_image("hangar_celebration")

    gallery.button("chcg14")
    gallery.unlock_image("asaga_jealous")

    gallery.button("chcg15")
    gallery.unlock_image("messhallparty1")

    gallery.button("chcg16")
    gallery.unlock_image("chigaralap1")
    gallery.unlock_image("chigaralap2")
    gallery.unlock_image("chigaralap3")
    gallery.unlock_image("chigaralap4")

    gallery.button("chcg17")
    gallery.unlock_image("icaricockpit")
    gallery.unlock_image("icaricockpit_orb")
    gallery.unlock_image("icaricockpit2")

    gallery.button("chcg18")
    gallery.unlock_image("claudecockpit1")
    gallery.unlock_image("claudecockpit_orb1")
    gallery.unlock_image("claudecockpit_orb2")
    gallery.unlock_image("claudecockpit2")
    gallery.unlock_image("claudecockpit3")
    gallery.unlock_image("claudecockpit4")

    gallery.button("chcg19")
    gallery.unlock_image("solacockpit1")
    gallery.unlock_image("solacockpit2")
    gallery.unlock_image("solacockpit_orb")
    gallery.unlock_image("solacockpit3")
    gallery.unlock_image("solacockpit4")
    gallery.unlock_image("solacockpit5")

    if CENSOR == False:

        gallery.button("chcg20")
        gallery.unlock_image("h_chigarah")
        
    if CENSOR == True:
    
        gallery.button("chcg20")
        gallery.unlock_image("chigarah1")

    gallery.button("chcg21")
    gallery.unlock_image("asaga_fall")

    if CENSOR == False:

        gallery.button("chcg22")
        gallery.unlock_image("h_chigarah2")
        gallery.unlock_image("h_chigarah3")
        
    if CENSOR == True:
        
        gallery.button("chcg22")
        gallery.unlock_image("chigarah2")
        gallery.unlock_image("chigarah3")

    gallery.button("chcg23")
    gallery.unlock_image("fight1")
    gallery.unlock_image("fight2")
    gallery.unlock_image("fight3")
    gallery.unlock_image("fight4")

    gallery.button("chcg24")
    gallery.unlock_image("kryska_cockpit_orb1")
    gallery.unlock_image("kryska_cockpit_orb2")
    gallery.unlock_image("kryska_cockpit1")
    gallery.unlock_image("kryska_cockpit2")

    gallery.button("chcg25")
    gallery.unlock_image("chigaramindstream")
    gallery.transform(tr_zoomout)

    gallery.button("chcg26")
    gallery.unlock_image("chigaramindstream2")
    gallery.unlock_image("chigaramindstream3")

    gallery.button("chcg27")
    gallery.unlock_image("alice_cockpit1")
    gallery.unlock_image("alice_cockpit2")
    gallery.unlock_image("alice_cockpit3")
    gallery.unlock_image("alice_cockpit4")
    gallery.unlock_image("alice_cockpit5")
    gallery.unlock_image("alice_cockpit6")

    gallery.button("chcg28")
    gallery.unlock_image("overhangar")

    gallery.button("chcg29")
    gallery.unlock_image("twist1")
    gallery.unlock_image("twist2")
    gallery.unlock_image("twist3")

    gallery.button("chcg30")
    gallery.unlock_image("dronedrop1")
    gallery.transform(tr_center)
    gallery.unlock_image("dronedrop2")
    gallery.unlock_image("dronedrop2","dronedrop3")
    gallery.unlock_image("dronedrop4")
    gallery.unlock_image("dronedrop5")
    gallery.unlock_image("dronedrop5","dronedrop6")

    gallery.button("chcg31")
    gallery.unlock_image("ondrone1")
    gallery.unlock_image("ondrone2")

    gallery.button("chcg32")
    gallery.unlock_image("kaytokiss1")
    gallery.unlock_image("kaytokiss1","kaytokiss2")

    gallery.button("chcg33")
    gallery.unlock_image("dead1")
    gallery.unlock_image("dead2")

    gallery.button("chcg34")
    gallery.unlock_image("swornenemies1")

    gallery.button("chcg35")
    gallery.unlock_image("swornenemies2")

    gallery.button("chcg36")
    gallery.unlock_image("standoff1")
    gallery.unlock_image("standoff2")
    gallery.unlock_image("standoff3")
    
    gallery.button("chcg37")
    gallery.unlock_image("kaytoend1")
    gallery.unlock_image("kaytoend2")
    gallery.unlock_image("kaytoend3")
    gallery.unlock_image("kaytoend4")

    gallery.button("chcg38")
    gallery.unlock_image("despair")
    
    gallery.button("chcg39")
    gallery.unlock_image("helives")
    gallery.unlock_image("helives_nopatch")

    #########MECHA CGS
    
    gallery.button("mccg1")
    gallery.unlock_image("piratesapproach")
    gallery.transform(tr_center)
    
    gallery.button("mccg2")
    gallery.unlock_image("havoc_dead")
    gallery.unlock_image("havocexplode")

    gallery.button("mccg3")
    gallery.unlock_image("coreexplode1")
    gallery.unlock_image("coreexplode2")

    gallery.button("mccg4")
    gallery.unlock_image("diode")

    gallery.button("mccg5")
    gallery.unlock_image("returntocera")
    gallery.transform(tr_center)

    gallery.button("mccg6")
    gallery.unlock_image("cera_pactfleet")
    
    gallery.button("mccg7")
    gallery.unlock_image("cera_pactryders")
    
    gallery.button("mccg8")
    gallery.unlock_image("battleshipapproach")
    
    gallery.button("mccg9")
    gallery.unlock_image("pactelite_attack1")
    gallery.unlock_image("pactelite_attack2")

    gallery.button("mccg10")
    gallery.unlock_image("libertyspin1")
    gallery.unlock_image("libertyspin2")

    gallery.button("mccg11")
    gallery.unlock_image("allryders_launch")

    gallery.button("mccg12")
    gallery.unlock_image("blackjack_attack")

    gallery.button("mccg13")
    gallery.unlock_image("bjbiancastop_back")
    gallery.unlock_image("bjbiancastop_back","bjbiancastop_bianca")

    gallery.button("mccg14")
    gallery.unlock_image("bianca_damaged1")
    gallery.unlock_image("bianca_damaged2")

    gallery.button("mccg15")
    gallery.unlock_image("alliancefleet_damaged")

    gallery.button("mccg16")
    gallery.unlock_image("nightmare_damaged")

    gallery.button("mccg17")
    gallery.unlock_image("nightmare_fire")
    gallery.unlock_image("nightmare_fire2")

    gallery.button("mccg18")
    gallery.unlock_image("goodvevil")

    gallery.button("mccg19")
    gallery.unlock_image("allshipsfire1")
    gallery.unlock_image("allshipsfire2")

    gallery.button("mccg20")
    gallery.unlock_image("sunrider_hit")
    
    gallery.button("mccg21")
    gallery.unlock_image("collison")
    
    gallery.button("mccg22")
    gallery.unlock_image("blackjackseraphim")
    
    gallery.button("mccg23")
    gallery.unlock_image("abyss")

    ############BACKGROUNDS

    gallery.button("bg1")
    gallery.unlock_image("bg bridge")
    gallery.unlock_image("bg bridge_damaged")

    gallery.button("bg2")
    gallery.unlock_image("bg pactbridge")
    
    gallery.button("bg3")
    gallery.unlock_image("bg sickbay")

    gallery.button("bg4")
    gallery.unlock_image("bg messhallwindows")
    gallery.unlock_image("bg messhallwindows_cera")

    gallery.button("bg5")
    gallery.unlock_image("bg hallway")
    gallery.unlock_image("bg hallway_distort")
    gallery.unlock_image("bg hallway_damaged")

    gallery.button("bg6")
    gallery.unlock_image("bg crewcabin")

    gallery.button("bg7")
    gallery.unlock_image("bg controlroom")

    gallery.button("bg8")
    gallery.unlock_image("bg office")

    gallery.button("bg9")
    gallery.unlock_image("bg captainscabin")

    gallery.button("bg10")
    gallery.unlock_image("bg hangar")

    gallery.button("bg11")
    gallery.unlock_image("bg stateroom")

    gallery.button("bg12")
    gallery.unlock_image("bg messhall")

    gallery.button("bg13")
    gallery.unlock_image("bg clonelab")

    gallery.button("bg14")
    gallery.unlock_image("bg brig")
    gallery.unlock_image("bg brig_damaged")

    gallery.button("bg15")
    gallery.unlock_image("bg awardhall")

    gallery.button("bg16")
    gallery.unlock_image("bg awardhall_destroyed")

    gallery.button("bg17")
    gallery.unlock_image("bg airlock")

    gallery.button("bg18")
    gallery.unlock_image("bg escapepod")
    gallery.unlock_image("bg escapepod_blue")

    gallery.button("bg19")
    gallery.unlock_image("bg cargohangar")

    gallery.button("bg20")
    gallery.unlock_image("bg mindstream1")
    gallery.unlock_image("bg mindstream2")

    gallery.button("bg21")
    gallery.unlock_image("bg desert")

    gallery.transition = dissolve
    
#########MUSIC

    mr = MusicRoom(channel='music', fadeout=1.0, fadein=0.0, loop=True, single_track=True, shuffle=False, stop_action=None)

    mr.add("Music/Anguish.ogg",always_unlocked=True)
    mr.add("Music/Camino.ogg",always_unlocked=True)
    mr.add("Music/Colors_of_an_Orchestra_II.ogg",always_unlocked=True)
    mr.add("Music/Cracking_the_Code.ogg",always_unlocked=True)
    mr.add("Music/Danger.ogg",always_unlocked=True)
    mr.add("Music/Destinys_Path.ogg",always_unlocked=True)
    mr.add("Music/Epic_Action_Hero.ogg",always_unlocked=True)
    mr.add("Music/Fallen_Angel.ogg",always_unlocked=True)
    mr.add("Music/Gore_and_Sand.ogg",always_unlocked=True)
    mr.add("Music/Love_Theme.ogg",always_unlocked=True)
    mr.add("Music/MarduksWrath.ogg",always_unlocked=True)
    mr.add("Music/Monkeys_Spinning_Monkeys.ogg",always_unlocked=True)
    mr.add("Music/Posthumus_Regnum.ogg",always_unlocked=True)
    mr.add("Music/Riding_With_the_Wind.ogg",always_unlocked=True)
    mr.add("Music/The_Bladed_Druid.ogg",always_unlocked=True)
    mr.add("Music/The_Final_Battle.ogg",always_unlocked=True)
    mr.add("Music/VolatileReaction.ogg",always_unlocked=True)
    
label bcheckset:
    $ bcheck1 = False
    $ bcheck2 = False
    $ bcheck3 = False
    $ bcheck4 = False
    $ bcheck5 = False
    $ bcheck6 = False
    $ bcheck7 = False
    $ bcheck8 = False
    $ bcheck9 = False
    
    return
    
init python:
    class AllVariables(store.object):
        def __init__(self):
            self.stat_prince = 0
            self.stat_justicar = 0
            self.affection_ava = 0
            self.affection_asaga = 0
            self.affection_chigara = 0
            self.affection_icari = 0
            self.affection_claude = 0
            self.affection_sola = 0
            self.affection_cosette = 0
            self.affection_kryska = 0

            self.battlemusic = True

            self.mission1_complete = False
            self.mission2_complete = False
            self.mission3_complete = False
            self.mission4_complete = False
            self.mission5_complete = False
            self.mission6_complete = False
            self.mission7_complete = False
            self.mission8_complete = False
            self.mission9_complete = False
            self.mission10_complete = False
            self.mission11_complete = False
            self.mission12_complete = False
            self.mission13_complete = False
            self.mission14_complete = False
            self.mission15_complete = False

            self.sunrider = None
            self.blackjack = None
            self.liberty = None
            self.phoenix = None
            self.bianca = None
            self.seraphim = None
            self.paradigm = None
            self.havoc = None
            self.paladin = None

            self.bcheck1 = False
            self.bcheck2 = False
            self.bcheck3 = False
            self.bcheck4 = False
            self.bcheck5 = False
            self.bcheck6 = False
            self.bcheck7 = False
            self.bcheck8 = False
            self.bcheck9 = False
            
            self.menu_hover = 0
            
            self.difficulty = 3
            self.tty = -5000
            self.httx = 0
            self.htty = -5000
            self.history_box = 0
            
            # self.config.keymap['game_menu'].remove('K_ESCAPE')
            # config.keymap['game_menu'].remove('mouseup_3')
            
            self.show_load = False
            self.show_preference = False
            self.show_sidemenu = False
            self.option_show = 1
            self.show_save = False

            ##new constants##

            self.TURN_SPEED = 0.5  #in seconds
            self.MOVE_IN_SPEED = 0.5 #for buttons and status displays
            self.MOVE_OUT_SPEED = 0.5
            self.MESSAGE_PAUSE = 0.75
            self.MISSILE_SPEED = 0.3
            self.SHIP_SPEED = 0.3
            self.ZOOM_SPEED = 0.1
            self.GRID_SIZE = (18,16)
    
    libday_mp = MultiPersistent("Liberation Day")
    
    
define kay = Character(u'凯托', what_outlines=[(5,"#000000", 1, 1),(2,"#575757", 0, 0)],who_outlines=[(5,"#000000",1,1),(3,"#575757",0,0)],ctc="ctc",ctc_position="fixed")
define asa = Character(u'阿萨嘉', what_outlines=[(5, "#000000", 1, 1),(2, "#be4c58", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#be4c58", 0, 0)],ctc="ctc",ctc_position="fixed")
define sha = Character(u'厦尔', what_outlines=[(5, "#000000", 1, 1),(2, "#26a3bc", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#26a3bc", 0, 0)],ctc="ctc",ctc_position="fixed")
define chi = Character(u'切嘉拉', what_outlines=[(5, "#000000", 1, 1),(2, "#615a9b", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#615a9b", 0, 0)],ctc="ctc",ctc_position="fixed")
define ava = Character(u'艾瓦', what_outlines=[(5, "#000000", 1, 1),(2, "#4A2A1A", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#4A2A1A", 0, 0)],ctc="ctc",ctc_position="fixed" )
define sol = Character(u'索拉', what_outlines=[(5, "#000000", 1, 1),(2, "#75798A", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#75798A", 0, 0)],ctc="ctc",ctc_position="fixed" )
define mar = Character(u'玛蕾', what_outlines=[(5, "#000000", 1, 1),(2, "#979797", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#979797", 0, 0)],ctc="ctc",ctc_position="fixed" )
define cro = Character(u'克劳', what_outlines=[(5, "#000000", 1, 1),(2, "#848484", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#848484", 0, 0) ],ctc="ctc",ctc_position="fixed"  )
define adr = Character(u'格雷', what_outlines=[(5, "#000000", 1, 1),(2, "#265739", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#265739", 0, 0)],ctc="ctc",ctc_position="fixed" )
define tut = Character(u'教程', what_outlines=[(5, "#000000", 1, 1),(2, "#323232", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#323232", 0, 0)],ctc="ctc",ctc_position="fixed" )
define narrator = Character(' ', what_outlines=[(5, "#000000", 1, 1),(2, "#272727", 0, 0) ],ctc="ctc",ctc_position="fixed")
define alp = Character(u'阿尔法', what_outlines=[(5, "#000000", 1, 1),(2, "#615a9b", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#615a9b", 0, 0)],ctc="ctc",ctc_position="fixed" )
define arc = Character(u'阿卡迪乌斯', what_outlines=[(5, "#000000", 1, 1),(2, "#701d2a", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#701d2a", 0, 0)],ctc="ctc",ctc_position="fixed" )
define ali = Character(u'爱丽丝', what_outlines=[(5, "#000000", 1, 1),(2, "#701d2a", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#701d2a", 0, 0)],ctc="ctc",ctc_position="fixed" )
define jay = Character(u'奥克朗', what_outlines=[(5, "#000000", 1, 1),(2, "#615a9b", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#615a9b", 0, 0)],ctc="ctc",ctc_position="fixed")
define pro = Character(u'原型', what_outlines=[(5, "#000000", 1, 1),(2, "#615a9b", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#615a9b", 0, 0) ],ctc="ctc",ctc_position="fixed" )
define lyn = Character(u'琳', what_outlines=[(5, "#000000", 1, 1),(2, "#615a9b", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#615a9b", 0, 0) ],ctc="ctc",ctc_position="fixed" )
define cla = Character(u'科洛特', what_outlines=[(5, "#000000", 1, 1),(2, "#e6a2c3", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#e6a2c3", 0, 0) ],ctc="ctc",ctc_position="fixed" )
define fon = Character(u'方特纳', what_outlines=[(5, "#000000", 1, 1),(2, "#3B0B39", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#3B0B39", 0, 0) ],ctc="ctc",ctc_position="fixed" )
define nar = Character('', what_outlines=[(5, "#000000", 1, 1),(2, "#615a9b", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#615a9b", 0, 0) ],ctc="ctc",ctc_position="fixed",what_ypos=-430)
define cul = Character(u'库仑', what_outlines=[(5, "#000000", 1, 1),(2, "#df6a3d", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#df6a3d", 0, 0) ],ctc="ctc",ctc_position="fixed" )
define ica = Character(u'伊卡莉', what_outlines=[(5, "#000000", 1, 1),(2, "dd9c38", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "dd9c38", 0, 0)],ctc="ctc",ctc_position="fixed" )
define kry = Character(u'科莉斯卡', what_outlines=[(5, "#000000", 1, 1),(2, "#3b3d66", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#3b3d66", 0, 0)],ctc="ctc",ctc_position="fixed" )
define cos = Character(u'柯赛特', what_outlines=[(5, "#000000", 1, 1),(2, "#d39980", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#d39980", 0, 0)],ctc="ctc",ctc_position="fixed" )
define pof = Character(u'PACT军官', what_outlines=[(5, "#000000", 1, 1),(2, "#d04545", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#d04545", 0, 0)],ctc="ctc",ctc_position="fixed" )
define pac = Character(u'PACT少尉', what_outlines=[(5, "#000000", 1, 1),(2, "#d04545", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#d04545", 0, 0)],ctc="ctc",ctc_position="fixed" )
define unof = Character(u'军官', what_outlines=[(5, "#000000", 1, 1),(2, "#d04545", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#d04545", 0, 0)],ctc="ctc",ctc_position="fixed" )
define cre = Character(" ", what_size=30,what_ypos=-700)
define wan = Character(u'游荡者', what_outlines=[(5, "#000000", 1, 1),(2, "#3b3d66", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#3b3d66", 0, 0)],ctc="ctc",ctc_position="fixed" )
define kuu = Character(u'库莎娜', what_outlines=[(5, "#000000", 1, 1),(2, "#d04545", 0, 0) ], who_outlines=[(5, "#000000", 1, 1),(3, "#d04545", 0, 0)],ctc="ctc",ctc_position="fixed" )


#########REPLAYS

label replay_havochit:
    
    scene black
    $ renpy.movie_cutscene("3DCG/havochit.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_havochitfly:
    
    scene black
    $ renpy.movie_cutscene("3DCG/havochitfly.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_havocattack:
    
    scene black
    $ renpy.movie_cutscene("3DCG/havocattack.webm",stop_music=True)
    
    $renpy.end_replay()    
    
label replay_blackjackhit:
    
    scene black
    $ renpy.movie_cutscene("3DCG/blackjackhit.webm",stop_music=True)
    
    $renpy.end_replay()    
    
label replay_blackjackfly:
    
    scene black
    $ renpy.movie_cutscene("3DCG/blackjackfly.webm",stop_music=True)
    
    $renpy.end_replay()    
    
label replay_blackjacklaser:
    
    scene black
    $ renpy.movie_cutscene("3DCG/blackjacklaser.webm",stop_music=True)
    
    $renpy.end_replay()    
    
label replay_havochitlaser:
    
    scene black
    $ renpy.movie_cutscene("3DCG/havochitlaser.webm",stop_music=True)
    
    $renpy.end_replay()    
    
label replay_blackjack_pulse:
    
    scene black
    $ renpy.movie_cutscene("3DCG/blackjack_pulse.webm",stop_music=True)
    
    $renpy.end_replay()    
    
label replay_titlecard:
    
    scene black
    $ renpy.movie_cutscene("3DCG/titlecard.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_sunrider_warp:
    
    scene black
    $ renpy.movie_cutscene("3DCG/sunrider warp.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_seraphim_snipe:
    
    scene black
    $ renpy.movie_cutscene("3DCG/seraphim_snipe.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_nightmareattack:
    
    scene black
    $ renpy.movie_cutscene("3DCG/nightmareattack.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_vanguardcut:
    
    scene black
    $ renpy.movie_cutscene("3DCG/vanguardcut.webm",stop_music=True)
    
    $renpy.end_replay()
        
label replay_blackjacknightmare:
    
    scene black
    $ renpy.movie_cutscene("3DCG/blackjacknightmare.webm",stop_music=True)
    
    $renpy.end_replay()
    
label replay_vanguard_eyepatch:
    
    play music "Music/The_Final_Battle_Cut.ogg"
    scene black
        
    $ renpy.movie_cutscene("3DCG/vanguard_eyepatch.webm",stop_music=False)
        
    stop music
    
    $renpy.end_replay()
    
label replay_vanguard_nopatch:
    
    play music "Music/The_Final_Battle_Cut.ogg"
    scene black    
    
    $ renpy.movie_cutscene("3DCG/vanguard_nopatch.webm",stop_music=False)
    
    stop music
    
    $renpy.end_replay()

label replay_op:
    
    scene black
    $ renpy.movie_cutscene("3DCG/op.webm",stop_music=True)
    
    $renpy.end_replay()

init python:

    Planet("CERA", "warpto_occupiedcera", 1297, 480, "warpto_occupiedcera")
    Planet("TYDARIA", "warpto_tydaria", 1390, 540, "warpto_tydaria")
    Planet("ASTRAL EXPANSE", "warpto_astralexpanse", 1250, 540, "warpto_astralexpanse")
    Planet("VERSTA", "warpto_versta", 1490, 725, "warpto_versta")
    Planet("NOMODORN", "warpto_nomodorn", 1630, 590, "warpto_nomodorn")
    Planet("RYUVIA PRIME", "warpto_ryuvia", 1410, 740, "warpto_ryuvia")
    Planet("FAR PORT", "warpto_farport", 1260, 776, "warpto_farport")
    Planet("ONGESS", "warpto_ongess", 1345, 655, "warpto_ongess")
    Planet("PACEMUS NEBULA", "warpto_pacemus", 1320, 570, "warpto_pacemus")
