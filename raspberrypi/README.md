# Tareas
En este taller hemos hecho:

## 1. RPI pinout

## 2. Configurar el sistema operativo Raspbian

## Arrancar el servidor Node-red
Siguiendo instrcciones de https://nodered.org/docs/hardware/raspberrypi:
* Por el escritorio: Menu -> Programming -> Node-RED.
* Por la línea de comandos (SSH) ejecutar:
```
run node-red-start
```
Si quieres que Node-RED arranque cada vez que enciendes la RPi ejecutar el commando:
```
sudo systemctl enable nodered.service  
```

