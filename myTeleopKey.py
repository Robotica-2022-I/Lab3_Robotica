#Se importan las librerias
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import argparse
import termios, sys, os
from numpy import pi
TERMIOS = termios

#se crea la funci[on getKey que lee la tecla presionada y devuelve el valor en binario]
def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c
#Se crea la fucion teleport que utiliza el comando teleport absolut para enviar la tortuga
#a la posicion absoluta [0,0,0]
def teleport(x, y,ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
    except rospy.ServiceException as e:
        print(str(e))
#Se crea la fucion teleportr que utiliza el comando teleport absolut para enviar la tortuga
#a la posicion relativa [0,0,180]
def teleportr(ang):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = teleportA(0, ang)
    except rospy.ServiceException as e:
        print(str(e))
#Se crea la fucion pubVel que utiliza la funcion cmd_vel para rotar y trasladar la tortuga
#Le ingresan valores de lineal y angular para determinar la direccion de avance y la direccion de rotacion
def pubVel(lineal,angular):
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('velPub', anonymous=False)
    vel = Twist()
    rate = rospy.Rate(10) 
    vel.linear.x = lineal
    vel.angular.z = angular
    rospy.loginfo(vel)
    pub.publish(vel)
    rate.sleep()
#Se crea la funcion action para coordinar las teclas w, a, s, d, r y espacio para que ejecuten los
#movimientos correspondientes
def action(tecla):
    try:
        if tecla == b'r':
            teleport(5.0,5.5,0)
        if tecla == b' ':
            teleportr(22)
        if tecla == b'w':
            pubVel(1,0)
        if tecla == b's':
            pubVel(-1,0)
        if tecla == b'a':
            pubVel(0,1)
        if tecla == b'd':
            pubVel(0,-1)
    except rospy.ROSInterruptException:
        pass
#Se crea el main y el comando getkey se pone en un bucle para que mantenga leyendo las entradas
#Si se desea salir y acabar el programa se presiona la letra 'p'
if __name__ == "__main__":
    i = True
    while i:
        key = getkey()
        print(str(key))
        action(key)
        if key == b'p':
            i = False