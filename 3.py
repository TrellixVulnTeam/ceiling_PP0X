currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_8/models/neighborhoods/daisys_garden.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
tunnelA = loader.loadModel('phase_6/models/cogHQ/Cog_Tunnel.bam')
tunnelA.reparentTo(currentLand.currentLandModels[zones[zID]])
tunnelA.setPos(0, 0, 0.025)
base.localAvatar.setPos(22.9513,60.1588,0.025)

G = get_builtins()
LoadingZone = G["LoadingZone"]
LoadingZone.define(3.6083, -1.4502, -14.5347, 9.84779, 5)
