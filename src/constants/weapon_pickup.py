from src.weapons import revolver, sniperrifle, assaultrifle, goldenrevolver


GRAVITY = 100

SPAWN_RATE = 10

WEAPON_PICKUPS = (
    (revolver.WEAPON, revolver.WEAPON_SPAWN_RATE),
    (sniperrifle.WEAPON, sniperrifle.WEAPON_SPAWN_RATE),
    (assaultrifle.WEAPON, assaultrifle.WEAPON_SPAWN_RATE),
    (goldenrevolver.WEAPON, goldenrevolver.WEAPON_SPAWN_RATE)
)