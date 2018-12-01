# Tareas
En este taller hemos hecho:

## 1. RPI pinout
![Raspberry PI PinOut MAP](https://github.com/Makespace-Mallorca/taller_sensores/blob/master/raspberrypi/rp2_pinout.png?raw=true)

## 2. Configurar el sistema operativo Raspbian
1. Descargar la imagen .imo del SO:
https://www.raspberrypi.org/downloads/raspbian/
2. Generar la tarjetas SSD. Instrucciones en:
https://www.raspberrypi.org/documentation/installation/installing-images/README.md
Ejemplo en Mac:
```
diskutil list
diskutil unmountDisk /dev/disk<disk# from diskutil>
sudo dd bs=1m if=image.img of=/dev/rdisk<disk# from diskutil> conv=sync
```
3. Actualizar el SO Raspbian:
```
sudo apt-get update
sudo apt-get dist-upgrade
```

## 3. Conectar el sensor DHT11
![Raspberry PI PinOut MAP](https://github.com/Makespace-Mallorca/taller_sensores/blob/master/raspberrypi/DHT11-Pinout-for-three-pin-and-four-pin-types-2-1024x742.jpg?raw=true)
![Raspberry PI PinOut MAP](https://github.com/Makespace-Mallorca/taller_sensores/blob/master/raspberrypi/How-to-Setup-the-DHT11-on-the-Raspberry-Pi-Three-pin-DHT11-Wiring-Diagram-768x359.png?raw=true)

## 4. Cargar los programas

## 5. Actualizar la librerias

## 6. Darse de alta en Thigspeak
https://thingspeak.com
Actualizar la APIKEY de escritura y la URL del endopoint de los campos de datos.

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

