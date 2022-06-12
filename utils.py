from .models import Monster
import re

class Knowledge:
    def attributeOfMonster(id):
        monster = Monster.objects.get(pk = id)
        monsterAttr = getattr(monster, 'c_attribute')
        return Monster.objects.filter(c_attribute = monsterAttr)

    def raceOfMonster(id):
        monster = Monster.objects.get(pk = id)
        monsterRace = getattr(monster, 'c_race')
        return Monster.objects.filter(c_race = monsterRace)


    def descriptionContainsAttribute(id):
        attributes = ['DARK', 'LIGHT', 'WATER', 'FIRE', 'WIND', 'EARTH', 'DIVINE']
        monster = Monster.objects.get(pk=id)
        list_of_all_results = list()
    
        matches = [attr for attr in attributes if attr in getattr(monster, 'c_description')]
        
        for match in matches:
            list_of_monsters_with_attribute = Monster.objects.filter(c_attribute = match)
            list_of_all_results.append(list_of_monsters_with_attribute)

        return list_of_all_results
    

    def descriptionContainsRace(id):
        races = ['Beast', 'Aqua', 'Insect', 'Fish', 'Spellcaster', 'Machine', 'Warrior',
                'Fiend', 'Beast-Warrior', 'Rock', 'Fairy', 'Dragon', 'Sea Serpent', 'Plant', 
                'Cyberse', 'Zombie', 'Wyrm', 'Winged Beast', 'Reptile', 'Psychic', 'Pyro', 'Dinosaur',
                'Thunder', 'Creator-God', 'Divine-Beast']
        monster = Monster.objects.get(pk=id)
        list_of_all_results = list()
        
        matches = [race for race in races if race in getattr(monster, 'c_description')]
    
        for match in matches:
            list_of_monsters_with_race = Monster.objects.filter(c_race = match)
            list_of_all_results.append(list_of_monsters_with_race)

        return list_of_all_results


    def descriptionLevelSpecHigher(description):
        regExForHigherLevel = 'Level ([1-9]|1[0-3]) or higher'
        matchForHigherLvl = re.search(regExForHigherLevel, description)
        if matchForHigherLvl:
            lvlconstraint = Knowledge.getLvlConstraint(re.Match.group(matchForHigherLvl))
            return Monster.objects.filter(c_level__gte = int(lvlconstraint))
        else:
            'None'


    def descriptionLevelSpecExact(description):
        regExForExactLevel = 'Level ([1-9]|1[0-3]) (?!or)'
        matchForExactLvl = re.search(regExForExactLevel, description)
        if matchForExactLvl:
            lvlconstraint = Knowledge.getLvlConstraint(re.Match.group(matchForExactLvl))
            return Monster.objects.filter(c_level__lte = int(lvlconstraint))
        else:
            'None'


    def descriptionLevelSpecLower(description):
        regExForLowerLevel = 'Level ([1-9]|1[0-3]) or lower'
        matchForLowerLvl = re.search(regExForLowerLevel, description)
        if matchForLowerLvl:
            lvlconstraint = Knowledge.getLvlConstraint(re.Match.group(matchForLowerLvl))
            return Monster.objects.filter(c_level__lte = int(lvlconstraint))
        else:
            'None'
    

    def getLvlConstraint(match):
        lvlReg = '([1-9]|1[0-3])'
        matchStr = str(match)
        matchLvl = re.search(lvlReg, matchStr)
        if matchLvl:
            return re.Match.group(matchLvl)
        else:
            return 'None'
        