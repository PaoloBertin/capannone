"""
    file: capannone.py
    
    Descrizione:    Costruzione di un capannone
                    Pilatri e piastre solaio realizzati con oggetti Part
    
"""

import FreeCAD as App
import Part

FreeCAD.ActiveDocument.Label='capannone'

App.setLogLevel('capannone', 'Trace')
#App.setLogLevel('capannone', 'Log')
#App.setLogLevel('capannone', 'Message')
log=App.Logger('capannone')


objects=App.ActiveDocument.Objects
for object in objects:
    App.ActiveDocument.removeObject(object.Name)


# pilastro
lunghezza=500.0    # lunghezza pilastro
larghezza=500.0    # larghezza pilastro
altezza=4000.0     # altezza pilastro


# solaio
campataX=8000.0    # distanza lungo X fra pilastri
campataY=8000.0    # distanza lungo y fra pilastri
spessore=500.0     # spessore solaio


def makePilastro(i, j, k):
    """ Costruzione pilastro """

    log.info('--- costruzione pilastro(' + str(i) + str(j) + str(k) + ')' + ' ---')

    traslazione=App.Vector(campataX*i, campataY*j, (altezza + spessore)*k)
    asseRotazione=App.Vector(0, 0, 1)
    pilastro=Part.makeBox(lunghezza, larghezza, altezza, traslazione, asseRotazione)
    log.trace('traslazione(' + str(traslazione) + str('\n'))
    
    # visualizza pilastro
    Part.show(pilastro)
    
    
def makePiastraSolaio(i, j, k):
    """ Costruzione piastra solaio """
    
    traslazione=App.Vector(campataX*i + lunghezza/2.0, campataY*j + larghezza/2.0, k*(altezza + spessore) + altezza)
    asseRotazione=App.Vector(0, 0, 1)
    solaio=Part.makeBox(campataX, campataY, spessore, traslazione, asseRotazione)    
    # visualizza solaio
    Part.show(solaio)    
        

def makeCapannone(m=2, n=2, o=1):
    """Controllo costruzione capannone """
    
    # pilastri
    for i in range(m+1):
        for j in range(n+1):
            for k in range(o):
                makePilastro(i, j, k)
    
       
    # piastre solaio
    for i in range(m):
        for j in range(n):
            for k in range(o):
                makePiastraSolaio(i, j, k)


campateX=5
campateY=5
piani=30
capannone = makeCapannone(campateX, campateY, piani)


# visualizzazione
Gui.SendMsgToActiveView("ViewFit")                  # visualizza l'intero edificio
Gui.activeDocument().activeView().viewIsometric()   # visualizazione isometrica
