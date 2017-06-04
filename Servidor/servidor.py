#! /usr/bin/env python
# -*- coding: utf-8 -*-

#Importamos las librerias para trabajar con forms
import wx
import wx.xrc

import socket
import sys
from subprocess import *
import threading
#Importamos el diseño del formulario Servidor
import form_servidor

import funciones_servidor

buszis = 1024
class Servidor(form_servidor.Servidor, funciones_servidor.FuncionesServidor):
    def __init__(self, parent):
        form_servidor.Servidor.__init__(self, parent)
        #Establecemos el proseso escuchar que estara a la espera de establecer conexion
        self.thread_escuchar = threading.Thread(target=self.escuchar)
        # Evita que el trhead se siga ejecutando al cerrar el programa
        self.thread_escuchar.setDaemon(True)
        #Iniciamos el proceso escuchar
        self.thread_escuchar.start()
        miIP = "Esperando conexion IP SERVIDOR " + (self.obtener_ip())
        self.lblCliente.SetLabel(miIP)
        # self.txtResultado.Disable()

    def mostrar_cliente(self, text):
        wx.CallAfter(self.lblCliente.SetLabel, text)

    def actualizar_text(self, text):
        wx.CallAfter(self.txtResultado.AppendText, text)

    def escuchar(self):

        try:
            while True:
                self.s = socket.socket()  # Creamos nuestro objeto socket
                self.port = 2525  #Establecemos el puerto por el cual nos conectaremos
                self.miIP = self.obtener_ip()  #Obtenemos la direccion IP
                self.direccion = (self.miIP, self.port)

                self.s.bind(('', self.port)) #Enlacamos el socket

                self.s.listen(5)  # Esperamos la conexion del cliente
                self.cliente, addr = self.s.accept()     # Establece  la conexion del cliente
                print addr
                addr = "Conectado desde: " + str(format(addr))
                self.mostrar_cliente(addr)
                mensaje = "Conexion establecida"
                self.cliente.send(mensaje)  # Envia un mensaje al cliente
                while True:
                    comando = self.cliente.recv(buszis)
                    if not comando:
                        break

                    if comando == "ls -l":
                        wx.CallAfter(self.txtResultado.SetValue, "") # Limpiamos la caja de texto
                        ls = self.listar()
                        respuesta = " "
                        for elemento in ls:
                            self.actualizar_text(format(elemento))
                            respuesta += str(elemento)
                        self.cliente.send(respuesta)

                    if comando == "repo":
                        rp = self.repositorio()
                        comando == ""

                    if comando == "df -h":
                        wx.CallAfter(self.txtResultado.SetValue, "") # Limpiamos la caja de texto
                        pt = self.particiones()
                        respuesta = " "
                        for elemento in pt:
                            self.actualizar_text(format(elemento))
                            respuesta += str(elemento)
                        self.cliente.send(respuesta)

                    if comando != "ls -l" and comando != "df -h" and comando != "repo":
                        wx.CallAfter(self.txtResultado.SetValue, "" )
                        cmd = self.ejecutar_comando(comando)
                        respuesta = " "
                        for elemento in cmd:
                            self.actualizar_text(format(elemento))
                            respuesta += str(elemento)
                        self.cliente.send(respuesta)
                self.cliente.close()  # Cierra la conexion
        except KeyboardInterrupt:
            self.s.close()
            self.thread_escuchar.exit()

    def __del__(self):
        self.s.close()
        self.Close()


#Instanciamos el formulario Principal
class MyApp(wx.App):
    def OnInit(self):
        frame1 = Servidor(None)
        self.SetTopWindow(frame1)
        frame1.Show()
        return 1
# end of class MyApp
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()

# app = wx.App(False)
# win = Servidor(None)
# app.MainLoop()
