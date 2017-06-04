#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import socket # Libreria que nos permite trabajar con sockets

#Importamos las librerias para trabajar con forms
import wx
import wx.xrc
import sys  # Libreria que nos permite ejecutar comandos de sistema
from subprocess import * # Libreria para usar Popen
class FuncionesServidor():

    #Optenemos la direccion ip de la maquina mediante Popen
    def obtener_ip(self):
        self.comando='hostname -I'  #Almacenamos el comando
        result = Popen(self.comando, shell=True, stdout=PIPE)
        for i in result.stdout:
            miIP=i.decode(sys.getdefaultencoding()).rstrip()
        if (miIP==""):
            miIP='localhost'
        return miIP

    def listar(self):
        self.comando='ls -l'  #Almacenamos el comando
        # Ejecutamos el comando con popen
        result = Popen(self.comando, shell=True, stdout=PIPE)
        return result.communicate() # Convierte el resultado de Popen a una tupla

    def repositorio(self):
        self.comando = "gedit /etc/apt/sources.list"
        result = Popen(self.comando, shell=True, stdout=PIPE)
        return result

    def particiones(self):
        self.comando = "df -h"
        result = Popen(self.comando, shell=True, stdout=PIPE)
        return result.communicate()

    def ejecutar_comando(self, comando):
        try:
            result = Popen(comando, shell=True, stdout=PIPE)
            return result.communicate()
        except Exception as e:
            return "Error!! este comando no es compatible :( "
