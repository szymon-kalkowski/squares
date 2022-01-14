import pytest,pygame
from operator import itemgetter

#functions
def copy(list):
    copy=[]
    for i in list:
        copy.append(i)
    return copy

def bubble_sort(list,dkey):
    sorted_list=copy(list)
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list)-i-1):
            if sorted_list[j+1][dkey]<sorted_list[j][dkey]:
                sorted_list[j], sorted_list[j+1]=sorted_list[j+1], sorted_list[j]
    return sorted_list

def sort_list(list,dkey):
    sorted_list=copy(list)
    sorted_list=sorted(sorted_list, key=itemgetter(dkey))
    return sorted_list

def list_reverse(list):
    reversed_list=[]
    for i in range(len(list)):
        reversed_list.append(list[len(list)-i-1])
    return reversed_list

def reverse(list):
    reversed_list=copy(list)
    reversed_list.reverse()
    return reversed_list

def centerX(object, x):
    cx=x+object.get_width()/2
    return cx

def centerY(object, y):
    cy=y+object.get_height()/2
    return cy

def collision(objIMG,objX,objY,i,playerIMG,playerX,playerY):
    if abs(centerX(objIMG[i],objX[i])-centerX(playerIMG,playerX))<5 and abs(centerY(objIMG[i],objY[i])-centerY(playerIMG,playerY))<5:
        return True
    else:
        return False

#test variables
playerIMG=pygame.image.load('pictures/b.png')
playerIMG=pygame.transform.scale(playerIMG, (50, 50))
playerX=100
playerY=200

object1=pygame.image.load('pictures/a.png')
object1=pygame.transform.scale(object1, (50, 50))

object2=pygame.image.load('pictures/c.png')
object2=pygame.transform.scale(object2, (50, 50))

objectIMG=[object1,object2]
objectX=[350,100]
objectY=[200,200]

list1=[6,3,4,2,1,8,7]

list2=[{"nick":"Simon","score":23,"time":13.41},
{"nick":"Mathews","score":213,"time":25.11},
{"nick":"Dominic","score":123,"time":10.47}]

#tests
def test_bubble_sort():
    assert bubble_sort(list2,"score")==sort_list(list2,"score")

def test_list_reverse():
    assert list_reverse(list1)==reverse(list1)

def test_centerX():
    assert centerX(object1,20)==45

def test_centerY():
    assert centerY(object1,10)==35

def test_collision():
    assert collision(objectIMG,objectX,objectY,0,playerIMG,playerX,playerY)==False
    assert collision(objectIMG,objectX,objectY,1,playerIMG,playerX,playerY)==True


