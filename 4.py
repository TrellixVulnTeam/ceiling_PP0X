currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_6/models/karting/RT_SpeedwayA.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(196,322.864,0)