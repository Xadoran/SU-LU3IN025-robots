# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Doruk OZGENC
#  Prénom Nom: Can GENIS
import time
import asyncio
import random 

def get_team_name():
    return "BordoBereliler" # à compléter (comme vous voulez)
    
async def uTurn():
    rotation = 0.4
    translation = 1
    await asyncio.sleep(3)
    
def wall_in_front(sensors):
    return sensors["sensor_front"]["distance"] < 1 and sensors["sensor_front"]["isRobot"] == False

def wall_on_left(sensors):
    return sensors["sensor_left"]["distance"] < 1 and sensors["sensor_left"]["isRobot"] == False
    
def wall_on_right(sensors):
    return sensors["sensor_right"]["distance"] < 1 and sensors["sensor_right"]["isRobot"] == False
    
def wall_on_frontLeft(sensors):
    return sensors["sensor_front_left"]["distance"] < 1 and sensors["sensor_front_left"]["isRobot"] == False
    
def wall_on_frontRight(sensors):
    return sensors["sensor_front_right"]["distance"] < 1 and sensors["sensor_front_right"]["isRobot"] == False
    
def wall_on_backRight(sensors):
    return sensors["sensor_back_right"]["distance"] < 1 and sensors["sensor_back_right"]["isRobot"] == False

def wall_on_backLeft(sensors):
    return sensors["sensor_back_left"]["distance"] < 1 and sensors["sensor_back_left"]["isRobot"] == False
    
def wall_on_back(sensors):
    return sensors["sensor_back"]["distance"] < 1 and sensors["sensor_back"]["isRobot"] == False
    
def enemy_is_chasing(sensors):
    if sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
        return True
        
def following_friend(sensors):
    if (sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True):
        return True
        
def following_friend_left(sensors):
    if (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True):
        return True
        
def following_friend_right(sensors):
    if (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == True):
        return True
        
def friend_on_left(sensors):
    if (sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == True):
        return True

def friend_on_right(sensors):
    if (sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == True):
        return True

def chasing_enemy(sensors):
    if (sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False):
        return True
        
def chasing_enemy_left(sensors):
    if (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False):
        return True

def chasing_enemy_right(sensors):
    if (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False):
        return True
        
def obstacle_in_front(sensors):
    return sensors["sensor_front"]["distance"] < 1 

def obstacle_in_front_left(sensors):
    return sensors["sensor_front_left"]["distance"] < 1 
    
def obstacle_in_front_right(sensors):
    return sensors["sensor_front_right"]["distance"] < 1
        
"""def spiderman(sensors):
    if sensors["sensor_front"]["distance"] < 1 and sensors["sensor_right"]["distance"] < 1 and sensors["sensor_front"]["isRobot"] == False and sensors["sensor_right"]["isRobot"] == False:
        translation = -1 * sensors["sensor_front"]["distance"]
    elif sensors["sensor_front"]["distance"] < 1 and sensors["sensor_left"]["distance"] < 1 and sensors["sensor_front"]["isRobot"] == False and sensors["sensor_left"]["isRobot"] == False:
        translation = 1 * sensors["sensor_front"]["distance"]"""
        
# Returns true if a robot should stick to walls
def isSpiderman(robotId):
    return (robotId == 0)  
        
# Behaviour of a spiderman 
def do_spiderman(sensors):
    rotation = 0 
    # Case 1: Wall in front and on right
    if wall_on_right(sensors) and wall_in_front(sensors):
        rotation = -0.2
    # Case 2: Wall in front and on left
    elif wall_on_left(sensors) and wall_in_front(sensors):
        rotation = 0.2
    # Case 3: Wall on left and behind    
    elif wall_on_backLeft(sensors) and wall_on_left(sensors) and not wall_in_front(sensors) and not wall_on_frontLeft(sensors) and not wall_on_frontRight(sensors) and not wall_on_right(sensors) and not wall_on_backRight(sensors):
        rotation = -0.2
    # Case 4: Wall on right and behind   
    elif not wall_on_backLeft(sensors) and not wall_on_left(sensors) and not wall_in_front(sensors) and not wall_on_frontLeft(sensors) and not wall_on_frontRight(sensors) and wall_on_right(sensors) and wall_on_backRight(sensors):
        rotation = 0.2
    else:
        rotation = idle_behaviour(sensors)
    return rotation

# Returns true if a robot should follow rival robots
def isPolice(robotId):
    return (robotId == 1 or robotId == 6)
    
# Behaviour of a police robot
def doPolice(sensors):
    if chasing_enemy_left(sensors):
        rotation = -0.7
    elif chasing_enemy_right(sensors):
        rotation = 0.7
    else:
        rotation = 0
    return rotation

# Default behaviour of an ordinary robot 
def idle_behaviour(sensors):
    rotation = 0
    
    # If an enemy is chasing, do an evasive manouver
    if enemy_is_chasing(sensors):
        uTurn()
    # If following a friend, get away from it
    elif following_friend(sensors):
        rotation = random.choice([0.8, -0.8])
    elif  following_friend_right(sensors) or friend_on_right(sensors):
        rotation = -0.8
    elif following_friend_left(sensors) or friend_on_left(sensors):
        rotation = 0.8
    # Evade any obstacles unless stated otherwise
    elif sensors["sensor_front"]["distance"] < 1:
        rotation = random.choice([0.5, -0.5])
    elif sensors["sensor_front_left"]["distance"] < 1:
        rotation = 0.6
    elif sensors["sensor_front_right"]["distance"] < 1:
        rotation = -0.45
        
    return rotation


def step(robotId, sensors):
    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)
    
    if isPolice(robotId) and (chasing_enemy_left(sensors) or chasing_enemy(sensors)):
        rotation = doPolice(sensors)
    elif isPolice(robotId) and (chasing_enemy_right(sensors) or chasing_enemy(sensors)):
        rotation = doPolice(sensors)
    elif isSpiderman(robotId):
        rotation = do_spiderman(sensors)
    else:
        rotation = idle_behaviour(sensors)

    return translation, rotation




"""    elif enemy_is_chasing(sensors):
        uTurn()
    elif following_friend(sensors):
        rotation = random.choice([0.8, -0.8])
    elif  following_friend_right(sensors) or friend_on_right(sensors):
        rotation = -0.8
    elif following_friend_left(sensors) or friend_on_left(sensors):
        rotation = 0.8
    elif sensors["sensor_front"]["distance"] < 1 and sensors["sensor_front"]["isRobot"] == False:
        rotation = random.choice([0.5, -0.5])
    elif sensors["sensor_front_left"]["distance"] < 1 and sensors["sensor_front_left"]["isRobot"] == False:
        rotation = 0.5
    elif sensors["sensor_front_right"]["distance"] < 1 and sensors["sensor_front_right"]["isRobot"] == False:
        rotation = -0.5
"""





""" isPolice(robotId) and chasing_enemy_right(sensors):
        rotation = 0.7
    elif (robotId == 0 or robotId == 8):
        spiderman(sensors)
""" 

"""
    else:
    idle_behaviour(sensors, translation, rotation)
"""

   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
