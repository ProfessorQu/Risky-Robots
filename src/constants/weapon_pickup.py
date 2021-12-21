from src.weapons import revolver, assaultrifle, goldenrevolver, sniperrifle, shotgun, rocketlauncher


GRAVITY = 100

SPAWN_RATE = 5

WEAPON_PICKUPS = (
    (revolver.WEAPON, revolver.WEAPON_SPAWN_RATE),
    (sniperrifle.WEAPON, sniperrifle.WEAPON_SPAWN_RATE),
    (assaultrifle.WEAPON, assaultrifle.WEAPON_SPAWN_RATE),
    (goldenrevolver.WEAPON, goldenrevolver.WEAPON_SPAWN_RATE),
    (shotgun.WEAPON, shotgun.WEAPON_SPAWN_RATE),
    (rocketlauncher.WEAPON, rocketlauncher.WEAPON_SPAWN_RATE),
)