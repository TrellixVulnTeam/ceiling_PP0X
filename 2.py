currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_6/models/neighborhoods/donalds_dock.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(0,0,0)