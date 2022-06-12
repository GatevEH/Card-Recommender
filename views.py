from django.shortcuts import render

from .models import Monster
from .utils import Knowledge

def index(request):
    list_of_monsters = Monster.objects.order_by('id')
    return render(request, 'cardsRecommender/index.html', {'listOfMonsters': list_of_monsters})

def card(request, id):
    monster = Monster.objects.get(pk=id)
    
    listExactLvl = list()
    listHigherLvl = list()
    listLowerLvl = list()

    listFinRaces = list()
    listFinAttr = list()
    listFin = list()
    
    listFinAttr = Knowledge.descriptionContainsAttribute(id)    
    for l in listFinAttr:
        listFin = listFin + list(l)

    listFinRaces = Knowledge.descriptionContainsRace(id)
    for l in listFinRaces:
        if l not in listFin:
            listFin = listFin + list(l)
    
    exactLvl = Knowledge.descriptionLevelSpecExact(getattr(monster, 'c_description'))
    higherLvl = Knowledge.descriptionLevelSpecHigher(getattr(monster, 'c_description'))
    lowerLvl = Knowledge.descriptionLevelSpecLower(getattr(monster, 'c_description'))
    
    if higherLvl:
        theHigherLvl = Knowledge.getLvlConstraint(higherLvl)
        listHigherLvl = Monster.objects.filter(c_level__gte = int(theHigherLvl))
    else:
        theHigherLvl = 'None'
        listHigherLvl = ''

    if lowerLvl:
        theLowerLvl = Knowledge.getLvlConstraint(lowerLvl)
        listLowerLvl = Monster.objects.filter(c_level__lte = int(theLowerLvl))
    else:
        theLowerLvl = 'None'
        listLowerLvl = ''

    if exactLvl:
        theExactLvl = Knowledge.getLvlConstraint(exactLvl)
        listExactLvl = Monster.objects.filter(c_level = int(theExactLvl))
    else:
        theExactLvl = 'None'
        listExactLvl = ''

    listFin = listFin + list(listHigherLvl)
    listFin = listFin + list(listLowerLvl)
    listFin = listFin + list(listExactLvl)
    
    return render(request, 
                    'cardsRecommender/card.html', 
                    {'monster': monster, 
                    'recommendedMonsters': set(listFin)
                    })