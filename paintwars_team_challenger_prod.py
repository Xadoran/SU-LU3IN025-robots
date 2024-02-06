# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: _________
#  Prénom Nom: _________
import time
import asyncio
import random 

def get_team_name():
    return "AnneSevenler" # à compléter (comme vous voulez)
    
async def uTurn():
    rotation = 0.4
    translation = 1
    await asyncio.sleep(3)
    
def enemy_is_chasing(sensors):
    if sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
        return True
        
def following_friend(sensors):
    if (sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True):
        return True
        
def following_friend_left(sensors):
    if (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True):
        return True
        
def friend_on_left(sensors):
    if (sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == True):
        return True

def friend_on_right(sensors):
    if (sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == True):
        return True

def following_friend_right(sensors):
    if (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == True):
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
        
def spiderman(sensors):
    if (sensors["sensor_front"]["distance_to_wall"] < 1 and sensors["sensor_right"]["distance_to_wall"] < 1):
        translation = -1 * sensors["sensor_front"]["distance_to_wall"]
    elif (sensors["sensor_front"]["distance_to_wall"] < 1 and sensors["sensor_left"]["distance_to_wall"] < 1):
        translation = 1 * sensors["sensor_front"]["distance_to_wall"]

def thePolice(sensors):
    if (chasing_enemy(sensors)):
        translation = 1
        rotation = 0 
    elif (chasing_enemy_left):
        translation = 1
        rotation = -1
    elif chasing_enemy(sensors):
        translation = 1
        rotation = 1  

def step(robotId, sensors):

    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)
    
    if enemy_is_chasing(sensors):
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

    return translation, rotation
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
