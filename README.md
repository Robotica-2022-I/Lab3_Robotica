# Lab3_Robotica
Descripción del desarrollo del laboratorio 3 de robótica "Robótica de Desarrollo, Intro a ROS"


Daniel Felipe Cantor Santana

Juan David Morales Restrepo

David Leonardo Cocoma Reyes 


# 1)Requisitos
Para el desarrollo de esta práctica fue necesario realizarlo en Ubuntu, ya que tanto ROS, como el ejercicio "Hello_turtle" solo estan disponibles para linux.


# 2)Ejercicio
La idea de este laboratorio es crear nuestro propio script, llamado "myTeleopKey.py" y que en este se definarán las siguientes instrucciones:

- El movimiento de la tortuga debe ser con las teclas W,A,S,D. 
- Debe retornar a su posición y orientación centrales con la tecla R
- Debe dar un giro de 180° con la tecla ESPACIO


# 3) Desarrollo laboratorio
  - El laboratorio se realizó en Python 3, empleando las mismas funciones que se presentan en el archivo "TeleopKey", las cuales definen la velocidad, y asocian el valor de las teclas al movimiento. El código realizado se encuentra en el archivo adjunto "myTeleopKey.py"
  
  - El video del funcionamiento del laboratorio se presenta a continuación:
  
    [![Alt text](https://img.youtube.com/vi/2K-DCGj8uyk/0.jpg)](https://www.youtube.com/watch?v=2K-DCGj8uyk)

# 4) Análisis
  Se evidencia como este ejercicio es un "hola mundo" para dar una idea de cómo funciona linux y cómo trabaja el sistema de ROS siendo capaz de realizar conecciones entre distintas aplicaciones, scripts, y sistemas por medio de nodos y registros de manera fácil y rápida por medio de las terminales en Linux.
  
  
# 5) Conclusiones

  - El framework ROS es de suma importancia para la robótica de desarrollo, ya que facilita la implementación de instrucciones a un sistema.
  
  - Facilita la comunicación entre diversos sistemas por medio de ROS y los servidores generados por este, de manera que no se necesita realizar una implementación nativa de las instrucciones gracias a que permite modificar en tiempo real por medio de distintos scripts sin importar el lenguaje.
