import random
import os
import tkinter
def maggen():

    print("Spell Effect is:")
    phys_effects = \
        ["Animating", "Attracting", "Binding","Blossoming", "Consuming","Creeping","Crushing","Diminishing","Dividing",
         "Dividing", "Duplicating","Enveloping","Expanding","Fusing","Grasping","Hastening","Hindering","Illuminating",
         "Imprisoning","Levitating", "Opening", "Petrifying", "Phasing", "Piercing", "Pursuing", "Reflecting",
         "Regenerating", "Rending","Repelling", "Resurrecting", "Screaming", "Sealing", "Shapeshifting", "Shielding",
         "Spawning", "Transmuting", "Transporting"]

    phys_elements = \
        ["Acid","Amber","Bark","Blood","Bone","Brine","Clay","Crow","Ember","Flesh","Fungus","Sand","Sap","Serpent",
         "Slime","Stone","Tar","Glass","Honey","Ice","Insect","Wood","Lava","Thorn","Vine","Water","Wine","Wood","Worm"]

    phys_forms = \
    ["Altar","Armor","Arrow","Beast","Blade","Cauldron","Chain","Chariot","Claw","Cloak","Colossus","Crown","Elemental",
     "Eye","Fountain","Gate","Golem","Hammer","Horn","Key","Mask","Monolith","Pit","Prison","Sentinel","Servant",
     "Shield","Spear","Steed","Swarm","Tentacle","Throne","Torch","Trap","Wall","Web"]

    eth_effects = \
        ["Avenging","Banishing","Bewildering","Blinding","Charming","Communicating","Compelling","Concealing",
         "Deafening","Deceiving","Deciphering","Disguising","Dispelling","Emboldening","Encoding","Energizing",
         "Enraging", "Excruciating","Foreseeing","Intoxicating","Maddening","Mesmerizing","Mindreading","Nullifying",
         "Paralyzing","Revealing","Revolting","Scrying","Silencing","Soothing","Summoning","Terrifying","Warding",
         "Wearying","Withering"]

    eth_elements = \
    ["Ash","Chaos","Distortion","Dream","Dust","Echo","Ectoplasm","Fire","Fog","Ghost","Harmony","Heat","Light",
     "Lightning","Memory","Mind","Mutation","Negation","Plague","Plasma","Probability","Rain","Rot","Shadow","Smoke",
     "Snow","Soul","Star",'Stasis',"Steam","Thunder","Time","Void","Warp","Whisper",'Wind']

    eth_forms = \
    ["Aura","Beacon","Beam","Blast","Blob","Bolt","Bubble","Call","Cascade","Cloud","Circle","Coil", "Cone","Cube",
     "Dance","Disk","Field","Form","Gaze","Loop","Moment","Nexus","Portal","Pulse","Pyramid","Ray","Shard","Sphere",
     "Spray","Storm","Swarm","Torrent","Touch","Vortex","Wave","Word"]


    random.seed()

    choice = random.randint(1, 12)

# This could be done in a single line, but who has time to think about programming?

    if choice == 1:
        return(random.choice(phys_effects) + " " + random.choice(phys_forms))  # 1
    elif choice == 2:
        return(random.choice(phys_effects) + " " + random.choice(eth_forms))  # 2
    elif choice == 3:
        return(random.choice(phys_effects) + " " + random.choice(phys_elements))  #
    elif choice == 4:
        return(random.choice(phys_effects) + " " + random.choice(eth_elements))  # 4
    elif choice == 5:
        return(random.choice(eth_effects) + " " + random.choice(eth_forms))  # 5
    elif choice == 6:
        return(random.choice(eth_effects) + " " + random.choice(phys_forms))  # 6
    elif choice == 7:
        return(random.choice(eth_effects) + " " + random.choice(phys_elements))  # 7
    elif choice == 8:
        return(random.choice(eth_effects) + " " + random.choice(eth_elements))  # 8
    elif choice == 9:
        return(random.choice(phys_elements) + " " + random.choice(phys_forms))  # 9
    elif choice == 10:
        return(random.choice(phys_elements) + " " + random.choice(eth_forms))  # 10
    elif choice == 11:
        return(random.choice(eth_elements) + " " + random.choice(phys_forms))  # 11
    elif choice == 12:
        return(random.choice(eth_elements) + " " + random.choice(eth_forms))  # 12



def main():
        print(maggen())




main()