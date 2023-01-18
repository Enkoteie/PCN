#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Envoi de données vers l'Arduino (série)
'''
import time
import serial
import serial.tools.list_ports

print("Recherche d'un port serie...")

ports = serial.tools.list_ports.comports(include_links=False)

if (len(ports) != 0): # on a trouvé au moins un port actif

    if (len(ports) > 1):     # affichage du nombre de ports trouvés
        print (str(len(ports)) + " ports actifs ont ete trouves:") 
    else:
        print ("1 port actif a ete trouve:")

    ligne = 1

    for port in ports :  # affichage du nom de chaque port
        print(str(ligne) + ' : ' + port.device)
        ligne = ligne + 1

    portChoisi = input('Ecrivez le numero du port desire:')

    print('1: 9600   2: 38400    3: 115200')

    baud = input('3')

    if (baud == 1):
        baud = 9600
    if (baud == 2):
        baud = 38400
    if (baud == 3):
        baud = 115200

    # on établit la communication série
    arduino = serial.Serial(ports[portChoisi - 1].device, baud, timeout=1)
    
    print('Connexion a ' + arduino.name + ' a un baud rate de ' + str(baud))
   
    while True:
        message = input('G01 A000 B090 C090 D090 E090 F010')
        message2 = input('G01 A000 B090 C090 D090 E090 F073')
        arduino.write(str(message))   # envoi du message série
        time.sleep(3)
        
else: # on n'a pas trouvé de port actif
    print("Aucun port actif n'a ete trouve")