currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_6/models/neighborhoods/minnies_melody_land.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
# Note for further creation: reparent everything after mainland to currentLand.currentLandModels[zones[zID]]
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)

# note: normally one would use "awaitForZoneThread()" before each loading zone, but this isn't quite defined yet
# until we actually make a loadingzone.
global isCurrentZone
isCurrentZone = True

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/WW_nbrhood.ogg')
G["music"].setLoop(True)
G["music"].play()
