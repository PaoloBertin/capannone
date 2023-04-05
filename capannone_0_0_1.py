"""
    file: capannone_0_0_1.py
    
    Descrizione:    Costruzione di un capannone
                    Pilatri e piastre solaio realizzati con ogetti 
    
"""


import FreeCAD as App
import FreeCAD, Draft, Arch
import ArchPrecast
from ColumnReinforcement import SingleTie


FreeCAD.ActiveDocument.Label='capannone_0_0_1'


App.setLogLevel('capannone_0_0_1', 'Trace')
#App.setLogLevel('capannone_0_0_1', 'Log')
#App.setLogLevel('capannone_0_0_1', 'Message')
log=App.Logger('capannone_0_0_1')


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
    log.trace('traslazione(' + str(traslazione) + str('\n'))
    # pilastro=Part.makeBox(lunghezza, larghezza, altezza, traslazione, asseRotazione)
    pilastro = ArchPrecast.makePrecast(slabtype="Champagne",
                                       chamfer=0.0,
                                       dentlength=4e+16,
                                       dentwidth=0.0,
                                       dentheight=4e+16,
                                       base=0.0,
                                       holenumber=0,
                                       holemajor=0.0,
                                       holeminor=0.0,
                                       holespacing=0.0,
                                       groovenumber=0,
                                       groovedepth=50.0,
                                       grooveheight=50.0,
                                       groovespacing=50.0,
                                       risernumber=0,
                                       downlength=0.0,
                                       riser=0.0,
                                       tread=0.0,
                                       dents=[],
                                       precasttype="Pillar",
                                       length=500.0,
                                       width=500.0,
                                       height=5000.0,)
    pilastro.Placement.Base = FreeCAD.Vector(0, 0, 0)
                            # FreeCAD.Vector(7750.0, -250.0, 0.0)
    pilastro.Placement.Rotation = pilastro.Placement.Rotation.multiply(FreeCAD.DraftWorkingPlane.getRotation().Rotation)
    Draft.autogroup(pilastro)    

    # visualizza pilastro
    #Part.show(pilastro)
    
    
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
#    for i in range(m):
#        for j in range(n):
#            for k in range(o):
#                makePiastraSolaio(i, j, k)


campateX=1
campateY=1
piani=1
capannone = makeCapannone(campateX, campateY, piani)


# visualizzazione
Gui.SendMsgToActiveView("ViewFit")                  # visualizza l'intero edificio
Gui.activeDocument().activeView().viewIsometric()   # visualizazione isometrica
