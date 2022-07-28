currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_6/models/karting/RT_SpeedwayA.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(196,322.864,0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GS_Race_RR.ogg')
G["music"].setLoop(True)
G["music"].play()
