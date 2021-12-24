from src.weapons import revolver, assaultrifle, goldenrevolver, sniperrifle, shotgun, rocketlauncher


GRAVITY = 100

SPAWN_RATE = 0
SPAWN_HEIGHT = 50

WEAPON_PICKUPS = (
    (revolver.WEAPON, revolver.WEAPON_SPAWN_RATE),
    (sniperrifle.WEAPON, sniperrifle.WEAPON_SPAWN_RATE),
    (assaultrifle.WEAPON, assaultrifle.WEAPON_SPAWN_RATE),
    (goldenrevolver.WEAPON, goldenrevolver.WEAPON_SPAWN_RATE),
    (shotgun.WEAPON, shotgun.WEAPON_SPAWN_RATE),
    (rocketlauncher.WEAPON, rocketlauncher.WEAPON_SPAWN_RATE),
)

LIFETIME = 20
FLICKER_START = 5
FLICKER_INTERVAL = 0.5