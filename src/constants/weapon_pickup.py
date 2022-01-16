from src.weapons import revolver, assaultrifle, goldenrevolver, sniperrifle, shotgun, rocketlauncher


GRAVITY = 100

SPAWN_RATE = 3
SPAWN_HEIGHT = 50

WEAPON_PICKUPS = (
    (revolver.WEAPON,       0),
    (sniperrifle.WEAPON,    1),
    (assaultrifle.WEAPON,   1),
    (goldenrevolver.WEAPON, 0.05),
    (shotgun.WEAPON,        1),
    (rocketlauncher.WEAPON, 0.25),
)

LIFETIME = 20
FLICKER_START = 5
FLICKER_INTERVAL = 0.5