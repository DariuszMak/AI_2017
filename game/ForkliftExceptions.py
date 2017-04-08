class ForkliftOutOfGridError(Exception):
    pass

class ForkliftMovedForwardWithPackageOnLoweredFork(Exception):
    pass

class ForkliftNotOnPackagePosition(Exception):
    pass

class ForkliftAlreadyCarryingPackage(Exception):
    pass

class ForkliftNotCarryingPackage(Exception):
    pass

class ForkliftTurningWithLoweredPackage(Exception):
    pass

class ForkliftMovingOnPackagePosAlreadyCarryingPackage(Exception):
    pass

class ForkliftMovedBackwardIntoPackage(Exception):
    pass
