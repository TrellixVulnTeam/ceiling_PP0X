currentLand.currentLandModels[zones[zID]] = loader.loadModel('phase_6/models/karting/RT_SpeedwayA.bam')
currentLand.currentLandModels[zones[zID]].reparentTo(render)
currentLand.currentLandModels[zones[zID]].setPos(0, 0, 0)
base.localAvatar.setPos(196,322.864,0)

G["music"].stop()
G["music"] = loader.loadSfx('phase_6/audio/bgm/GS_Race_BKR.ogg')
G["music"].setLoop(True)
G["music"].play()


async def heavyWeight():
    print("loading...")
    weight = loader.loadModel('phase_6/models/karting/Kart3_Final.bam')
    weight.reparentTo(render)
    goofball = loader.loadModel('phase_6/models/char/TT_G-500.bam')
    goofball.reparentTo(render)
    goofball.setPos(225,420.864,0)
    goofball.setScale(32)
    x = 196
    z = 318
    y0 = 666
    y1 = -530
    maxSize = 125
    currentY = y0
    currentSize = 1
    import time
    while (currentY > y1):
        print("!!!ERROR LOADING KART(S)!!!")
        currentSize = currentSize + 1
        currentY = currentY - .69
        weight.setScale(currentSize)
        weight.setPos(x, z, currentY)
        time.sleep(.001)
    time.sleep(.1)
    currentY = y0
    currentSize = 1
    weight.removeNode()
    goofball.removeNode()
    loadZone(1)


asyncio.run(heavyWeight())