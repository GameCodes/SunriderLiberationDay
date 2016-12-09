## this file defines all the different ships and weapons that you'll be using
## 1) player ships
## 2) PACT ships
## 3) pirate ships
## 4) weapons
## 5) Buffs
## 6) support skills (these usually apply the previously defined buffs)
## 7) store items
## 8) achievements

init 2 python: #Ships

###  PLAYER Ships ###

    class Sunrider(Battleship): # your ship!
        def __init__(self):
            super(Sunrider, self).__init__() # proper inheritance requires super()
            self.stype = 'Cruiser'
            self.name = 'Sunrider'
            self.animation_name = 'sunrider'
            self.faction = 'Player'
            self.max_hp = 1500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 3
            self.max_rockets = 2
            self.repair_drones = None
            self.pilot = "Ava"
            self.voice_channel = 'avavoice'
            
            #custom upgrades
            self.upgrades['base_armor'] = ['Armor',1,5,500,2]
            self.upgrades['max_missiles'] = ['Missile Storage',1,1,500,2]
            
            self.missiles = self.max_missiles
            self.rockets = 0
            self.evasion = -25  # cruisers are easy to hit
            self.lbl = Image('Battle UI/label_sunrider.png')  #this is the battle avatar
            if store.legion_destroyed:
                self.portrait = Image('Battle UI/ava_portrait_eyepatch.png')
            else:
                self.portrait = Image('Battle UI/ava_portrait.png')
            self.flak = 40
            self.flak_range = 2
            self.move_cost = 30
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 15
            self.armor = self.base_armor

            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_sunrider.png'
            self.icon = 'upgrade/select_sunrider.png'
            self.hovericon = hoverglow(self.icon)

          ##the sunrider gets personal death code!
        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))

            if BM.mission != 'skirmishbattle':
                set_cell_available(self.location) #tell the BM that the old cell is now free again
                destroyed_ships.append(self)
                player_ships.remove(self)
                BM.ships.remove(self)
                renpy.jump('sunrider_destroyed')
            else:
                BM.you_lose()

    class BlackJack(Battleship): # defining the Blackjack
        def __init__(self):
            super(BlackJack, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Black Jack'
            self.animation_name = 'blackjack'
            self.faction = 'Player'
            self.max_hp = 600
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.evasion = 25
            self.lbl = Image('Battle UI/label_blackjack.png')  #this is the battle avatar
            self.portrait = 'Battle UI/asaga_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/BlackJack/blackjack.png',
                'melee':'gameplay/Animations/BlackJack/blackjack_sword.png',
                'character':"Character/Asaga/asaga_plugsuit_point_happy.png"
                }
            self.flak = 35
            self.pilot = "Asaga"
            self.voice_channel = 'asavoice'
            
            ##custom upgrade scaling
            self.upgrades['melee_dmg'] = ['Melee Damage',1,0.05,100,1.4]
            self.upgrades['melee_acc'] = ['Melee Accuracy',1,0.05,100,1.4]
            self.upgrades['melee_cost'] = ['Melee Energy Cost',1,-0.05,100,1.8]

            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_blackjack.png'
            self.icon = 'upgrade/select_blackjack.png'
            self.hovericon = hoverglow(self.icon)

    class Liberty(Battleship):  #you can use any existing blueprint as a base, which makes things really easy.
        def __init__(self):
            super(Liberty, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Liberty'
            self.animation_name = 'liberty'
            self.support = True
            self.faction = 'Player'
            self.max_hp = 475
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.move_cost = 20
            self.evasion = 20
            self.lbl = Image('Battle UI/label_liberty.png')  #this is the battle avatar
            self.portrait = 'Battle UI/chigara_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Liberty/side.png'
                }
            self.flak = 0
            self.shield_generation = 35
            self.shields = self.shield_generation
            self.shield_range = 1
            self.pilot = "Chigara"
            self.voice_channel = 'chivoice'
            self.upgrades['base_armor'] = ['Armor',1,2,200,2.5]
            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_liberty.png'
            self.icon = 'upgrade/select_liberty.png'
            self.hovericon = hoverglow(self.icon)

    class Phoenix(Battleship):
        def __init__(self):
            super(Phoenix, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Phoenix'
            self.animation_name = 'phoenix'
            self.faction = 'Player'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 0
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 10
            self.hate = 100
            self.evasion = 50
            self.lbl = Image('Battle UI/label_phoenix.png')  #this is the battle avatar
            self.portrait = 'Battle UI/icari_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/side.png',
                'melee':'gameplay/Animations/Phoenix/melee.png',
                'character':"Character/Icari/icari_plugsuit_point_angry.png"
                }
            self.flak = 20
            self.pilot = "Icari"
            self.voice_channel = 'icavoice'
            self.upgrades['max_hp'] = ['Hull Plating',1,100,100,2.0]
            self.upgrades['max_en'] = ['Energy Reactor',1,5,150,1.3]
            self.upgrades['base_armor'] = ['Armor',1,1,500,1.2]

            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_phoenix.png'
            self.icon = 'upgrade/select_phoenix.png'
            self.hovericon = hoverglow(self.icon)


    class Bianca(Battleship):
        def __init__(self):
            super(Bianca, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Bianca'
            self.animation_name = 'bianca'
            self.faction = 'Player'
            self.support = True
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.move_cost = 30
            self.evasion = 20
            self.lbl = Image('Battle UI/label_bianca.png')  #this is the battle avatar
            self.portrait = 'Battle UI/claude_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Bianca/side.png'
                }
            self.flak = 0
            self.shield_generation = 30
            self.shields = self.shield_generation
            self.shield_range = 1
            self.pilot = "Claude"
            self.voice_channel = 'clavoice'
            self.upgrades['base_armor'] = ['Armor',1,2,200,2.5]

            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_bianca.png'
            self.icon = 'upgrade/select_bianca.png'
            self.hovericon = hoverglow(self.icon)


    class Seraphim(Battleship):
        def __init__(self):
            super(Seraphim, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Seraphim'
            self.animation_name = 'seraphim'
            self.faction = 'Player'
            self.max_hp = 375
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.hate = 100
            self.evasion = 20
            self.lbl = Image('Battle UI/label_seraphim.png')  #this is the battle avatar
            self.portrait = 'Battle UI/sola_portrait.png'
            self.upgrades['kinetic_dmg'] = ['Kinetic Damage',1,0.075,100,1.4]
            self.upgrades['kinetic_acc'] = ['Kinetic Accuracy',1,0.075,100,1.4]
            self.upgrades['kinetic_cost'] = ['Kinetic Energy Cost',1,-0.05,100,1.8]
            self.sprites = {
                'standard':'gameplay/Animations/Seraphim/side.png',
                }
            self.flak = 0
            self.pilot = "Sola"
            self.voice_channel = 'solvoice'

            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_seraphim.png'
            self.icon = 'upgrade/select_seraphim.png'
            self.hovericon = hoverglow(self.icon)


    class Paladin(Battleship):
        def __init__(self):
            super(Paladin, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Paladin'
            self.animation_name = 'paladin'
            self.faction = 'Player'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 2
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.hate = 100
            self.evasion = 10
            self.lbl = Image('Battle UI/label_paladin.png')  #this is the battle avatar
            self.portrait = 'Battle UI/kryska_portrait.png'
            self.sprites = {
                'standard':'gameplay/Animations/Paladin/side.png',
                'character':"Character/Kryska/kryska_plugsuit_handonhip_focussmile.png"
                }
            self.flak = 18
            self.pilot = "Kryska"
            self.voice_channel = 'kryvoice'

            ####################UPGRADE BACKGROUND AND ICONS
            self.upgrade_menu = 'Menu/upgrade_paladin.png'
            self.icon = 'upgrade/select_paladin.png'
            self.hovericon = hoverglow(self.icon)


    class AllianceCruiser(Battleship):
        def __init__(self):
            super(AllianceCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Alliance Cruiser'
            self.animation_name = 'alliancecruiser'
            self.pilot = 'Alliance Captain'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 12
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.hate = 100
            self.evasion = 0
            self.lbl = Image('Battle UI/label_alliancecruiser.png')  #this is the battle avatar
            self.default_weapon_list = [AllianceCruiserLaser(),AllianceCruiserMissile(),AllianceCruiserKinetic(),AllianceCruiserAssault()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 2
            self.voice_channel = "othvoice"

        def voice(self,event):
            if not BM.english_battle_voices:
                if event == 'Sel' or event == 'HitBuff':
                    renpy.music.queue('sound/beep1.ogg',channel='othvoice')
                else:
                    renpy.music.queue('sound/beep2.ogg',channel='othvoice')

            else:
                if event == 'Sel':
                    voice_list = ['AllianceCruiser/Alliance Cruiser Here.ogg','AllianceCruiser/Reporting For Duty.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'For' or event == 'Bac':
                    voice_list = ['AllianceCruiser/Yes Sir.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Dam':
                    voice_list = ["AllianceCruiser/Were Taking Fire.ogg","AllianceCruiser/Hull Breaches Reported.ogg","AllianceCruiser/Reroute Emergency Power.ogg"]
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Ret':
                    voice_list = ["AllianceCruiser/Abandon Ship.ogg"]
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'HitBuff':
                    voice_list = ["AllianceCruiser/All Hands Brace For Combat.ogg"]
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Laser' or event == 'Missile' or event == 'Kin':
                    voice_list = ["AllianceCruiser/Firing Weapons.ogg","AllianceCruiser/Open Fire.ogg","AllianceCruiser/Weapons Free.ogg"]
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                
            return
            
    class EnemyAllianceCruiser(Battleship):
        def __init__(self):
            super(EnemyAllianceCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Alliance Cruiser'
            self.animation_name = 'alliancecruiser'
            self.faction = 'Alliance'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 12
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.money_reward = 200
            self.hate = 100
            self.evasion = 0
            self.blbl = Image('Battle UI/label_enemyalliancecruiser.png')  #this is the battle avatar
            self.lbl = self.blbl 
            self.default_weapon_list = [AllianceCruiserLaser(),AllianceCruiserMissile(),AllianceCruiserKinetic(),AllianceCruiserAssault()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 2

    class EnemyAllianceInfantry(Battleship):
        def __init__(self):
            super(EnemyAllianceInfantry, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Alliance Infantry'
            self.faction = 'Alliance'
            self.max_hp = 600
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 0
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.money_reward = 50
            self.evasion = 13
            self.blbl = Image('Battle UI/label_enemyallianceinfantry.png')  #this is the battle avatar
            self.lbl = self.blbl 
            self.default_weapon_list = [AllianceInfantryMissile(),AllianceInfantryKinetic(),AllianceInfantryAssault()]
            self.portrait = None
            self.flak = 10
            self.flak_range = 1

    class AllianceInfantry(Battleship):
        def __init__(self):
            super(AllianceInfantry, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Alliance Infantry'
            self.animation_name = 'alliancecruiser'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 600
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 0
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 1
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.evasion = 13
            self.lbl = Image('Battle UI/label_allianceinfantry.png')  #this is the battle avatar
            self.default_weapon_list = [AllianceInfantryMissile(),AllianceInfantryKinetic(),AllianceInfantryAssault()]
            self.portrait = None
            self.flak = 10
            self.flak_range = 1

            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class EnemyAllianceSupportCruiser(Battleship):
        def __init__(self):
            super(EnemyAllianceSupportCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Alliance Support Cruiser'
            self.animation_name = 'alliancecruiser'
            self.faction = 'Alliance'
            self.max_hp = 1100
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.money_reward = 100
            self.hate = 500
            self.evasion = 0
            self.blbl = Image('Battle UI/label_alliancesupportcruiser.png')  #this is the battle avatar
            self.lbl = self.blbl 
            self.default_weapon_list = []
            self.portrait = None
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 40
            self.shields = self.shield_generation
            self.shield_range = 2
            
    class AllianceSupportCruiser(Battleship):
        def __init__(self):
            super(AllianceSupportCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Alliance Support Cruiser'
            self.animation_name = 'alliancecruiser'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 1100
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 30
            self.hate = 500
            self.evasion = 0
            self.lbl = Image('Battle UI/label_alliancesupportcruiser.png')  #this is the battle avatar
            self.default_weapon_list = []
            self.portrait = None
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 40
            self.shields = self.shield_generation
            self.shield_range = 2

            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class AllianceCarrier(Battleship):
        def __init__(self):
            super(AllianceCarrier, self).__init__()
            self.stype = 'Carrier'
            self.name = 'Alliance Carrier'
            self.animation_name = 'alliancebattleship'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 3300
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 18
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 50
            self.hate = 100
            self.evasion = -40
            self.lbl = Image('Battle UI/label_alliancecarrier.png') 
            self.default_weapon_list = [AllianceCarrierKinetic(),AllianceCarrierAssault(),AllianceCarrierRepair()]
            self.portrait = None
            self.flak = 40
            self.flak_range = 1
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class EnemyAllianceCarrier(Battleship):
        def __init__(self):
            super(EnemyAllianceCarrier, self).__init__()
            self.stype = 'Battleship'
            self.name = 'Alliance Carrier'
            self.animation_name = 'alliancebattleship'
            self.faction = 'Alliance'
            self.max_hp = 3300
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 18
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.money_reward = 500
            self.move_cost = 50
            self.hate = 100
            self.evasion = -40
            self.blbl = Image('Battle UI/label_enemyalliancecarrier.png')  #this is the battle avatar
            self.lbl = self.blbl 
            self.default_weapon_list = [AllianceCarrierKinetic(),AllianceCarrierAssault(),AllianceCarrierRepair()]
            self.portrait = None
            self.flak = 40
            self.flak_range = 1
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
                        
    class CeraGunboat(Battleship):
        def __init__(self):
            super(CeraGunboat, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Cera Gunboat'
            self.animation_name = 'alliancecruiser'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 3
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 50
            self.evasion = 43
            self.lbl = Image('Battle UI/label_ceragunboat.png')  #this is the battle avatar
            self.default_weapon_list = [CeraGunboatAssault(),SuppressiveFire()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 1
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']

    class RyuvianFalcon(Battleship):
        def __init__(self):
            super(RyuvianFalcon, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'Ryuvian Falcon'
            self.animation_name = 'ryuvianfalcon'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 120
            self.base_armor = 5
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 15
            self.hate = 100
            self.evasion = 30
            self.lbl = Image('Battle UI/label_ryuvianfalcon.png')  #this is the battle avatar
            self.default_weapon_list = [RyuvianFalconKinetic(),RyuvianFalconPulse()]
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']


    class UnionBattleship(Battleship):
        def __init__(self):
            super(UnionBattleship, self).__init__()
            self.stype = 'Battleship'
            self.name = 'Union Battleship'
            self.animation_name = 'unionbattleship'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 2900
            self.hp = self.max_hp
            self.max_en = 120
            self.base_armor = 40
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.hate = 100
            self.evasion = -32
            self.lbl = Image('Battle UI/label_unionbattleship.png')  #this is the battle avatar
            self.default_weapon_list = [UnionBattleshipLaser(),UnionBattleshipKinetic(),UnionBattleshipAssault(),BigGravityGun()]
            self.portrait = None
            self.flak = 36
            self.flak_range = 1
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']

    class AllianceBattleship(Battleship):
        def __init__(self):
            super(AllianceBattleship, self).__init__()
            self.stype = 'Battleship'
            self.name = 'Alliance Battleship'
            self.animation_name = 'alliancebattleship'
            self.pilot = 'Alliance Commander'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 2100
            self.hp = self.max_hp
            self.max_en = 120
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 2
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.hate = 100
            self.evasion = -25
            self.lbl = Image('Battle UI/label_alliancebattleship.png')  #this is the battle avatar
            self.default_weapon_list = [AllianceBattleshipLaser(),AllianceBattleshipMissile(),AllianceBattleshipKinetic(),AllianceBattleshipCannon(),AllianceBattleshipAssault()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 2
            self.voice_channel = "othvoice"
            
        def voice(self,event):
            if not BM.english_battle_voices:
                if event == 'Sel' or event == 'HitBuff':
                    renpy.music.queue('sound/beep1.ogg',channel='othvoice')
                else:
                    renpy.music.queue('sound/beep2.ogg',channel='othvoice')

            else:
                if event == 'Sel':
                    voice_list = ['AllianceBattleship/selection1.ogg','AllianceBattleship/selection2.ogg','AllianceBattleship/selection3.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'For' or event == 'Bac':
                    voice_list = ['AllianceBattleship/move1.ogg','AllianceBattleship/move2.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Dam':
                    voice_list = ['AllianceBattleship/damage1.ogg','AllianceBattleship/damage2.ogg','AllianceBattleship/damage3.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Ret':
                    voice_list = ['AllianceBattleship/die.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
            return
            
    class EnemyAllianceBattleship(Battleship):
        def __init__(self):
            super(EnemyAllianceBattleship, self).__init__()
            self.stype = 'Battleship'
            self.name = 'Alliance Battleship'
            self.animation_name = 'alliancebattleship'
            self.faction = 'Alliance'
            self.mercenary = True
            self.max_hp = 2100
            self.hp = self.max_hp
            self.max_en = 120
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 2
            self.missiles = self.max_missiles
            self.move_cost = 40
            self.money_reward = 400
            self.hate = 100
            self.evasion = -25
            self.blbl = Image('Battle UI/label_enemyalliancebattleship.png')  #this is the battle avatar
            self.lbl = self.blbl 
            self.default_weapon_list = [AllianceBattleshipLaser(),AllianceBattleshipMissile(),AllianceBattleshipKinetic(),AllianceBattleshipCannon(),AllianceBattleshipAssault()]
            self.portrait = None
            self.flak = 30
            self.flak_range = 2

    class FriendlyPactAssaultCarrier(Battleship):
        def __init__(self):
            super(FriendlyPactAssaultCarrier, self).__init__()
            self.stype = 'Assault Carrier'
            self.name = 'PACT Assault Carrier'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.faction = 'Player'
            self.mercenary = True
            self.animation_name = 'pactassaultcarrier'
            self.max_hp = 2800
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -30
            self.blbl = 'Battle UI/label_friendly_pactassaultcarrier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [FriendlyPACTAssaultCarrierAssault(),FriendlyPACTAssaultCarrierMissile(),FriendlyPACTAssaultCarrierKinetic(),FriendlyPACTAssaultCarrierLaser()]
            self.flak = 45
            self.flak_range = 2
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 40
            self.move_cost = 30
            self.armor = self.base_armor
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class FriendlyPactFastCruiser(Battleship):
        def __init__(self):
            super(FriendlyPactFastCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'PACT Fast Cruiser'
            self.faction = 'Player'
            self.mercenary = True
            self.animation_name = 'pactfastcruiser'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.money_reward = 375
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 8  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_friendly_pactfastcruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [FriendlyPACTFastCruiserKinetic(),FriendlyPACTFastCruiserAssault()]
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 7
            self.move_cost = 25
            self.armor = self.base_armor
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class FriendlyPactElite(Battleship):
        def __init__(self):
            super(FriendlyPactElite, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Elite'
            self.animation_name = 'pactelite'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 700
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 20
            self.base_armor = 3
            self.money_reward = 80
            self.max_missiles = 1
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 3
            self.default_weapon_list = [FriendlyPACTEliteLaser(),FriendlyPACTEliteMissile(),FriendlyPACTEliteMelee(),FriendlyPACTEliteAssault()]
            self.blbl = 'Battle UI/label_friendly_pactelite.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class FriendlyPactSupport(Battleship):
        def __init__(self):
            super(FriendlyPactSupport, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Support'
            self.support = True  #signifies to the AI this unit uses support skills
            self.animation_name = 'pactsupport'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 450
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 40
            self.move_cost = 20
            self.base_armor = 0
            self.money_reward = 80
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 0
            self.default_weapon_list = [PactRepair(), DisableLite(), PactRestore(), PactFlakOff(), PactShutOff()]
            self.blbl = 'Battle UI/label_friendly_pactsupport.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 1
            
            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']
            
    class TemporaryAllianceBattleship(AllianceBattleship):
        def __init__(self):
            AllianceBattleship.__init__(self)
            self.temporary = True
            BM.end_turn_callbacks.append(self.expiry_callback)
            
        def expiry_callback(self):
            if self.turns_alive > 3: #this counter starts at 1 and is increased just before callbacks are run. this ship lasts for 3 turns
                show_message("The Alliance Battleship goes back to base")
                BM.temp_battleship_active = False
                delete_ship(self)
                BM.end_turn_callbacks.remove(self.expiry_callback)
    
    class UnionFrigate(Battleship):
        def __init__(self):
            super(UnionFrigate, self).__init__()
            self.stype = 'Frigate'
            self.name = 'Mining Union Frigate'
            self.animation_name = 'unionfrigate'
            self.pilot = 'Union Luitenant'
            self.faction = 'Player'
            self.mercenary = True
            self.max_hp = 475
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 4
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 20
            self.hate = 100
            self.evasion = 5
            self.blbl = Image('Battle UI/label_unionfrigate.png')  #base(default) label
            self.lbl = self.blbl
            self.default_weapon_list = [UnionFrigateLaser(),ShdJam()]  #just this?
            self.portrait = None
            self.flak = 0
            self.flak_range = 0
            self.shield = 0
            self.shield_range = 0

        def voice(self,event):
            if not BM.english_battle_voices:
                if event == 'Sel' or event == 'HitBuff':
                    renpy.music.queue('sound/beep1.ogg',channel='othvoice')
                else:
                    renpy.music.queue('sound/beep2.ogg',channel='othvoice')

            else:
                if event == 'Sel':
                    voice_list = ['UnionFrigate/selection1.ogg','UnionFrigate/selection2.ogg','UnionFrigate/selection3.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'For' or event == 'Bac' or event == 'Las' or event == 'Cur':
                    voice_list = ['UnionFrigate/attack1.ogg','UnionFrigate/attack2.ogg','UnionFrigate/attack3.ogg']
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Dam':
                    voice_list = ["UnionFrigate/hit1.ogg","UnionFrigate/hit2.ogg","UnionFrigate/hit3.ogg"]
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                elif event == 'Ret':
                    voice_list = ["UnionFrigate/die1.ogg"]
                    renpy.music.queue('sound/Voice/' + renpy.random.choice(voice_list),channel='othvoice')
                
            return

    class Agamemnon(Battleship):
        def __init__(self):
            super(Agamemnon, self).__init__()
            self.stype = 'Ship'
            self.name = 'Agamemnon'
            self.animation_name = 'agamemnon'
            self.faction = 'Player'
            self.max_hp = 800
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 8
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 50
            self.hate = 300
            self.evasion = 0
            self.lbl = Image('Battle UI/label_agamemnon.png')  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']

        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            set_cell_available(self.location) #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            player_ships.remove(self)
            renpy.jump('sunrider_destroyed')

    class Freighter(Battleship):
        def __init__(self):
            super(Freighter, self).__init__()
            self.stype = 'Ship'
            self.name = 'Freighter'
            self.animation_name = 'mochi'
            self.faction = 'Player'
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 10
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 50
            self.hate = 50
            self.evasion = 0
            self.lbl = Image('Battle UI/label_mochi.png')  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "othvoice"
            self.selection_voice = ['sound/beep1.ogg']
            self.moveforward_voice = ['sound/beep2.ogg']
            self.movebackward_voice = ['sound/beep2.ogg']
            self.buffed_voice = ['sound/beep2.ogg']
            self.cursed_voice = ['sound/beep2.ogg']

        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            set_cell_available(self.location) #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            player_ships.remove(self)
            sunrider.hp = -1
            BM.you_lose()

    class PhoenixBoaster(Battleship):
        def __init__(self):
            super(PhoenixBoaster, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Unknown Hostile'
            self.animation_name = 'phoenixboaster'
            self.faction = 'PACT'
            self.max_hp = 700
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 15
            self.base_armor = 4
            self.money_reward = 300
            self.armor = 4
            self.default_weapon_list = [PhoenixBoasterLaser(),PhoenixBoasterAssault()]
            self.blbl = 'Battle UI/label_phoenixboaster.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/boaster_side.png',
                }
            self.flak = 20
            self.flak_range = 1

    class PactBomber(Battleship):
        def __init__(self):
            super(PactBomber, self).__init__()
            self.stype = 'Ryder' #subtype bomber
            self.name = 'PACT Bomber'
            self.animation_name = 'pactbomber'
            self.faction = 'PACT'
            self.max_hp = 550
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 2
            self.max_rockets = 1
            self.money_reward = 75
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 10  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 5
            self.move_cost = 30
            self.blbl = Image('Battle UI/label_pactbomber.png')  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.default_weapon_list = [PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket()]
            self.sprites = {
                'standard':'gameplay/Animations/PACTBomber/side.png',
                }
            self.flak = 0
            self.flak_range = 0

    class SeraphimEnemy(Battleship):
        def __init__(self):
            super(SeraphimEnemy, self).__init__()
            self.stype = 'Ryder' #subtype bomber
            self.name = 'Ryuvian Ryder'
            self.animation_name = 'seraphimenemy'
            self.faction = 'PACT'
            self.max_hp = 375
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 0
            self.money_reward = 150
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 4  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 20
            self.move_cost = 30
            self.default_weapon_list = [SeraphimEnemyKinetic()]


            self.blbl = Image('Battle UI/label_seraphimenemy.png')  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/SeraphimEnemy/side.png',
                }
            self.flak = 0
            self.flak_range = 0

    class Mochi(Battleship):
        def __init__(self):
            super(Mochi, self).__init__()
            self.stype = 'Ship'
            self.name = 'Mochi'
            self.animation_name = 'mochi'
            self.faction = 'Player'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.base_armor = 15
            self.armor = self.base_armor
            self.en = self.max_en
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.move_cost = 200
            self.hate = 50
            self.evasion = -20
            self.lbl = Image('Battle UI/label_mochi.png')  #this is the battle avatar
            self.portrait = None
            self.flak = 0
            self.flak_range = 0

            self.voice_channel = "avavoice"
            self.selection_voice = ['Agamemnon/beep1.ogg']
            self.moveforward_voice = ['Agamemnon/beep2.ogg']
            self.movebackward_voice = ['Agamemnon/beep2.ogg']
            self.buffed_voice = ['Agamemnon/beep2.ogg']
            self.cursed_voice = ['Agamemnon/beep2.ogg']

        def destroy(self,attacker,no_animation = False):
            BM.stopAI = True
            if not no_animation:
                try:
                    renpy.call_in_new_context('die_{}'.format(self.animation_name)) #show the death animation
                except:
                    show_message('missing animation. "die_{}" does\'t seem to exist'.format(self.animation_name))
            set_cell_available(self.location) #tell the BM that the old cell is now free again
            BM.ships.remove(self)
            player_ships.remove(self)
            sunrider.hp = -1
            BM.you_lose()

### PACT ships ###

    class MissileFrigate(Battleship):
        def __init__(self):
            super(MissileFrigate, self).__init__()
            self.stype = 'Frigate'
            self.name = 'PACT Missile Frigate'
            self.animation_name = 'pactmissilefrigate'
            self.faction = 'PACT'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.move_cost = 30
            self.money_reward = 100
            self.max_missiles = 6   #a lot of missiles, but it's all it has. things go wrong when it's out anywway
            self.missiles = self.max_missiles
            self.default_weapon_list = [PactFrigateMissile()]
            self.evasion = 0 # frigates get no penalty and no bonus to evasion
            self.blbl = 'Battle UI/label_missilefrigate.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.flak = 0
            self.flak_range = 0

    class PactMook(Battleship):
        def __init__(self):
            super(PactMook, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Mook'
            self.animation_name = 'pactmook'
            self.faction = 'PACT'
            self.max_hp = 400
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 20
            self.base_armor = 0
            self.money_reward = 50
            self.max_missiles = 0
            self.missiles = self.max_missiles
            self.armor = 0
            self.default_weapon_list = [PACTMookLaser(),PACTMookMissile(),PACTMookAssault()]
            self.blbl = 'Battle UI/label_pactmook.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTMook/side.png'
                }
            self.flak = 10
            self.flak_range = 1

    class PhoenixEnemy(Battleship):
        def __init__(self):
            super(PhoenixEnemy, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Phoenix'
            self.animation_name = 'phoenixenemy'
            self.faction = 'PACT'
            self.max_hp = 300
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 50
            self.move_cost = 10
            self.base_armor = 0
            self.money_reward = 200
            self.armor = 0
            self.default_weapon_list = [PhoenixEnemyMelee(),PhoenixAssault()]
            self.blbl = 'Battle UI/label_phoenixenemy.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Phoenix/side_mirror.png',
                'melee':'gameplay/Animations/Phoenix/melee_mirror.png',
                'character':"Character/Icari/icari_plugsuit_point_crazylaugh.png"
                }
            self.flak = 20
            self.flak_range = 1

            self.voice_channel = "icavoice"
            self.attack_voice = ["sound/Voice/Icari/Icari Attacking Melee 1.ogg","sound/Voice/Icari/Icari Attacking Melee 2.ogg","sound/Voice/Icari/Icari Attacking Melee 3.ogg","sound/Voice/Icari/Icari Attacking Melee 1.ogg"]

    class Nightmare(Battleship):
        def __init__(self):
            super(Nightmare, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Nightmare'
            self.animation_name = 'nightmare'
            self.faction = 'PACT' #for now...
            self.max_hp = 3200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 50
            self.move_cost = 10
            self.base_armor = 20
            self.armor = self.base_armor
            self.money_reward = 800
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            
            self.default_weapon_list = [NightmareLaser(),NightmarePulse(),NightmareMissile(),NightmareMelee()]
            self.blbl = 'Battle UI/label_nightmare.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Nightmare/side.png',
                'melee':'gameplay/Animations/Nightmare/melee.png',
                }
            self.flak = 100
            self.flak_range = 2
            self.shield_generation = 100
            self.shields = self.shield_generation
            self.shield_range = 2

    class Arcadius(Battleship):
        def __init__(self):
            super(Arcadius, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Arcadius'
            self.animation_name = 'nightmare'
            self.faction = 'PACT' #for now...
            self.max_hp = 1000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 37
            self.move_cost = 20
            self.base_armor = 4
            self.money_reward = 300
            self.max_missiles = 1
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 4
            self.default_weapon_list = [ArcadiusLaser(),ArcadiusPulse(),ArcadiusMissile(),ArcadiusMelee()]
            self.blbl = 'Battle UI/label_nightmare.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Nightmare/side.png',
                'melee':'gameplay/Animations/Nightmare/melee.png',
                }
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0

    class PactElite(Battleship):
        def __init__(self):
            super(PactElite, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Elite'
            self.animation_name = 'pactelite'
            self.faction = 'PACT'
            self.max_hp = 700
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 30
            self.move_cost = 20
            self.base_armor = 3
            self.money_reward = 80
            self.max_missiles = 1
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 3
            self.default_weapon_list = [PACTEliteLaser(),PACTEliteMissile(),PACTEliteMelee(),PACTEliteAssault()]
            self.blbl = 'Battle UI/label_pactelite.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTElite/side.png',
                'melee':'gameplay/Animations/PACTElite/melee.png',
                }
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0

    class PactSupport(Battleship):
        def __init__(self):
            super(PactSupport, self).__init__()
            self.stype = 'Ryder'
            self.name = 'PACT Support'
            self.support = True  #signifies to the AI this unit uses support skills
            self.animation_name = 'pactsupport'
            self.faction = 'PACT'
            self.max_hp = 450
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.evasion = 40
            self.move_cost = 20
            self.base_armor = 0
            self.money_reward = 80
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.armor = 0
            self.default_weapon_list = [PactRepair(), DisableLite(), PactRestore(), PactFlakOff(), PactShutOff()]
            self.blbl = 'Battle UI/pactsupport_label.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PACTSupport/side.png',
                }
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 1

    class PactCruiser(Battleship):
        def __init__(self):
            super(PactCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'PACT Cruiser'
            self.faction = 'PACT'
            self.animation_name = 'pactcruiser'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 300
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -25  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactcruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTCruiserLaser(),PACTCruiserKinetic(),PACTCruiserAssault()]
            self.flak = 30
            self.flak_range = 2
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 1
            self.base_armor = 30
            self.move_cost = 30
            self.armor = self.base_armor

    class PactFastCruiser(Battleship):
        def __init__(self):
            super(PactFastCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'PACT Fast Cruiser'
            self.faction = 'PACT'
            self.animation_name = 'pactfastcruiser'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.money_reward = 375
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 8  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactfastcruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTFastCruiserKinetic(),PACTFastCruiserAssault()]
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 7
            self.move_cost = 25
            self.armor = self.base_armor

    class RyuvianCruiser(Battleship):
        def __init__(self):
            super(RyuvianCruiser, self).__init__()
            self.stype = 'Cruiser'
            self.name = 'Ryuvian Cruiser'
            self.faction = 'PACT'
            self.animation_name = 'ryuviancruiser'
            self.max_hp = 1200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 370
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -20  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_ryuviancruiser.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [RyuvianCruiserKinetic(),RyuvianCruiserMissile()]
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 30
            self.move_cost = 20
            self.armor = self.base_armor

    class RyuvianFalconEnemy(Battleship):
        def __init__(self):
            super(RyuvianFalconEnemy, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'Ryuvian Falcon'
            self.faction = 'PACT'
            self.animation_name = 'ryuvianfalconenemy'
            self.max_hp = 9001
            self.hp = self.max_hp
            self.max_en = 150
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 40  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_ryuvianfalcon_enemy.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [RyuvianFalconEnemyKinetic(),RyuvianFalconEnemyPulse(),RyuvianFalconEnemyRepair(),RyuvianFalconEnemyRestore()]
            self.flak = 100
            self.flak_range = 2
            self.shield_generation = 100
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 100
            self.move_cost = 20
            self.armor = self.base_armor

    class PactOutpost(Battleship):
        def __init__(self):
            super(PactOutpost, self).__init__()
            self.stype = 'Station'
            self.name = 'PACT Outpost'
            self.faction = 'PACT'
            self.animation_name = 'pactstation'
            self.max_hp = 900
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 0
            self.money_reward = 1000
            self.boss = True
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -40  # cruisers are easy to hit
            self.blbl = 'Battle UI/pactstation.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTOutpostLaser(),PACTOutpostKinetic()]
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 20
            self.armor = self.base_armor
            self.move_cost = 1000

    class PactBattleship(Battleship):
        def __init__(self):
            super(PactBattleship, self).__init__()
            self.stype = 'Battleship'
            self.name = 'PACT Battleship'
            self.faction = 'PACT'
            self.animation_name = 'pactbattleship'
            self.max_hp = 2100
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 2
            self.max_rockets = 1
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -40  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactbattleship.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTBattleshipLaser(),PACTBattleshipKinetic(),PACTBattleshipAssault(),PACTBattleshipMissile(),PACTBattleshipRocket()]
            self.flak = 40
            self.flak_range = 2
            self.shield_generation = 40
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 40
            self.move_cost = 50
            self.armor = self.base_armor

    class PactDestroyer(Battleship):
        def __init__(self):
            super(PactDestroyer, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'PACT Destroyer'
            self.faction = 'PACT'
            self.animation_name = 'pactdestroyer'
            self.max_hp = 550
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 275
            self.max_missiles = 0
            self.max_rockets = 8
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 5  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pactdestroyer.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [SuperRocket()]
            self.flak = 0
            self.flak_range = 0
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 8
            self.move_cost = 30
            self.armor = self.base_armor

    class PactCarrier(Battleship):
        def __init__(self):
            super(PactCarrier, self).__init__()
            self.stype = 'Carrier'
            self.name = 'PACT Carrier'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.spawns = [
                ( PactMook,50,[ PACTMookLaser(),PACTMookMissile(),PACTMookAssault() ] ),
                ( PactBomber,100,[ PACTBomberLaser(),PACTBomberMissile(),PACTBomberRocket() ] )
                ]
            self.faction = 'PACT'
            self.animation_name = 'pactcarrier'
            self.max_hp = 2000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -50
            self.blbl = 'Battle UI/label_pactcarrier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTCarrierAssault()]
            self.flak = 60
            self.flak_range = 2
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 40
            self.move_cost = 50
            self.armor = self.base_armor

    class PactProtoCarrier(Battleship):
        def __init__(self):
            super(PactProtoCarrier, self).__init__()
            self.stype = 'Carrier'
            self.name = 'PACT Carrier'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.spawns = [
                ( Arcadius,100,[ ArcadiusMelee(),ArcadiusMissile(),ArcadiusLaser(),ArcadiusPulse() ] ),
                ]
            self.faction = 'PACT'
            self.animation_name = 'pactcarrier'
            self.max_hp = 2000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 0
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -50
            self.blbl = 'Battle UI/label_pactcarrier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTCarrierAssault()]
            self.flak = 60
            self.flak_range = 2
            self.shield_generation = 50
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 40
            self.move_cost = 50
            self.armor = self.base_armor


    class PactAssaultCarrier(Battleship):
        def __init__(self):
            super(PactAssaultCarrier, self).__init__()
            self.stype = 'Assault Carrier'
            self.name = 'PACT Assault Carrier'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.spawns = [
                ( PactElite,60,[ PACTEliteLaser(),PACTEliteMissile(),PACTEliteAssault(),PACTEliteMelee() ] ),
                ( PactSupport,60,[ PactRepair(), DisableLite(), PactRestore(), PactFlakOff(), PactShutOff() ] )
                ]
            self.faction = 'PACT'
            self.animation_name = 'pactassaultcarrier'
            self.max_hp = 2800
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.money_reward = 500
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -30
            self.blbl = 'Battle UI/label_pactassaultcarrier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PACTAssaultCarrierAssault(),PACTAssaultCarrierMissile(),PACTAssaultCarrierKinetic(),PACTAssaultCarrierLaser()]
            self.flak = 45
            self.flak_range = 2
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 40
            self.move_cost = 30
            self.armor = self.base_armor

    class EnemyBlackjack(Battleship):
        def __init__(self):
            super(EnemyBlackjack, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Enemy Black Jack'
            #indicate what units this carrier can spawn. syntax: [ship,cost,weaponlist]
            self.faction = 'PACT'
            self.animation_name = 'enemyblackjack'
            self.max_hp = 1600
            self.hp = self.max_hp
            self.max_en = 120
            self.en = self.max_en
            self.money_reward = 300
            self.max_missiles = 2
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 40
            self.blbl = 'Battle UI/label_enemyblackjack.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [EnemyBlackjackAssault(),EnemyBlackjackKinetic(),EnemyBlackjackLaser(),EnemyBlackjackMelee(),EnemyBlackjackPulse()]
            self.flak = 40
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 20
            self.move_cost = 15
            self.armor = self.base_armor

    class Legion(Battleship):
        def __init__(self):
            super(Legion, self).__init__()
            self.stype = 'Super Dreadnought'
            self.name = 'Legion'
            self.faction = 'PACT'
            self.animation_name = 'legion'
            self.max_hp = 26000
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.money_reward = 2000
            self.max_missiles = 5
            self.max_rockets = 0
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -70  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_legion.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [LegionLaser(),LegionKinetic(),LegionMissile()]
            self.flak = 100
            self.flak_range = 2
            self.shield_generation = 100
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 80
            self.move_cost = 50
            self.armor = self.base_armor


### pirate ships ###

    class PirateBomber(Battleship):
        def __init__(self):
            super(PirateBomber, self).__init__()
            self.stype = 'Ryder' #subtype bomber
            self.name = 'Pirate Bomber'
            self.animation_name = 'piratebomber'
            self.faction = 'Pirate'
            self.max_hp = 350
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 1
            self.max_rockets = 1
            self.money_reward = 80
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 8  #Ryders are not typically armored
            self.armor = self.base_armor
            self.evasion = 10
            self.move_cost = 30
            self.blbl = 'Battle UI/label_piratebomber.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/PirateBomber/bomber_side.png'
                }
            self.flak = 20
            self.flak_range = 1
            self.default_weapon_list = [PirateBomberMissile(),PirateBomberRocket(),PirateBomberAssault()]

    class Havoc(PirateBomber):
        def __init__(self):
            super(Havoc, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Havoc'
            self.animation_name = 'havoc'
            self.faction = 'Pirate'
            self.max_hp = 1500
            self.hp = self.max_hp
            self.max_en = 130
            self.en = self.max_en
            self.boss = False
            self.max_missiles = 3
            self.max_rockets = 2
            self.money_reward = 500
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.base_armor = 17
            self.armor = 17
            self.evasion = 8
            self.move_cost = 30
            self.blbl = 'Battle UI/havoc.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.sprites = {
                'standard':'gameplay/Animations/Havoc/havoc.png',
                'melee':'gameplay/Animations/Havoc/havoc_melee.png',
                'character':"Character/Cosette/cosette_plugsuit_front_evilsmile.png"
                }
            self.flak = 40
            self.flak_range = 2
            self.default_weapon_list = [HavocMelee(),HavocAssault(),HavocMissile(),HavocRocket()]

            ##voices##
            self.voice_channel = "cosvoice"
            self.attack_voice = ["sound/Voice/Cosette/Cosette Melee Attack 1.ogg","sound/Voice/Cosette/Cosette Melee Attack 2.ogg","sound/Voice/Cosette/Cosette Melee Attack 3.ogg","sound/Voice/Cosette/Cosette Melee Attack 4.ogg"]
            
    class HavocPlayer(Havoc):
        def __init__(self):
            super(HavocPlayer, self).__init__()
            self.faction = 'Player'
            self.pilot = "Cosette"
            self.blbl = 'Battle UI/label_playerhavoc.png'
            self.portrait = 'Battle UI/cosette_portrait.png'            
            self.lbl = self.blbl
            self.default_weapon_list = [HavocMelee(),HavocAssault(),HavocMissile(),SunriderMIRV()]
            self.voice_channel = 'cosvoice'
            self.move_cost = 40


    class PirateGrunt(Battleship):
        def __init__(self):
            super(PirateGrunt, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Pirate Grunt'
            self.animation_name = 'pirategrunt'
            self.faction = 'Pirate'
            self.max_hp = 275
            self.hp = self.max_hp
            self.max_missiles = 1
            self.max_rockets = 0
            self.base_armor = 0
            self.armor = 0
            self.money_reward = 50
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 12
            self.move_cost = 20
            self.blbl = 'Battle UI/label_pirategrunt.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.default_weapon_list = [PirateGruntLaser(),PirateGruntMissile(),PirateGruntAssault()]
            self.sprites = {
                'standard':'gameplay/Animations/PirateGrunt/side.png'
                }
            self.flak = 15
            self.flak_range = 1

    class PirateDestroyer(Battleship):
        def __init__(self):
            super(PirateDestroyer, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'Pirate Destroyer'
            self.animation_name = 'piratedestroyer'
            self.faction = 'Pirate'
            self.max_hp = 500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.move_cost = 30
            self.evasion = -10
            self.money_reward = 100
            self.blbl = 'Battle UI/label_piratedestroyer.png'  #this is the battle avatar
            self.lbl = self.blbl #this is what is displayed and can be changed to suit the moment
            self.default_weapon_list = [PirateDestroyerLaser(),PirateDestroyerKinetic()]
            self.flak = 0
            self.flak_range = 0

    class PirateBase(Battleship):
        def __init__(self):
            super(PirateBase, self).__init__()
            self.stype = 'Station'
            self.name = 'Pirate Base'
            self.faction = 'Pirate'
            self.animation_name = 'piratebase'
            self.max_hp = 2200
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 5
            self.max_rockets = 0
            self.boss = False
            self.money_reward = 500
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -50  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_piratebase.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PirateBaseKinetic(),PirateBaseAssault(),PirateBaseMissile()]
            self.flak = 30
            self.flak_range = 1
            self.shield_generation = 25
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 50
            self.armor = self.base_armor
            self.move_cost = 1000

    class PirateIronhog(Battleship):
        def __init__(self):
            super(PirateIronhog, self).__init__()
            self.stype = 'Destroyer'
            self.name = 'Pirate Ironhog'
            self.faction = 'Pirate'
            self.animation_name = 'pirateironhog'
            self.max_hp = 480
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 3
            self.boss = False
            self.money_reward = 175
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = -10  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_pirateironhog.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [PirateIronhogAssault(),PirateIronhogRocket()]
            self.flak = 60
            self.flak_range = 1
            self.shield_generation = 0
            self.shields = self.shield_generation
            self.shield_range = 0
            self.base_armor = 7
            self.armor = self.base_armor
            self.move_cost = 20

    class Nightmare_Flierdrone(Battleship):
        def __init__(self):
            super(Nightmare_Flierdrone, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Flier Drone'
            self.faction = 'PACT'
            self.max_hp = 500
            self.hp = self.max_hp
            self.max_en = 100
            self.en = self.max_en
            self.max_missiles = 0
            self.max_rockets = 0
            self.boss = False
            self.money_reward = 50
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 68  # cruisers are easy to hit
            self.blbl = 'Battle UI/label_nightmareflier.png'  #this is the battle avatar
            self.lbl = self.blbl
            self.default_weapon_list = [NightmareFlierdroneLaser()]
            self.flak = 40
            self.flak_range = 1
            self.shield_generation = 30
            self.shields = self.shield_generation
            self.shield_range = 1
            self.base_armor = 0
            self.armor = self.base_armor
            self.move_cost = 10

    class Nightmare_Ascendant(Battleship):
        def __init__(self):
            super(Nightmare_Ascendant, self).__init__()
            self.stype = 'Ryder'
            self.name = 'Nightmare Ascendant'
            self.faction = 'PACT'
            self.animation_name = 'theboss'
            self.move_cost = 5
            self.boss = True
            self.max_hp = 30000
            self.hp = self.max_hp
            self.max_en = 140
            self.en = self.max_en
            self.max_missiles = 9
            self.max_rockets = 9
            self.money_reward = 5000 #does it matter?
            self.missiles = self.max_missiles
            self.rockets = self.max_rockets
            self.evasion = 40
            self.blbl = 'Battle UI/label_nightmareascendant.png'  #temp image
            self.lbl = self.blbl
            self.weapons = self.default_weapon_list
            self.flak = 80
            self.flak_range = 2
            self.shield_generation = 80
            self.shields = self.shield_generation
            self.shield_range = 2
            self.base_armor = 15
            self.armor = self.base_armor
            # self.move_cost = 25
            self.brain = DefaultAI(self)
            self.default_weapon_list = [NightmareAscendant_Laser()]
        
        def __getattribute__(self,name):
            v = store.object.__getattribute__(self, name)
            if not is_number(v): return v #speedup the code
            
            # try to not crash the game
            if not hasattr(self,'buffs'):
                return v
                
            buffs = store.object.__getattribute__(self, 'buffs')
            
            for buff in buffs:
                for affected_stat in buff.affected_stats:
                    if name == affected_stat:
                        #curses only have half effect on this unit.
                        if buff.curse:                            
                            v = int( ( buff.get_modified_stat(name,v) + v ) / 2.0 )
                        else:
                            v = buff.get_modified_stat(name,v)
                        continue
            return v   
            
        def set_buff(self,buff):
            if buff is None: 
                debuglog_add("error: {} was told to set a None buff".format(self.name))
                return False
                
            #this unit is immune to disable
            if buff.name == "Disabled":
                show_message("The boss is immune!")
                return False
                
            buff = buff(self)
            if buff.curse:
                show_message("The curse is only half as effective as normal")
            
            if self.has_buff(buff.name):
                if buff.cumulative:
                    for i in self.buffs:
                        if i.name == buff.name:
                            i.stack_counter += 1
                            self.update_stats()
                            
                            if i.function_at_stacksize is not None:
                                stacksize,function = i.function_at_stacksize
                                if stacksize <= i.stack_counter:
                                    BM.stopAI = True
                            return True
                else:
                    for i in self.buffs:
                        if i.name == buff.name and i.turns_left < buff.duration:
                            i.turns_left = buff.duration
                            self.update_stats()
                            return True
                #didn't increase the stack and didn not refresh duration -> failure
                return False 
            else:
                self.buffs.append(buff)
                self.update_stats()
                return True    
        
        # def destroy(self,attacker,no_animation = False):
            # self.brain.destroyed()
            
init 2 python: ### Weapons ###

##############SUNRIDER WEAPONS
    class SunriderLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            self.name = 'Trinities'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""

    class SunriderMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 80
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Sunrider_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""

    class SunriderKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 70
            self.wtype = 'Kinetic'
            self.name = 'Sunrider\'s main guns'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            一发远距离和面对小目标敌人时不甚精确的重击。
            面对动能武器时护甲效果加倍。"""

    class SunriderPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 25
            self.energy_use = 40
            self.shot_count = 9
            self.accuracy = 90
            self.wtype = 'Pulse'
            self.name = 'Sunrider_Pulse'
            self.attack_voice = ["sound/Voice/Ava/Ava Attacking Lasers 3.ogg",
                                "sound/Voice/Ava/Ava Attacking Lasers 4.ogg"]
            self.lbl = Image('Battle UI/button_pulse.png')
            self.tooltip = u"""
            发射大量激光脉冲。即使敌人闪避了其中几发，
            其它依旧可能命中。它们总伤害比激光束更强，
            但是不能穿透护甲，也会被护盾抵消。"""

    class SunriderAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'Sunrider\'s Flak'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

    class SunriderRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 800
            self.energy_use = 30
            self.shot_count = 1
            self.accuracy = 100
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.name = 'Thermonuclear warhead'
            self.lbl = Image('Battle UI/button_rocket.png')
            self.tooltip = u"""
            发射装有毁灭性弹头的大型火箭。
            弹药极度有限，会被敌人防空火力击落。"""
            
    class SunriderMIRV(SuperRocket):
        def __init__(self):
            SuperRocket.__init__(self)
            self.damage = 1200
            self.energy_use = 30
            self.splash_reduction = 0.5
            self.tooltip = u"""
            发射装有毁灭性弹头的大型MIRV火箭，对周围造成
            一半溅射伤害，必定命中，但是会被防空火力击落。"""

########################RYUVIAN FALCON

    class RyuvianFalconKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 410
            self.energy_use = 50
            self.shot_count = 1
            self.accuracy = 73
            self.wtype = 'Kinetic'
            self.name = 'Falcon Punch'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            尽管威力不如标准型，在隼鹰级的轻型舰体上
            装备如此强大的火炮依旧是工程学上的壮举。
            面对动能武器时护甲效果加倍。"""

    class RyuvianFalconPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 30
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 90
            self.wtype = 'Pulse'
            self.name = 'Sunrider_Pulse'
            self.lbl = Image('Battle UI/button_pulse.png')
            self.tooltip = u"""
            发射大量激光脉冲。即使敌人闪避了其中几发，
            其它依旧可能命中。它们总伤害比激光束更强，
            但是不能穿透护甲，也会被护盾抵消。"""


##############ALLIANCE CRUISER WEAPONS
    class AllianceCruiserLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 250
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 125
            self.wtype = 'Laser'
            self.name = 'AllianceCruiser_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""

    class AllianceCruiserMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 70
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 100
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'AllianceCruiser_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""

    class AllianceCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 425
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 75
            self.wtype = 'Kinetic'
            self.name = 'AllianceCruiser_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            一发远距离和面对小目标敌人时不甚精确的重击。
            面对动能武器时护甲效果加倍。"""

    class AllianceCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'AllianceCruiser_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

##############ALLIANCE INFANTRY WEAPONS

    class AllianceInfantryMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 8
            self.accuracy = 100
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'AllianceInfantry_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""

    class AllianceInfantryKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 87
            self.wtype = 'Kinetic'
            self.name = 'AllianceInfantry_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            由于联盟的战斗小队在面对PACT的重装甲时束手无策，
            一部分部队装备上了大型反物质步枪。报告显示这以
            速度和反太空骑士能力的牺牲换来了更高的穿甲能力。"""

    class AllianceInfantryAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 40
            self.shot_count = 18
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'AllianceCruiser_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

            
#################################CERA GUNBOAT WEAPONS

    class CeraGunboatAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 30
            self.shot_count = 18
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'CeraGunboat_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

#############################UNION BATTLESHIP WEAPONS

    class UnionBattleshipLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 340
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 97
            self.wtype = 'Laser'
            self.name = 'AllianceBattleship_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            矿业联合的小行星采掘船前端装备了用于切割矿石的 
            强力激光。联合坚决否认这种装备在军事上应用的 
            可能性。会被敌人的护盾抵消。"""

    class UnionBattleshipKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 65
            self.wtype = 'Kinetic'
            self.name = 'UnionBattleship_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            对海盗和觊觎中立星缘者的有效吓阻力量。 
            出于外交关系的考虑和法律规定威力较小。
            面对动能武器时护甲效果加倍。"""

    class UnionBattleshipAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 60
            self.wtype = 'Assault'
            self.name = 'UnionBattleship_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            暴雨般的防空弹幕洒向使用小型作战单位和导弹的
            海盗们。护甲在面对弹幕武器时效果加倍。也提供
            防空火力。但是连续拦截后效果会减弱。"""

##############ALLIANCE BATTLESHIP WEAPONS
    class AllianceBattleshipLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 300
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 115
            self.wtype = 'Laser'
            self.name = 'AllianceBattleship_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""

    class AllianceBattleshipMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 80
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 100
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'AllianceBattleship_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""

    class AllianceBattleshipKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 550
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 75
            self.wtype = 'Kinetic'
            self.name = 'AllianceBattleship_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            一发远距离和面对小目标敌人时不甚精确的重击。
            面对动能武器时护甲效果加倍。"""

    class AllianceBattleshipCannon(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 1500
            self.energy_use = 120
            self.shot_count = 1
            self.accuracy = 70
            self.wtype = 'Kinetic'
            self.name = 'AllianceBattleship_Cannon'
            self.lbl = Image('Battle UI/button_cannon.png')
            self.animation_name = 'kinetic2'
            self.tooltip = u"""
            毁灭性的终极火力，可以穿透最坚固的护甲，
            但是需要大量能量，对小目标敌人效果很差。"""

    class AllianceBattleshipAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'AllianceBattleship_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

##############ALLIANCE CARRIER WEAPONS

    class AllianceCarrierKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 4
            self.accuracy = 75
            self.wtype = 'Kinetic'
            self.name = 'AllianceCarrier_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            巨大的联盟航母进行过改造以装备足以同时与整个
            舰队作战的主炮。不建议战舰接近这个怪物。"""

    class AllianceCarrierAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'AllianceCarrier_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""
            
    class AllianceCarrierRepair(Support):
        def __init__(self):
            Support.__init__(self)
            self.repair = True
            self.damage = 400 #also used for heals
            self.energy_use = 40
            self.name = 'AllianceCarrierRepair'
            self.shot_count = 1
            self.lbl = Image('Battle UI/button_repair.png')
            self.max_range = 1
            self.target_type_restriction = ['Ryder']
            self.tooltip = u"""
            为邻近的太空骑士回复约400点生命值。"""
            
###################BLACK JACK WEAPONS

    class BlackjackLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'Blackjack_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""


    class BlackjackMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 20
            self.shot_count = 10
            self.accuracy = 70
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Blackjack_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""

    class BlackjackPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 30
            self.energy_use = 50
            self.shot_count = 7
            self.accuracy = 80
            self.wtype = 'Pulse'
            self.name = 'Blackjack_Pulse'
            self.lbl = Image('Battle UI/button_pulse.png')
            self.tooltip = u"""
            发射大量激光脉冲。即使敌人闪避了其中几发，
            其它依旧可能命中。它们总伤害比激光束更强，
            但是不能穿透护甲，也会被护盾抵消。"""

    class BlackjackAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.name = 'Blackjack_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

    class BlackjackMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 400    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 70
            self.acc_degradation = 0
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = Image('Battle UI/button_melee.png')
            self.tooltip = u"""
            切开敌人的太空骑士，造成毁灭性伤害。只能用于
            近身范围的敌人。移动到敌人身边会触发先制反击。"""
            
    class BlackjackKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 100
            self.name = "Blackjack Kinetic"
            self.energy_use = 70
            self.shot_count = 4
            self.accuracy = 65
            self.wtype = 'Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            这些穿甲弹对重甲目标相当有效。"""            


#############################################LIBERTY WEAPONS

    class LibertyLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 100
            self.energy_use = 50
            self.shot_count = 1
            self.accuracy = 110
            self.wtype = 'Laser'
            self.name = 'Liberty_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""


###################PALADIN WEAPONS

    class PaladinMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 80
            self.energy_use = 20
            self.shot_count = 5
            self.accuracy = 70
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Paladin_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""

    class PaladinAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 14
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Assault'
            self.name = 'Paladin_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""


    class PaladinKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 70
            self.wtype = 'Kinetic'
            self.name = 'Paladin_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            一发远距离和面对小目标敌人时不甚精确的重击。
            面对动能武器时护甲效果加倍。"""

################################################FRIENDLY ASSAULT CARRIER

    class FriendlyPACTAssaultCarrierLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 320
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 100
            self.wtype = 'Laser'
            self.name = 'Friendly_PACTAssaultCarrier_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""

    class FriendlyPACTAssaultCarrierKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 2
            self.accuracy = 65
            self.wtype = 'Kinetic'
            self.name = 'Friendly_PACTAssaultCarrier_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            一发远距离和面对小目标敌人时不甚精确的重击。
            面对动能武器时护甲效果加倍。"""

    class FriendlyPACTAssaultCarrierAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 55
            self.wtype = 'Assault'
            self.name = 'Friendly_PACTAssaultCarrier_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

    class FriendlyPACTAssaultCarrierMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 80
            self.uses_rockets = False
            self.uses_missiles = True
            self.wtype = 'Missile'
            self.name = 'Friendly_PACTAssaultCarrier_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""
            
#############################################################FRIENDLY FAST CRUISER

    class FriendlyPACTFastCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 75
            self.wtype = 'Kinetic'
            self.name = 'Friendly_PACTFastCruiser_Kinetic'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            一发远距离和面对小目标敌人时不甚精确的重击。
            面对动能武器时护甲效果加倍。"""

    class FriendlyPACTFastCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'
            self.name = 'Friendly_PACTFastCruiser_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""            


########################################################FRIENDLY PACT ELITE

    class FriendlyPACTEliteMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Missile'
            self.name = 'Friendly_PACTElite_Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。"""
            
    class FriendlyPACTEliteAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 40
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.wtype = 'Assault'
            self.name = 'Friendly_PACTElite_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""            

    class FriendlyPACTEliteLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 230
            self.energy_use = 60
            self.accuracy = 110
            self.shot_count = 1
            self.name = 'Friendly_PACTElite_Laser'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""

    class FriendlyPACTEliteMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 375
            self.energy_use = 50
            self.accuracy = 180
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.shot_count = 1
            self.acc_degradation = 0
            self.type = 'Melee'
            self.shot_count = 1
            self.lbl = Image('Battle UI/button_melee.png')
            self.tooltip = u"""
            切开敌人的太空骑士，造成毁灭性伤害。只能用于
            近身范围的敌人。移动到敌人身边会触发先制反击。"""

############################################## FRIENDLY PACT SUPPORT



############################################# PACT MISSILE FRIGATE

    class PactFrigateMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.shot_count = 6
            self.energy_use = 60

############################################# PIRATE GRUNT

    class PirateGruntLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PirateGruntMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 38
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70

    class PirateGruntAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 60
            self.wtype = 'Assault'


######################################### HAVOC

    class HavocMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 12
            self.accuracy = 80
            self.wtype = 'Missile'
            self.lbl = Image('Battle UI/button_missile.png')
            self.tooltip = u"""
            向敌人发射大量导弹。虽然每发火力较弱，
            但是数量庞大足以造成巨大杀伤。在长距离
            上依然精准。有弹药限制，会被防空火力削弱。
            """

    class HavocAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 30
            self.energy_use = 50
            self.shot_count = 15
            self.accuracy = 70
            self.wtype = 'Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

    class HavocRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 900
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 80
            self.shot_count = 1

    class HavocMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 70    #multiplied by shot count
            self.energy_use = 50
            self.ammo_use = 0
            self.accuracy = 140
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.shot_count = 10
            self.lbl = Image('Battle UI/button_melee.png')
            self.tooltip = u"""
            切开敌人的太空骑士，造成毁灭性伤害。只能用于
            近身范围的敌人。移动到敌人身边会触发先制反击。"""

########################################## PIRATE BOMBER

    class PirateBomberMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Missile'

    class PirateBomberAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 50
            self.shot_count = 20
            self.accuracy = 58
            self.wtype = 'Assault'

    class PirateBomberRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 450
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 60
            self.shot_count = 1

########################################## PIRATE IRONHOG

    class PirateIronhogAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 19
            self.energy_use = 50
            self.shot_count = 25
            self.accuracy = 65
            self.wtype = 'Assault'

    class PirateIronhogRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 275
            self.energy_use = 60
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 80
            self.shot_count = 4

########################################### PIRATE DESTROYER

    class PirateDestroyerLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110

    class PirateDestroyerKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 70

################################################PACT CRUISER

    class PACTCruiserLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 200
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55

    class PACTCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 50
            self.wtype = 'Assault'

################################################PACT FAST CRUISER


    class PACTFastCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 75

    class PACTFastCruiserAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'


################################################RYUVIAN CRUISER

    class RyuvianCruiserMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 60
            self.energy_use = 60
            self.shot_count = 5
            self.accuracy = 110

    class RyuvianCruiserKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 60

################################################RYUVIAN FALCON ENEMY

    class RyuvianFalconEnemyKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 600
            self.energy_use = 50
            self.shot_count = 1
            self.accuracy = 75
            
    class RyuvianFalconEnemyPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 95
            self.wtype = 'Pulse'
            
    class RyuvianFalconEnemyRepair(Support):
            def __init__(self):
                Support.__init__(self)
                self.repair = True
                self.damage = 500 #also used for heals
                self.energy_use = 60
                self.name = 'Repair I'
                self.shot_count = 1

    class RyuvianFalconEnemyRestore(Support):
            def __init__(self):
                Support.__init__(self)
                self.energy_use = 60
                self.modifies = 'restore'
                self.buff_strength = 1
                self.buff_duration = 1
                self.name = 'Restore'

################################################ENEMY SERAPHIM

    class SeraphimEnemyKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.shot_count = 1
            self.accuracy = 150


################################################PACT OUTPOST

    class PACTOutpostLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 150
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 110

    class PACTOutpostKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 150
            self.energy_use = 60
            self.shot_count = 2
            self.accuracy = 50

################################################PACT BATTLESHIP

    class PACTBattleshipLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 250
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTBattleshipKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 500
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55

    class PACTBattleshipAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 50
            self.wtype = 'Assault'

    class PACTBattleshipMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 40
            self.shot_count = 10
            self.accuracy = 80
            self.wtype = 'Missile'

    class PACTBattleshipRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 700
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 80
            self.shot_count = 1

##########################################################PACT TORPEDO DESTROYER

    class PACTDestroyerRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 700
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 90
            self.shot_count = 1

################################################NIGHTMARE ASCENDANT

    class NightmareAscendant_Laser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 120


################################################PACT ASSAULT CARRIER

    class PACTAssaultCarrierLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 320
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 100

    class PACTAssaultCarrierKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 350
            self.energy_use = 60
            self.shot_count = 2
            self.accuracy = 65

    class PACTAssaultCarrierAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 55
            self.wtype = 'Assault'

    class PACTAssaultCarrierMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 80
            self.wtype = 'Missile'

################################################LEGION

    class LegionLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 500
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 100

    class LegionKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.shot_count = 5
            self.accuracy = 65

    class LegionMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 200
            self.energy_use = 50
            self.shot_count = 10
            self.accuracy = 100
            self.wtype = 'Missile'


###################################################################PACT CARRIER

    class PACTCarrierAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 25
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 50
            self.wtype = 'Assault'


#################################################PACT MOOK

    class PACTMookLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 180
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PACTMookMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 30
            self.energy_use = 30
            self.shot_count = 9
            self.accuracy = 70

    class PACTMookAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 70
            self.wtype = 'Assault'


######################################### PACT ELITE

    class PACTEliteMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Missile'

    class PACTEliteAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 18
            self.energy_use = 40
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'

    class PACTEliteLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 230
            self.energy_use = 60
            self.accuracy = 110
            self.shot_count = 1

    class PACTEliteMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 375
            self.energy_use = 50
            self.accuracy = 180
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.shot_count = 1

######################################### PACT SUPPORT

    class PactRepair(Support):
        def __init__(self):
            Support.__init__(self)
            self.repair = True
            self.damage = 300 #also used for heals
            self.energy_use = 60
            self.name = 'Repair I'
            self.shot_count = 1
            self.lbl = Image('Battle UI/button_repair.png')
            self.tooltip = u"""
            为目标回复约300点生命值。
            使用距离有限。"""

    class DisableLite(Curse): #halves available EN
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 100
            self.applied_buff = DisableLiteD
            self.accuracy = 9999
            self.modifies = 'energy regen'
            self.buff_strength = -50
            self.buff_duration = 2
            self.name = 'Disable Lite'
            self.lbl = Image('Battle UI/button_disable.png')
            self.tooltip = u"""
            目标的技能消耗两倍能量。"""

    class PactRestore(Restore):
        def __init__(self):
            Restore.__init__(self)
            self.energy_use = 60
            self.name = 'Restore'
            self.lbl = Image('Battle UI/button_restore.png')
            self.tooltip = u"""
            移除目标身上的敌对属性修正效果。
            使用距离有限。"""

    class PactFlakOff(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 40
            self.applied_buff = FlakOffD
            self.modifies = 'flak'
            self.sort_on = 'pship.flak'
            self.accuracy = 9999
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Flak Off'
            self.lbl = Image('Battle UI/button_flak.png')
            self.tooltip = u"""
            目标两回合内无法先制反击或拦截导弹类武器。"""

    class PactShutOff(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 60
            self.applied_buff = ShieldDown
            self.accuracy = 9999
            self.modifies = 'shield_generation'
            self.sort_on = 'pship.shield_generation'
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Shield Down'
            self.lbl = Image('Battle UI/button_shutoff.png')
            self.tooltip = u"""
            消除目标的护盾两回合。"""


############################################## PIRATE BASE

    class PirateBaseKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 100
            self.energy_use = 60
            self.shot_count = 5
            self.accuracy = 40

    class PirateBaseAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 13
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 40
            self.wtype = 'Assault'

    class PirateBaseMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.shot_count = 15
            self.accuracy = 70
###are these still used?##

    class Rocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 300   #multiplied by shot count
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.accuracy = 60    #seems low, but missiles have very low accuracy degradation over distance.
            self.wtype = 'Rocket'
            self.name = 'Basic Rockets'
            self.shot_count = 2
            self.lbl = Image('Battle UI/button_rocket.png')

    class Flak(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 40
            self.accuracy = 130
            self.acc_degradation = 100 #flak is only useful at point blank range
            self.shot_count = 30  #many shots, but any armor will block it
            self.wtype = 'Assault'
            self.name = 'Basic Flak'
            self.lbl = Image('Battle UI/button_assault.png')

    class MachineGun(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 40
            self.accuracy = 50
            self.shot_count = 15  #many shots, but any armor will block most
            self.wtype = 'Assault'
            self.name = 'Basic Assault'
            self.lbl = Image('Battle UI/button_assault.png')

#################################################### PHOENIX BOOSTER

    class PhoenixBoasterLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 180
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

    class PhoenixBoasterAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 10
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 60
            self.wtype = 'Assault'

########################################## PACT BOMBER

    class PACTBomberMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 40
            self.energy_use = 30
            self.shot_count = 10
            self.accuracy = 70
            self.wtype = 'Missile'

    class PACTBomberRocket(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 500
            self.energy_use = 50
            self.uses_rockets = True
            self.uses_missiles = False
            self.eccm = 10
            self.wtype = 'Rocket'
            self.accuracy = 70
            self.shot_count = 1

    class PACTBomberLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 140
            self.energy_use = 70
            self.shot_count = 1
            self.accuracy = 100

 ###########################################PHOENIX

    class PhoenixAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 12
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 65
            self.wtype = 'Assault'
            self.name = 'Phoenix_Assault'
            self.lbl = Image('Battle UI/button_assault.png')
            self.tooltip = u"""
            弹幕武器发射大量小口径弹幕，即使敌人闪避了
            其中几发，其它依旧可能命中。面对弹幕武器时
            护甲效果加倍。也是用来拦截敌人导弹的防空火力，
            但是连续拦截后效果会减弱。"""

    class PhoenixMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 250    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 60
            self.acc_degradation = 0
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'  #lol
            self.type = 'Melee'
            self.shot_count = 2
            self.lbl = Image('Battle UI/button_melee.png')
            self.tooltip = u"""
            切开敌人的太空骑士，造成毁灭性伤害。只能用于
            近身范围的敌人。移动到敌人身边会触发先制反击。"""


 ###########################################PHOENIX ENEMY

    class PhoenixEnemyMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 250    #multiplied by shot count
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100  #this is needed for AI melee weapons or else range is infinite.
            self.wtype = 'Melee'
            self.name = 'Zantetsuken'
            self.type = 'Melee'
            self.shot_count = 2
            self.lbl = Image('Battle UI/button_melee.png')

################################################# SERAPHIM
    class SeraphimKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 300
            self.energy_use = 100
            self.shot_count = 1
            self.accuracy = 150
            self.tooltip = u"""
            索拉的步枪来自文明更加先进的时代。
            惊人的火力和精度，但是需要大量能量。"""

################################################### BIANCA

    class BiancaAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 250
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 55
            self.wtype = 'Kinetic'
            self.force_counter = True
            self.name = 'Bianca Shotgun'
            self.lbl = Image('Battle UI/button_kinetic.png')
            self.tooltip = u"""
            提供可靠的火力输出。但除非目标很大或距离很近，
            否则并不精准。可以用来进行先制反击。"""


##################################################### UNION FRIGATE


    class UnionFrigateLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 175
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            self.name = 'Trinities'
            self.lbl = Image('Battle UI/button_laser.png')
            self.tooltip = u"""
            激光是长距离上的精准武器，但是火力有限。
            会被敌人的护盾抵消。"""


###################################################NIGHTMARE ASCENDANT FLIER

    class NightmareFlierdroneLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 300
            self.energy_use = 50
            self.shot_count = 1
            self.accuracy = 90

###################################################### NIGHTMARE

    class NightmareMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 900    #multiplied by shot count
            self.energy_use = 30
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1

    class NightmareMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 100
            self.energy_use = 60
            self.shot_count = 15
            self.accuracy = 100
            self.wtype = 'Missile'

    class NightmareLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 575
            self.energy_use = 40
            self.shot_count = 1
            self.accuracy = 120

    class NightmarePulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 70
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 85
            self.wtype = 'Pulse'
            
###################################################### ENEMY BLACKJACK

    class EnemyBlackjackMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 500    #multiplied by shot count
            self.energy_use = 30
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1

    class EnemyBlackjackLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 130

    class EnemyBlackjackPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 50
            self.energy_use = 30
            self.shot_count = 15
            self.accuracy = 100
            self.wtype = 'Pulse'
            
    class EnemyBlackjackAssault(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 20
            self.energy_use = 30
            self.shot_count = 20
            self.accuracy = 70
            self.wtype = 'Assault'

    class EnemyBlackjackKinetic(Kinetic):
        def __init__(self):
            Kinetic.__init__(self)
            self.damage = 150
            self.energy_use = 50
            self.shot_count = 5
            self.accuracy = 80


###################################################### ARCADIUS

    class ArcadiusMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 500    #multiplied by shot count
            self.energy_use = 30
            self.ammo_use = 0
            self.accuracy = 160
            self.acc_degradation = 100
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1

    class ArcadiusMissile(Missile):
        def __init__(self):
            Missile.__init__(self)
            self.damage = 50
            self.energy_use = 60
            self.shot_count = 10
            self.accuracy = 100
            self.wtype = 'Missile'

    class ArcadiusLaser(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 300
            self.energy_use = 40
            self.shot_count = 1
            self.accuracy = 110

    class ArcadiusPulse(Laser):
        def __init__(self):
            Laser.__init__(self)
            self.damage = 50
            self.energy_use = 40
            self.shot_count = 12
            self.accuracy = 78
            self.wtype = 'Pulse'

####boss weapons###

    class BossLaser(Laser):
        #pierces through enemies and ignores 50 points of shielding.
        def __init__(self):
            Laser.__init__(self)
            self.name = 'Boss Laser'
            self.ignore_shielding = 50 #subtractive
            self.damage = 400
            self.energy_use = 60
            self.shot_count = 1
            self.accuracy = 120
            self.wtype = 'Laser'
            
        def fire(self, parent, target, counter = False): 
            if self.parent is None: self.parent = parent
            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))
            
            BM.battle_log_insert(['attack', 'laser'], "{0} attacks {1} with a super laser".format(parent.name, target))
                ## actual damage calculation
            total_damage = 0
            store.total_armor_negation = 0
            store.total_shield_negation = 0
            store.total_flak_interception = 0
            store.hit_count = 0
            
            #get all the hexes in between boss and target location
            if type(target) is tuple: #I do want to be able to target empty hexes
                targetobject = store.object()
                targetobject.location = target
                listlocs = interpolate_hex(parent.location, target)
            else:
                targetobject = target
                listlocs = interpolate_hex(parent.location, target.location)
                
            if self.parent.location in listlocs: listlocs.remove(self.parent.location)
            
            #show shots on map
            BM.shooting = BulletSprite(parent,targetobject,self)
            order_state = BM.order_used 
            # BM.order_used = False #hide order button during animation
            play_sound_effects(self.fire_sound,1)
            
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            renpy.hide_screen('commands')            
            
            renpy.pause(0.75)
            BM.shooting = False

            renpy.show_screen('commands')
            renpy.hide_screen('battle_screen')
            renpy.show_screen('battle_screen')
            #stop showing shots moving across map

            #find list of ship being hit
            ships_hit = []
            for hex in listlocs:
                for ship in BM.ships:
                    if ship.location == hex:
                        ships_hit.append(ship)
                    
            damage_dict = {}
            for ship in ships_hit:
                total_damage = 0
                ship.update_armor()
                
                #cover mechanic. it returns true if cover is hit. see functions.rpy
                if cover_mechanic(self,ship,75):
                    return 'miss'

                for shot in range(self.shot_count):
                    damage = self.damage * parent.energy_dmg * renpy.random.triangular(0.95,1.05)  #add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0
                    if ship.shields > 0:
                        if not self.ignore_shielding:
                            negation = damage * ship.shields / 100.0
                        else:
                            effective_shielding = ship.shields - self.ignore_shielding
                            if effective_shielding < 0: effective_shielding = 0
                            negation = damage * effective_shielding / 100.0
                        damage -= negation
                        if damage < 0: damage = 1
                        store.total_shield_negation += int(negation)
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s shields negated {2} damage of {3}'s laser attack".format(str(shot), ship.name, str(int(negation)), parent.name))

                    if damage <= ship.armor:
                        damage = 1
                        store.total_armor_negation += damage
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s armour withstood {2}'s laser attack".format(str(shot), ship.name, parent.name))
                    else:
                        damage -= ship.armor
                        store.total_armor_negation += ship.armor
                        BM.battle_log_insert(['attack', 'laser', 'detailed'], "<{0}>{1}'s armour negated {2} damage of {3}'s laser attack".format(str(shot), ship.name, ship.armor, parent.name))
                    total_damage += int(damage)
                    store.hit_count += 1
                    damage_dict[ship] = int(total_damage)
                        
            return damage_dict
            
    class BossRocket(SuperRocket):
        def __init__(self):
            SuperRocket.__init__(self)
            self.damage = 600
            self.energy_use = 70
            self.aoe_range = 1 # 0 would be single hex
            self.friendly_fire = True
            self.accuracy = 999 #explosion is big enough that just exploding near the target is fine
            self.eccm = 25
            self.acc_degradation = 0
            self.shot_count = 3
            self.name = "Boss Rocket"
            self.lbl = 'Battle UI/button_rocket.png'
            self.wtype = 'Rocket'
            self.uses_rockets = True
            self.uses_missiles = False
            self.splash_reduction = 0.50  #multiplicative. outside of the prime hex units take 50% damage
            self.ammo_use = 3 #fires 3 rockets at once
            self.shot_count = 1
            
        def fire(self, parent, targets, counter = False):
            #takes a list of 3 targets
            if self.parent is None: self.parent = parent
            BM.missiles = []
            wName = "rocket"
            
            if type(targets) is not list:
                targets = [ (13,7) , (13,9) , (11,11) ]

            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))

            if self.ammo_use > parent.rockets:
                return 'no ammo'
            else:
                parent.rockets -= self.ammo_use
                BM.battle_log_insert(['attack', 'missile'], "{0} attacks with super rocket".format(parent.name))

            #setup
            BM.selectedmode = False
            starting_location = self.parent.location
            BM.selected = parent
            
            max_distance = 0
            for target_location in targets:
                #simulate resulte of flak
                BM.missiles.append = self.simulate(parent,target_location,multi_rocket = True)
                distance = get_distance(starting_location,target_location)
                if distance > max_distance:
                    max_distance = distance
            
            #show missile moving across map
            BM.missile_moving = True
            prepare_map_animation() #hides commands and orders screens
            play_sound_effects(self.fire_sound,1)
            
            store.wait_times = []
            max_wait = 0
            for missile in BM.missiles:
                remaining_wait = get_ship_distance(missile.parent,missile.target)*MISSILE_SPEED*1.5
                if remaining_wait > max_wait: max_wait = remaining_wait
                if not missile.shot_down:                    
                    store.wait_times.append(remaining_wait)
            max_wait += 1
            store.wait_times.sort()
            
            if len(wait_times) == 0:
                renpy.pause(max_wait)
                for ship in BM.ships:
                    ship.flaksim = None
                BM.missile_moving = False
                end_map_animation()
                return 'miss'
            store.wait_times2 = [wait_times[0]]
            if len(wait_times) > 1:
                wait_times2.append(wait_times[1]-wait_times[0])
            if len(wait_times) > 2:
                wait_times2.append(wait_times[2]-wait_times[1])
            for a in range(len(wait_times2)):
                renpy.pause(round(wait_times2[a],1))
                max_wait -= wait_times[a]
                renpy.music.play( 'sound/explosion4.ogg', channel = 'sound{}'.format(a+1))  
                
            if max_wait > 0:renpy.pause(round(max_wait,1))
            
            BM.missile_moving = False
            
            #required with multi-rocket simulation
            for ship in BM.ships:
                ship.flaksim = None
            
            end_map_animation()
            #stop showing missile moving across map

            #reset flak and simulation
            for ship in BM.ships:
                ship.flak_used = False
                ship.flaksim = None

            #start handeling actual damage
            ship_damage_dict = {}
            for missile in BM.missiles:
                if missile.shot_down:
                    continue
                else:
                    target = missile.target.location
                shiplist = get_ships_around_hex(target) #AOE range always 1?
                for ship in shiplist:
                    damage = 0 
                    if not self.friendly_fire:  
                        if ship.faction == parent.faction:
                            continue #to next ship
                    damage = self.damage * parent.missile_dmg * renpy.random.triangular(0.95,1.05)  #add upgrade effect and add a little variation in the damage
                    damage = damage * (100 + parent.modifiers['damage'][0] + BM.environment['damage']) / 100.0 #pretty much defunct now
                    if ship.location != target:
                        damage *= self.splash_reduction
                        if damage < 0: damage = 0
                    damage -= ship.armor
                    store.total_armor_negation += ship.armor
                    if damage <= 1:damage = 1                    
                    store.total_armor_negation = 0
                    if ship in ship_damage_dict:
                        ship_damage_dict[ship] += int(damage)
                    else:
                        ship_damage_dict[ship] = int(damage)
            BM.missiles = []
            return ship_damage_dict            
            
    class BossMelee(Melee):
        def __init__(self):
            Melee.__init__(self)
            self.damage = 800
            self.name = 'Boss Melee'
            self.energy_use = 40
            self.ammo_use = 0
            self.accuracy = 130
            self.acc_degradation = 0
            self.wtype = 'Melee'
            self.type = 'Melee'
            self.shot_count = 1   
            self.force_counter = True
            
init 2 python: ### Buffs ###

    class FullForward(Buff):
        name = "Full Forward"
        tooltip = u"提升百分之二十的伤害和百分之十五的命中"
        affected_stats = ['damage','accuracy']
        duration = 3
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            if stat == 'accuracy':
                return int(v + 15)
            elif stat == 'damage':
                return int(v * 1.20)
                
    class AllGuard(Buff):
        name = "All Guard"
        tooltip = u"提升百分之二十防空火力、百分之十护盾和百分之十闪避"
        affected_stats = ['flak','shield_generation','evasion']
        duration = 3
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            if stat == 'flak':
                return v + 20
            elif stat == 'shield_generation':
                if v > 0: return v + 10
                return v
            elif stat == 'evasion':
                return v + 10
                
    class InjectionRods(Buff):
        name = "All Power To Engines"
        tooltip = u"持续时间内移动消耗能量减半"
        affected_stats = ['move_cost']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            if stat == 'move_cost':
                return int(v / 2)
                
    class AccuracyUpB(Buff):
        name = "Aim Up"
        tooltip = u"增加命中二十五点"
        affected_stats = ['accuracy']
        duration = 3
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            return v + 25
            
    class FlakUpB(Buff):
        name = "Cover"
        tooltip = u"为目标提供火力支援，提高十五点防空火力"
        affected_stats = ['flak']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            return v + 15
            
    class Sentinel(Buff):
        name = "Sentinel"
        tooltip = u"大幅增加护甲，增加敌人攻击目标的几率"
        affected_stats = ['armor','hate']
        
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',curse=False,parent=parent)
            
        def get_modified_stat(self,stat,v):
            if stat == 'armor':
                return (v * 3) + 30 #giving a bit extra because I'm nice like that.            
            elif stat == 'hate':
                return (v+500) * 8
            
    class DamageUpB(Buff):
        name = "Damage Up"
        tooltip = u"增加伤害百分之三十"
        affected_stats = ['damage']
        duration = 3
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            return int(v * 1.3)

    class StealthB(Buff):
        name = "Stealth"
        tooltip = u"""使用者免疫先制反击，并降低敌人攻击目标的几率"""
        affected_stats = ['hate']
        duration = 1
        
        def __init__(self,parent):
            Buff.__init__(self,'utility',parent=parent)
            
        def get_modified_stat(self,stat,v):
            return int(v * 0.25)
    
    class CloakB(Buff):
        name = "Cloak"
        tooltip = u"""让使用者完全从敌人的雷达上消失，变得无法锁定。
        只有敌人的辅助单位可以侦测到并打断这一效果。"""
        affected_stats = ['hate']
        duration = 1
        
        def __init__(self,parent):
            Buff.__init__(self,'utility',parent=parent)
            
        def get_modified_stat(self,stat,v):
            return int(v * 0)
            
    class AwakenedSeraphim(Buff):
        name = "Awakened"
        tooltip = u"增加一百点命中并使伤害翻倍"
        affected_stats = ['accuracy','damage']
        duration = 3
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',parent=parent)
            
        def get_modified_stat(self,stat,v):
            if stat == 'accuracy':
                return v + 100
            elif stat == 'damage':
                return v * 2
                
    class AwakenedAsaga(Buff):
        name = "True Awakening"
        tooltip = u"每回合增加护甲、闪避和伤害，不会失效，对自身造成持续伤害"
        affected_stats = ['armor','evasion','damage']
        duration = -1 #does not expire.
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',parent=parent)
            turn_counter = 1
            
        def get_modified_stat(self,stat,v):
            if stat == 'armor':
                v = v + self.turn_counter #I'm just too nice.
            return int( v * (1.0+0.5*self.turn_counter))
                
        def callback(self):
            self.turn_counter += 1
            #chivo
            if self.turn_counter == 10: chivo_process('I Have the Power!')
            blackjack.hp -= (100 + 50 * self.turn_counter)
            blackjack.update_stats()
            if blackjack.hp < 1:
                blackjack.hp = 1
                # blackjack.hate *= 2  #changed my mind on this
                self.remove()
            return
                
    ##debufs##
        #since debufs tick down at the start of a faction's turn, a duration of 1
        #doesn't do anything as it'll expire right away.
        
    class AccDownD(Buff):
        name = "Aim Down"
        tooltip = u"降低命中二十五点"
        affected_stats = ['accuracy']
        duration = 3
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',curse=True,parent=parent)
            
        def get_modified_stat(self,stat,v):
            return v - 25

    class EvnDownD(Buff):
        name = "SuppressiveFire"
        tooltip = u"降低目标敌人的闪避二十五点"
        affected_stats = ['evasion']
        duration = 1
        
        def __init__(self,parent):
            Buff.__init__(self,'offense',curse=True,parent=parent)
            
        def get_modified_stat(self,stat,v):
            return v - 25


    class DisableD(Buff):
        name = "Disabled"
        tooltip = u"完全瘫痪敌人，包括护盾和防空"
        affected_stats = ['en','flak','shield_generation']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'Utility',curse=True,parent=parent)
            
        def get_modified_stat(self,stat,v):
            return 0 #wow, looks harsh
            
    class DisableLiteD(Buff):
        name = "Disable Lite"
        tooltip = u"武器、技能和移动的消耗加倍"
        affected_stats = ['energy_use','move_cost']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'Utility',curse=True,parent=parent)
            
        def get_modified_stat(self,stat,v):
            return v * 2

    class FlakOffD(Buff):
        name = "Flak Off"
        tooltip = u"防空火力失效"
        affected_stats = ['flak']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',curse=True,parent=parent)
            
        def get_modified_stat(self,stat,v):
            return 0
            
    class ShieldDown(Buff):
        name = "Shield Down"
        tooltip = u"无法产生护盾"
        affected_stats = ['shield_generation']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',curse=True,parent=parent)
            
        def get_modified_stat(self,stat,v):
            return 0

    class ShieldJam(Buff):
        name = "Shield Jam"
        cumulative = True
        tooltip = u"每层降低护盾效果"
        affected_stats = ['shield_generation']
        duration = 2
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',curse=True,parent=parent)
            self.stack_counter = 1
            
        def get_modified_stat(self,stat,v):
            return v - 15 * self.stack_counter
            
    class Disruption(Buff):
        name = "Disruption"
        cumulative = True        
        tooltip = u"积累六层以赢得胜利"
        affected_stats = []
        duration = -1
        
        def __init__(self,parent):
            Buff.__init__(self,'defense',curse=False,parent=parent)
            self.function_at_stacksize = [6,BM.you_win]
            self.stack_counter = 1
            
        def get_modified_stat(self,stat,v):
            return v
            
init -1 python: ### SUPPORT SKILLS ###
    #many of the attributes are now defunct but should be harmless.
            
    class Repair(Support):
        def __init__(self):
            Support.__init__(self)
            self.repair = True
            self.damage = 300 #also used for heals
            self.energy_use = 80
            self.name = 'Repair I'
            self.shot_count = 1
            self.lbl = Image('Battle UI/button_repair.png')
            self.tooltip = u"""
            为目标回复约{}点生命值。
            使用距离有限。""".format(self.damage)

    class AccUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = AccuracyUpB
            self.modifies = 'accuracy'
            self.buff_strength = 25
            self.buff_duration = 3
            self.name = 'Aim Up'
            self.lbl = Image('Battle UI/button_aimup.png')
            self.tooltip = u"""
            为目标增加25点命中。
            使用距离有限。"""

    class FlakUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = FlakUpB
            self.modifies = 'flak'
            self.buff_strength = 15
            self.buff_duration = 3
            self.max_range = 2
            self.energy_use = 50
            self.name = 'Cover'
            self.lbl = Image('Battle UI/button_cover.png')
            self.tooltip = u"""
            为目标提供火力支援，提高15点防空火力
            有效距离三格。"""

    class Taunt(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = Sentinel
            self.modifies = 'armor'
            self.buff_strength = 100
            self.buff_duration = 2
            self.name = 'Taunt'
            self.self_buff = True
            self.lbl = Image('Battle UI/button_drawfire.png') 
            self.tooltip = u"""
            增加护甲，并使敌人攻击你。"""            

    class DamageUp(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = DamageUpB
            self.modifies = 'damage'
            self.buff_strength = 30
            self.buff_duration = 3
            self.name = 'Damage Up'
            self.lbl = Image('Battle UI/button_atkup.png')
            self.tooltip = u"""
            为目标增加百分之三十伤害。
            使用距离有限。"""

    class Restore(Support):
        def __init__(self):
            Support.__init__(self)
            self.modifies = 'restore'
            self.accuracy = 99999
            self.buff_strength = 1
            self.buff_duration = 1
            self.name = 'Restore'
            self.energy_use = 40  #don't refer to this directly, use the energy_cost method instead
            self.lbl = Image('Battle UI/button_restore.png')
            self.tooltip = u"""
            移除目标身上的敌对属性修正效果。
            使用距离有限。"""
            
        def fire(self,parent,target,counter = False,hidden=False):
            if self.parent is None: self.parent = parent
            
            #take away energy
            if parent.en < self.energy_cost(parent):  #energy handling
                return 'no energy'
            else:
                parent.en = increment_attribute(parent,'en',-self.energy_cost(parent))
            
            #bookkeeping
            if parent is target:
                BM.battle_log_insert(['support', 'debuff'], "{0} performs self-restoration".format(parent.name))
            else:
                BM.battle_log_insert(['support', 'debuff'], "{0} attempts to restore {1}".format(parent.name, target.name))
            
            #chivo
            if target.faction == "Player" and len( [f for f in target.buffs if f.curse] ) >= 3: chivo_process('Hello Nurse')
            
            #remove all curses from the target
            target.buffs[:] = [f for f in target.buffs if not f.curse]
            target.update_stats()
            
            #animation
            if not hidden:
                target.getting_buff = True
                BM.selectedmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
                if BM.phase == 'Player':
                    if target is not parent and target.pilot is not None:
                        target.voice("HitBuff")
                message = "All curses were removed from the {}".format(target.name)
                BM.battle_log_insert(['support', 'debuff'], message)
                show_message(message)
                target.getting_buff = False
                if BM.phase == 'Player':
                    BM.selectedmode = True
                    BM.targetingmode = False
                renpy.hide_screen('battle_screen')
                renpy.show_screen('battle_screen')
            return 0

    class Stealth(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = StealthB
            self.self_buff = True
            self.energy_use = 20
            self.accuracy = 100
            self.acc_degradation = 100
            self.modifies = 'stealth'
            self.buff_strength = 100
            self.buff_duration = 1
            self.name = 'Stealth'
            self.lbl = Image('Battle UI/button_stealth.png')
            self.tooltip = u"""
            免疫先制反击一回合，降低敌人攻击你的几率。"""
            
    class Cloak(Stealth):
        def __init__(self):
            Stealth.__init__(self)
            self.applied_buff = CloakB
            self.energy_use = 30
            self.name = 'Cloak'
            self.lbl = Image('Battle UI/button_cloak.png')
            self.tooltip = u"""
            完全从敌人雷达上消失，只有专门的辅助单位
            可以侦测到你并打断隐蔽力场。"""

    class Awaken(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = AwakenedSeraphim
            self.self_buff = True
            self.energy_use = 100
            self.accuracy = 100
            self.hp_cost = 75
            self.acc_degradation = 100
            self.modifies = ['damage','accuracy']
            self.buff_strength = 100
            self.buff_duration = 3
            self.name = 'Awaken'
            self.lbl = Image('Battle UI/button_awaken.png')
            self.tooltip = u"""
            暂时让炽天使的系统过载，三回合内
            增加一百点命中并让伤害翻倍。"""

    class AwakenAsaga(Support):
        def __init__(self):
            Support.__init__(self)
            self.applied_buff = AwakenedAsaga
            self.self_buff = True
            self.energy_use = 100
            self.accuracy = 100
            self.hp_cost = 100
            self.acc_degradation = 100
            self.modifies = ['damage','evasion','armor']
            self.buff_strength = 100
            self.buff_duration = -1
            self.name = 'Awaken Asaga'
            self.lbl = Image('Battle UI/button_asaawaken.png')
            # self.end_of_turn_callback = self.callback
            self.weapon_replace = EndAwakenAsaga()
            self.tooltip = u"""
            增加黑杰克的伤害，闪避和护甲，但是也造成每回合递增的伤害直至取消。"""

        def callback(self):
            if self.parent.has_buff("True Awakening"):
                if self in blackjack.weapons:
                    blackjack.weapons.remove(self)
                    blackjack.weapons.append(EndAwakenAsaga())

    class EndAwakenAsaga(Support):
        def __init__(self):
            Support.__init__(self)
            self.self_buff = True
            self.energy_use = 0
            self.accuracy = 100
            self.name = "Cancel Awakening"
            self.lbl = Image('Battle UI/button_asaawaken.png')
            self.tooltip = u"""
            取消觉醒效果。"""

        def fire(self,parent,target,counter = False):
            blackjack.remove_buff("True Awakening")            
            
            # blackjack.modifiers['damage'] = [0,0]
            # blackjack.modifiers['evasion'] = [0,0]
            # blackjack.modifiers['armor'] = [0,0]
            # blackjack.update_stats()
            # BM.end_turn_callbacks = []
            
            blackjack.remove_weapon(self)
            blackjack.register_weapon(AwakenAsaga())
            
    class Disrupt(Support):  #cast 6 times to win battle
        def __init__(self):
            Support.__init__(self)
            # self.energy_use = self.parent.max_en
            self.accuracy = 9999
            self.self_buff = True
            self.applied_buff = Disruption
            self.modifies = ''
            self.buff_strength = 0
            self.buff_duration = -1
            self.cumulative = True  #do not overwrite but add to the current modifier.
            self.name = 'Disrupt'
            self.lbl = Image('Battle UI/button_disrupt.png')
            self.tooltip = u"""
            使用六次以赢得战斗。"""  
        
        def energy_cost(self,parent):
            if parent is None: parent = self.parent
            if parent is None: 
                set_weapon_parent()
                parent = self.parent
            if parent is None: return 0
            return parent.max_en
            
    class BigGravityGun(GravityGun):
        def __init__(self):
            GravityGun.__init__(self)
            self.works_only_on = None
            self.energy_use = 40
            self.lbl = Image('Battle UI/button_uniongravity.png')
            self.tooltip = u"""
            让使用者将任一单位移动一格。
            如果将敌对单位移动到拥有弹幕武器的
            友方单位身边的话，会触发先制反击。
            使用距离有限。"""

#### curse skills ####

    class AccDown(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.applied_buff = AccDownD
            self.energy_use = 30
            self.modifies = 'accuracy'
            self.accuracy = 9999
            self.buff_strength = -25
            self.buff_duration = 3
            self.name = 'Aim Down'
            self.lbl = Image('Battle UI/button_aimdown.png')
            self.tooltip = u"""
            降低目标的武器精度二十五点。"""

    class SuppressiveFire(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.applied_buff = EvnDownD
            self.energy_use = 30
            self.modifies = 'evasion'
            self.accuracy = 9999
            self.buff_strength = -25
            self.buff_duration = 1
            self.max_range = 3
            self.name = 'Suppressive Fire'
            self.lbl = Image('Battle UI/button_suppress.png')
            self.tooltip = u"""
            向敌人发射EMP炮弹，降低敌人闪避攻击的能力。最大射程三格。"""

    class Disable(Curse): #takes away all EN
        def __init__(self):
            Curse.__init__(self)
            self.applied_buff = DisableD
            self.hate_penalty = 250
            self.energy_use = 100
            self.accuracy = 9999
            self.modifies = ['energy regen','flak', 'shield_generation']
            self.buff_strength = -100
            self.buff_duration = 2 #has to be 2 or else the debuff won't last beyond the start of their next turn
            self.name = 'Disable'
            self.lbl = Image('Battle UI/button_disable.png')
            self.tooltip = u"""
            让目标本回合完全无法行动。"""

    class FlakOff(Curse):
        def __init__(self):
            Curse.__init__(self)
            self.applied_buff = FlakOffD
            self.energy_use = 40
            self.modifies = 'flak'
            self.accuracy = 9999
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Flak Off'
            self.lbl = Image('Battle UI/button_flak.png')
            self.tooltip = u"""
            目标两回合内无法先制反击或拦截导弹类武器。"""

    class ShutOff(Curse):  #shuts down shield generation
        def __init__(self):
            Curse.__init__(self)
            self.applied_buff = ShieldDown
            self.energy_use = 60
            self.accuracy = 9999
            self.modifies = 'shield_generation'
            self.buff_strength = -100
            self.buff_duration = 2
            self.name = 'Shield Down'
            self.lbl = Image('Battle UI/button_shutoff.png')
            self.tooltip = u"""
            消除目标的护盾两回合。"""

    class ShdJam(Curse):  #shuts down shield generation
        def __init__(self):
            Curse.__init__(self)
            self.energy_use = 40
            self.accuracy = 9999
            self.applied_buff = ShieldJam
            self.modifies = 'shield_generation'
            self.buff_strength = -15
            self.buff_duration = 1
            self.cumulative = True  #do not overwrite but add to the current modifier.
            self.name = 'Shield Jam'
            self.lbl = Image('Battle UI/button_shdjam.png')
            self.tooltip = u"""
            暂时降低目标的护盾十五点，可以叠加。"""
            
init -1 python: ## store items ##
    # see classes.rpy for more details on what each field does

    class NewWarhead(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'new warhead'
            self.display_name = u"火箭弹头"
            self.cost = 300
            self.tooltip = u'购买弹头后，太阳骑士号可以向敌人发射威力强大的火箭。一枚火箭造成{}伤害，但是可以被敌人的防空火力击落。太阳骑士号最多同时携带[sunrider.max_rockets]枚火箭。'.format(sunrider.weapons[3].damage)
            self.variable_name = 'sunrider.rockets'    #this decides what is shown in the store after [owned:
            # self.visibility_condition = 'sunrider.rockets < sunrider.max_rockets'
            self.max_amt = sunrider.max_rockets    #you can buy no more than this number of this item. see previous field

        def buy(self): #here is where you decide what this item -does-.
            sunrider.rockets += 1

    class RocketUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'Rocketupgrade1'
            self.display_name = u"量子弹头许可"
            self.cost = 2000
            self.tooltip = u'核弹头的取得相当容易，但是威力更大的武器一直在联盟的严格管控之下。通过支付相应的费用，矿业联合可以将您的核弹头升级为量子弹头，永久增加太阳骑士号火箭武器的基础伤害百分之五十。'
            self.visibility_condition = 'sunrider_rocket.damage < 1200'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            store.sunrider_rocket.damage = 1200
            store.sunrider_rocket.keep_after_reset['damage'] = 1200

    class RepairUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'RepairUpgrade1'
            self.display_name = u"携带式修理机器人"
            self.cost = 1000
            self.tooltip = u'尽管全面的修理需要在干船坞慢慢进行，战场修理技术仍然是必不可少的。这些最新的可携带式修理机器人允许“自由”的修理量提高200点，同时降低修理技能的能量消耗10点。'
            self.visibility_condition = 'store.chigara_repair.damage < 500'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            store.chigara_repair.damage = 500
            store.chigara_repair.keep_after_reset['damage'] = 500
            store.chigara_repair.energy_use = 70
            store.chigara_repair.keep_after_reset['energy_use'] = 70

    class NewRepairDrone(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'repair drones'
            self.display_name = u"修理机器人"
            self.cost = 400
            self.tooltip = u'这些自动机器人可以快速修复舰体的受损部分和电子设备，是居家旅行的必需品。恢复太阳骑士号一半生命值，最多携带8个。'
            self.visibility_condition = 'sunrider.repair_drones != None'
            self.variable_name = 'sunrider.repair_drones'
            self.max_amt = 8

        def buy(self):
            sunrider.repair_drones += 1

    class ContractAllianceCruiser(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'alliance cruiser'
            self.display_name = u"联盟巡洋舰"
            self.cost = 2000
            self.variable_name = "get_shipcount_in_list('Alliance Cruiser',player_ships)"
            self.max_amt = 2
            self.tooltip = u'太阳议会宣战后，无数的联盟战斗巡洋舰加入了战斗。如果支付相应的费用，矿业联合可以利用在太阳议会的影响力让一艘状态良好的联盟战斗巡洋舰作为太阳骑士号的护卫行动。尽管速度不快，联盟的战斗巡洋舰威力无比同时固若金汤。最多同时保有{}艘。'.format(self.max_amt)
            self.background_image = "store/item_mercenary.png"
            

        def buy(self):
            create_ship(AllianceCruiser()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1

    class ContractUnionFrigate(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'union frigate'
            self.display_name = u"联合护卫舰"
            self.cost = 750
            self.variable_name =  "get_shipcount_in_list('Mining Union Frigate',player_ships)"
            self.max_amt = 3
            self.tooltip = u'矿业联合有一支庞大的部队用来击退海盗。只要支付相应的费用，您也可以得到一艘联合的护卫舰来保护您的安全。这些护卫舰尽管小而脆弱，但是廉价且迅速。最多同时保有{}艘。'.format(self.max_amt)
            self.background_image = "store/item_mercenary.png"

        def buy(self):
            create_ship(UnionFrigate()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1

    class ContractCeraGunboat(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'ceragunboat'
            self.display_name = u"瑟拉炮艇"
            self.cost = 750
            self.variable_name =  "get_shipcount_in_list('Cera Gunboat',player_ships)"
            self.max_amt = 4
            self.visibility_condition = "store.mission2_complete"
            self.tooltip = u'一整支宇宙舰队并不会瞬间蒸发。瑟拉的迅速沦陷让一些部队分散在星系各处却没有统一指挥。通过支付一些费用，您可以让一些灵巧的瑟拉炮艇回到您的舰队。作为可以同时在宇宙和大气圈内使用的火力支援运输船，这些炮艇可以为大型战舰提供防空和反太空骑士火力。最多同时保有{}艘。'.format(self.max_amt)
            self.background_image = "store/item_mercenary.png"

        def buy(self):
            create_ship(CeraGunboat()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1

    class ContractRyuvianFalcon(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'ryuvianfalcon'
            self.display_name = u"鲁维亚隼鹰级"
            self.cost = 1500
            self.variable_name =  "get_shipcount_in_list('Ryuvian Falcon',player_ships)"
            self.max_amt = 2
            self.visibility_condition = "store.discoverfalcon == True"
            self.tooltip = u'通过古战场回收的材料和数据，我们得以生产出在帕西姆斯星云遭遇的鲁维亚幽灵船。尽管和原版仍有差距，隼鹰级依旧是危险的驱逐舰，装有巨大的动能炮和脉冲炮。她的速度和机动性远超一般舰型。最多同时保有{}艘。'.format(self.max_amt)
            self.background_image = "store/item_mercenary.png"

        def buy(self):
            create_ship(RyuvianFalcon()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1

    class ContractUnionBattleship(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'unionbattleship'
            self.display_name = u"联合战舰"
            self.cost = 3000
            self.variable_name =  "get_shipcount_in_list('Union Battleship',player_ships)"
            self.max_amt = 1
            self.visibility_condition = "store.mission5_complete == True"
            self.tooltip = u'尽管矿业联合小行星采掘船的主业是采集矿石，坚实的护甲、强力的激光和引力射线让这种巨型船只成为了强大的战舰。尽管矿业联合宣称这些武器只是用来驱逐海盗的，批评者们依旧指出这只是拙劣的伪装，这些采掘船是矿业联合用来维护自己在各大矿区利益的战舰。最多同时保有{}艘。'.format(self.max_amt)
            self.background_image = "store/item_mercenary.png"

        def buy(self):
            create_ship(UnionBattleship()) #location=None, weaponlist=[] i.e. default
            BM.mercenary_count += 1

    class SellWishallArtifact(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'wishall'
            self.display_name = u"出售愿望机"
            self.cost = -10000
            self.tooltip = u'愿望机是古鲁维亚遗物，可以让拥有者进行一次免费的指挥决断。另外，您也可以在这里出售它以得到10 000元。'
            self.visibility_condition = "store.wishall"

        def buy(self): #here is where you decide what this item -does-.
            store.wishall = False

    class SunriderShieldUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'sunrider_shield_upgrade'
            self.display_name = u"太阳骑士护盾"
            self.cost = 1500
            self.tooltip = u"由于太阳骑士号的意外离港，她没来得及装备上能量护盾。尽管她的原装护盾随着瑟拉的沦陷失落了，矿业联合可以为她配备一个基础型护盾装置。护盾购买后可以在研究室进一步升级。"
            self.visibility_condition = 'store.sunrider.shield_generation == 0'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            store.sunrider.shield_generation = 15
            store.sunrider.shields = store.sunrider.shield_generation
            store.sunrider.shield_range = 0

    class OngessiteThrusters(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'black_jack_thrusters'
            self.display_name = u"液态昂格希特燃料"
            self.cost = 1500
            self.tooltip = u"对昂格斯的占领让联盟得到了稳定的昂格希特供应。黑杰克和帕拉丁可以使用高品质液态昂格希特作为燃料，减少移动的能量消耗百分之二十五。"
            self.visibility_condition = 'store.blackjack.move_cost > 15 and store.OngessTruth == False'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            store.blackjack.move_cost = 15
            store.paladin.move_cost = 30

    class GravityGunBooster(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'gravity_gun_booster'
            self.display_name = u"引力发生器"
            self.cost = 500
            self.tooltip = u"切嘉拉可以通过安装这种设备让比安卡的引力武器更加高效，能量消耗降至40。"
            self.visibility_condition = 'store.bianca.weapons[1].energy_use == 60'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            store.bianca.weapons[1].energy_use = 40
            store.bianca.weapons[1].keep_after_reset['energy_use'] = 40
            
    class ShipCLeanUp(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'Ship Clean Up'
            self.display_name = u"火箭贮藏舱"
            self.cost = 2000
            self.tooltip = u"并非所有设备都需要占据庞大的空间。大副艾瓦在船上装上了大量的非必要设备，它们可以升级甚至直接丢弃来为更重要的装备提供空间。允许太阳骑士号多携带一枚火箭。"
            self.visibility_condition = "sunrider.max_rockets == 2"
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            sunrider.max_rockets += 1
            store.store_items[0].__init__()  #needed to update the new maximum so you can buy more

    class RepairDronesMk2(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'Repair Drones Mk2'
            self.display_name = u"修理机器人II型"
            self.cost = 1800
            self.tooltip = u"由于中立星缘的战争需求，矿业联合的科学家们赶制出了新型的修理机器人。新型号采用了更高级的材料，提升了战斗环境下的工作稳定性，并升级了AI使得修理能力进一步上升。修理机器人现在恢复百分之七十五的最大生命。"
            self.visibility_condition = "BM.repair_drone_heal == 0.5"
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            BM.repair_drone_heal = 0.75
            
    class OngessiteInjectionRods(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'Ongessite Injection Rods'
            self.display_name = u"昂格希特能量棒"
            self.cost = 3000
            self.tooltip = u"联盟科学家的最新发明。这些昂格希特能量棒可以让几乎所有引擎焕发生机。解锁“全速前进”指令：消耗800指挥点数，玩家的所有单位移动消耗能量减半。"
            self.visibility_condition = "'ALL POWER TO ENGINES' not in BM.orders and not OngessTruth"
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            BM.orders["ALL POWER TO ENGINES"] = [800,'injection_rods']            

    class ArmorPenetratingRoundsAsaga(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'Asagas armor penetrating rounds'
            self.display_name = u"穿甲弹"
            self.cost = 3000
            self.tooltip = u"这些弹药可以通过黑杰克的突击步枪发射，能够有效穿透装甲。为黑杰克增加动能武器攻击，造成100x4的动能伤害。" 
            self.visibility_condition = "not blackjack.has_weapon('Blackjack Kinetic')"
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            blackjack.register_weapon(BlackjackKinetic())
            
    class MIRVTorpedoLicence(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = 'MIRV Quantum Torpedo License'
            self.display_name = u"MIRV量子弹头许可"
            self.cost = 8000
            self.tooltip = u"尽管这被联盟的法律禁止，但我们并没有遵守他们法律的必要不是吗？只要向矿业联合支付一笔可观的费用，他们就可以为我们提供弹头，同时解决掉包括一万两千页“使用条款”在内的法律问题。太阳骑士号的火箭可以造成溅射伤害。" 
            self.visibility_condition = 'sunrider_rocket.damage == 1200 and sunrider_rocket.aoe_range == 0'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            store.sunrider.weapons[3] = SunriderMIRV()
            store.sunrider_rocket = store.sunrider.weapons[3]
            
    class PortableShieldGeneratorUpgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = "Portable Shield Generator Upgrade"
            self.display_name = u"可携带式护盾装置"
            self.cost = 1500
            self.tooltip = u"在发掘一颗偏远行星的时候，矿业联合出土了一台古代太空骑士。尽管太空骑士本身已经无法使用，其驾驶员的遗骸持有着一台单人护盾装置。这种装置可以装在自由的浮游机器人上，让它可以把自己的护盾转移到地图的其他位置。"
            self.visibility_condition = 'not liberty.has_weapon("Portable Shield Generator")'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            liberty.register_weapon(PortableShieldGenerator()) 

    class AllianceHoloShow(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = "Alliance Holo Show"
            self.display_name = u"召唤联盟战舰"
            self.cost = 4000
            self.tooltip = u"支付相应费用后，矿业联合会在各大媒体的黄金时段播放太阳骑士号的奋战和成就。由于这个节目的影响，联盟愿意保护太阳骑士号的安全，防止这艘知名战舰发生意外……解锁“召唤联盟战舰”指令：消耗2000指挥点数，召唤一艘联盟战舰三回合。"
            self.visibility_condition = '"SUMMON BATTLESHIP" not in BM.orders and (store.mission3_complete or store.mission4_complete)'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            BM.orders["SUMMON BATTLESHIP"] = [2000,'summon battleship']
            
    class UpgradeStealth(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = "Upgrade Stealth"
            self.display_name = u"隐蔽力场发生器"
            self.cost = 2200
            self.tooltip = u"一个可以让太空骑士从所有常规光学和电子侦测仪器中消失的鲁维亚遗物。将它装在凤凰上后，潜行效果下的凤凰将不可被选为攻击目标。附近的敌人辅助单位可以解除这一效果。"
            self.visibility_condition = 'not phoenix.has_weapon("Cloak") and affection_icari >= 5'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            phoenix.weapons[2] = Cloak()
            
    class CMDupgrade(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = "CMD upgrade"
            self.display_name = u"舰长团介绍信"
            self.cost = 5000
            self.tooltip = u"矿业联合能够将您引荐到太空巨鲸舰长团，这是名垂青史的精英舰长们才有资格加入的团体。提升指挥点数上限至5000点。"
            self.visibility_condition = 'BM.max_cmd < 5000'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            BM.max_cmd = 5000
            
    class VanguardSplash(StoreItem):
        def __init__(self):
            StoreItem.__init__(self)
            self.id = "Vanguard Splash"
            self.display_name = u"先锋扩散力场"
            self.cost = 20000
            self.tooltip = u"一个威力巨大的鲁维亚遗物，其产生等离子场的能力可以用来提升先锋火炮的伤害范围。当然，从矿业联合购买它的价格可不便宜。先锋火炮可以造成溅射伤害。"
            self.visibility_condition = 'BM.vanguard_splash == False'
            self.background_image = "store/item_upgrade.png"

        def buy(self):
            BM.vanguard_splash = True           
            
python early: ## achievements ##

    class Lucky(Achievement):
        name = 'Lucky!'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Survive an attack with less than 10hp remaining."
            self.icon = "lucky_locked.png"
            
    class Unlucky(Achievement):
        name = 'Unlucky!'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Have a player unit get killed at 0 to -9 HP."
            self.icon = "unlucky_locked.png"
    
    class LoseALife(Achievement):
        name = 'Lose a life'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Have a non-mercenary player unit get destroyed for the first time."            
            self.icon = "loselife_locked.png"
            
    class PeopleDieWhenTheyAreKilled(Achievement):
        name = 'People Die When They Are Killed'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Lose a mercenary unit."
            self.icon = "peopledie_locked.png"
            
    class SpreadOut(Achievement):
        name = 'Spread Out!'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Have 5 player ships or more get hit by an AoE rocket."
            self.icon = "spreadout_locked.png"
       
    class IHaveThePower(Achievement):
        name = 'I Have the Power!'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Get 10 stacks of 'Awakening' on Asaga."
            self.icon = "ihavepower_locked.png"
            
    class PhoenixDown(Achievement):
        name = 'Phoenix Down'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Revive the Phoenix twice in the same battle."
            self.times_revived = 0
            self.icon = "phoenixdown_locked.png"
            
        def process(self):
            if self.active:
                self.times_revived += 1
                if self.times_revived > 1:
                    self.unlock()
                    
        def end_mission(self):
            self.times_revived = 0

    class Vengeance(Achievement):
        name = 'Vengeance'
        def __init__(self):
            self.stat_max = 1000
            self.stat_modulo = 100
            Achievement.__init__(self)
            self.description = "Kill 1000 enemies."
            self.tracked_value = 0
            self.icon = "vengeance_locked.png"
            
        def process(self):
            if self.active:
                self.tracked_value += 1
                # store.achievement.progress(self.name,1)
                if self.tracked_value >= 1000:
                    self.unlock()
            
    class LibertyOrDeath(Achievement):
        name = 'Liberty or Death'
        def __init__(self):
            self.stat_max = 50000
            self.stat_modulo = 5000
            Achievement.__init__(self)
            self.description = "Repair 50'000 hp in battle with the Liberty."
            self.tracked_value = 0
            self.icon = "liberty_locked.png"
            
        def process(self,amount):
            if self.active:
                self.tracked_value += amount
                # store.achievement.progress(self.name,amount)
                if self.tracked_value >= 50000:
                    self.unlock()

    class Captain(Achievement):
        name = 'Captain'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Beat the game on Captain difficulty or higher."
            self.missions_completed = set()
            self.icon = "captain_locked.png"
            
        def end_mission(self):
            if self.active:
                if BM.lowest_difficulty >= 3:
                    if BM.mission == self.total_missions:
                        self.unlock()
                        
    class Admiral(Achievement):
        name = 'Admiral'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Beat the game on Admiral difficulty or higher."
            self.missions_completed = set()
            self.icon = "admiral_locked.png"
            
        def end_mission(self):
            if self.active:
                if BM.lowest_difficulty >= 4:
                    if BM.mission == self.total_missions:
                        self.unlock()

    class SpaceWhaleRancher(Achievement):
        name = 'Space Whale Rancher'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Beat the game on Space Whale difficulty. Yeah, good luck with that."
            self.missions_completed = set()
            self.icon = "spacewhale_locked.png"
            
        def end_mission(self):
            if self.active:
                if BM.lowest_difficulty >= 5:
                    if BM.mission == self.total_missions:
                        self.unlock()
                        show_message("Congratulations! You are officially better at the game than the people who made it.")

    class ByTheSkinOfOurTeeth(Achievement):
        name = 'By the Skin of Our Teeth'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Win a battle with only the Sunrider left alive."
            self.icon = "byskin_locked.png"
            
        def end_mission(self):
            if len(player_ships) == 1:
                self.unlock()

    class PennyPincher(Achievement):
        name = 'Penny Pincher'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Complete the game without buying anything at the store."
            self.icon = "pennypincher_locked.png"
            
        def end_mission(self):
            if self.name not in BM.achievement_data:
                BM.achievement_data[self.name] = True
            if BM.achievement_data[self.name]:
                if BM.mission == self.total_missions:
                    if BM.achievement_data[self.name]:
                        self.unlock()
        
        def process(self):
            if self.active:
                BM.achievement_data[self.name] = False

    class IsntItSad(Achievement):
        name = "Isn't it Sad, Chigara?"
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Complete the game without ever buying new upgrades."
            self.icon = "aintitsad_locked.png"
        
        def end_mission(self):
            if self.name not in BM.achievement_data:
                BM.achievement_data[self.name] = True
            if BM.achievement_data[self.name]:
                if BM.mission == self.total_missions:
                    if BM.achievement_data[self.name]:
                        self.unlock()           
                    
        def process(self):
            if self.active:
                BM.achievement_data[self.name] = False                    

    class TooAwesomeToUse(Achievement):
        name = 'Too Awesome to Use'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Complete the game with the wishall still in your inventory."
            self.icon = "tooawesome_locked.png"
        
        def end_mission(self):
            if self.active:
                if BM.mission == self.total_missions and store.wishall:
                    self.unlock()
                    
    class CantTouchThis(Achievement):
        name = "Can't Touch This"
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Use short range warp 3 times in the same turn."
            self.warp_count = 0
            self.icon = "canttouch_locked.png"
            
        def process(self):
            if self.active:
                self.warp_count += 1
                if self.warp_count >= 3:
                    self.unlock()
                    
        def end_turn(self):
            if self.active:
                self.warp_count = 0
                
        def end_mission(self):
            self.end_turn()                
            
    class MeetMyLittleFriend(Achievement):
        name = 'Meet My Little Friend'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Kill a PACT support with melee."
            self.icon = "meetfriend_locked.png"

    class NaturalEnemy(Achievement):
        name = 'Natural Enemy'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Kill 2 PACT support units in the same turn with Sola."
            self.kill_count = 0
            self.icon = "naturalenemy_locked.png"
            
        def end_turn(self):
            if self.active:
                self.kill_count = 0
                
        def end_mission(self):
            self.end_turn()
                
        def process(self):
            if self.active:
                self.kill_count += 1
                if self.kill_count >= 2:
                    self.unlock()

    class Domination(Achievement):
        name = 'Domination'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Kill 10 units in the same turn."
            self.kill_count = 0
            self.icon = "domination_locked.png"
            
        def end_turn(self):
            if self.active:
                self.kill_count = 0
                
        def end_mission(self):
            if self.active:
                self.kill_count = 0
                
        def process(self):
            if self.active:
                self.kill_count += 1
                if self.kill_count >= 10:
                    self.unlock()
            
    class Mogul(Achievement):
        name = 'Mogul'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Save up to 50'000 credits."
            self.icon = "dollar_locked.png"

    class ThisIsMyCommand(Achievement):
        name = 'This is My Command!'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Use vanguard for the fist time."   
            self.icon = "thiscommand_locked.png"

    class GrandTactician(Achievement):
        name = 'Grand Tactician'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Hit 8 units at once."   
            self.icon = "grandtactician_locked.png"

    class FormingTheFleet(Achievement):
        name = 'Forming the Fleet'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Contract your first merc."
            self.icon = "formingfleet_locked.png"
            
        def process(self):
            if self.active:
                for ship in player_ships:
                    if ship.mercenary:
                        self.unlock()
            
    class CompulsiveHoarding(Achievement):
        name = 'Compulsive Hoarding'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Buy at least 20 different things in the store (including merc contracts)."
            self.bought_items = set()
            self.icon = "hoarder_locked.png"
            
        def process(self,item):
            if self.active:
                self.bought_items.add(item.id)
                if len(self.bought_items) >= 20:
                    self.unlock()

    class AllForOne(Achievement):
        name = 'All For One'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Put all debufs (except Disable) on the same enemy."   
            self.icon = "allforone_locked.png"
            
        def process(self,enemy):
            if self.active:
                if len(enemy.buffs) >= 5: #enemies don't buff themselves... right? would have to make a list comprehension if they did.
                    self.unlock()
            
    class OneForAll(Achievement):
        name = 'One For All'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Put 5 different buffs on the same friendly unit."
            self.icon = "oneforall_locked.png"
            
        def process(self,friendly):
            if self.active:
                if len([f for f in friendly.buffs if not f.curse]) >= 5: #hint: power to engines is a separate buff to full forward
                    self.unlock()
            
    class HelloNurse(Achievement):
        name = 'Hello Nurse'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Have Bianca use Restore on an allied unit afflicted by all possible debuffs."
            self.icon = "hellonurse_locked.png"

    class WithOneRyder(Achievement):
        name = 'With One Ryder Tied Behind My Back.'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Complete a battle while ignoring one of your Ryders."
            self.idle_units = set()
            self.icon = "onehand_locked.png"
            
        def end_turn(self):
            if self.active:
                for ship in player_ships:
                    
                    #skip and remove ships without a location
                    if ship.location is None: 
                        if ship.name in self.idle_units:
                            self.idle_units.remove(ship.name)
                        continue
                        
                    #ending up with less than max EN disqualifies a unit
                    if ship.name in self.idle_units and ship.en != ship.max_en:
                        self.idle_units.remove(ship.name)
                    
                    #ending a turn with max EN on turn 1 adds it to the idle units list
                    if BM.turn_count == 1 and ship.en == ship.max_en and ship.stype == 'Ryder':
                        self.idle_units.add(ship.name)
                        
                #when at the end of a turn no units were idle this chivo was failed this mission
                if len(self.idle_units) == 0:
                    self.active = False #failed
                    
        def end_mission(self):
            if self.active:
                self.end_turn()
                if self.active:
                    self.unlock()
            else:
                if not self.cleared:
                    self.active = True

    class Deathwish(Achievement):
        name = 'Deathwish'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Have the Paladin get destroyed with Draw Fire ability active." 
            self.icon = "deathwish_locked.png"

    class BlackJackChivo(Achievement):
        name = 'Black Jack'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Perform exactly 21 attacks with Black Jack in a battle." 
            self.hidden = True
            self.attribution = "Akioklaus"
            self.attack_count = 0
            self.icon = "blackjack_locked.png"
            
        def end_mission(self):
            if self.active:
                if self.attack_count == 21:
                    self.unlock()
                self.attack_count = 0
                
        def process(self):
            if self.active:
                self.attack_count +=1

    class StingLikeABee(Achievement):
        name = 'Sting Like a Bee'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Destroy a capital ship with an assault weapon." 
            self.attribution = 'SayuriUliana'
            self.icon = "stingbee_locked.png"

    class ThereCanBeOnlyOne(Achievement):
        name = 'There Can Only Be One'
        def __init__(self):
            self.stat_max = 30
            self.stat_modulo = 10
            Achievement.__init__(self)
            self.description = "Kill 30 units with melee." 
            self.attribution = 'SayuriUliana'
            self.tracked_value = 0
            self.icon = "onlyone_locked.png"
            
        def process(self):
            if self.active:
                self.tracked_value += 1
                # store.achievement.progress(self.name,1)
                if self.tracked_value >= 30:
                    self.unlock()

    class WhatAreYouImplying(Achievement):
        name = 'What Are You Implying?'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Have both the Phoenix and the Paladin end their turns next to each other every turn for an entire battle"
            self.attribution = 'Sir Fluffykins'
            self.hidden = True
            self.icon = "implying_locked.png"
            
        def end_turn(self):
            if self.active:
                if get_ship_distance(phoenix,paladin) > 1:
                    self.active = False #failure
                    
        def end_mission(self):
            if self.active:
                self.end_turn()
                if self.active:
                    self.unlock()
            else:
                if not self.cleared:
                    self.active = True

    class CosetteCaptured(Achievement):
        name = 'Cosette Captured'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Capture Cosette."
            self.icon = "cosettecaptured_locked.png"            
            self.hidden = True
            
    class CosetteDead(Achievement):
        name = 'No Loli Space Pirate Route'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Kill Cosette."
            self.icon = "cosettedead_locked.png"            
            self.hidden = True
            
    class WelcomeBack(Achievement):
        name = 'Welcome Back Captain'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Finish the prologue."
            self.icon = "welcomeback_locked.png"            
            self.hidden = True
            
    class HavocRestored(Achievement):
        name = 'Havoc Restored'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Restore the Havoc."
            self.icon = "havocrestored_locked.png"            
            self.hidden = True
            
    class FalconChivo(Achievement):
        name = 'Falcon Discovered'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Scavage the starship grave yard to discover the Falcon."
            self.icon = "falcon_locked.png"            
            self.hidden = True

    class NoFalcon(Achievement):
        name = 'No Falcon'
        def __init__(self):
            Achievement.__init__(self)
            self.description = "Leave the starship grave yard alone."
            self.icon = "nofalcon_locked.png"            
            self.hidden = True
    
            
            
            
            
            
            
            
            