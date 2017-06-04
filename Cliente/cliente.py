#! /usr/bin/env python
# -*- coding: utf-8 -*-

import socket # Libreria que nos permite trabajar con sockets
#Importamos las librerias para trabajar con forms
import wx
import wx.xrc
#Importamos el diseño del formulario Cliente
import form_cliente
bufzis = 1024 # Establecemos el tamaño en byte que podemos recibir
class Cliente(form_cliente.Cliente):
    def __init__(self, parent):
        form_cliente.Cliente.__init__(self, parent)

        # Desactivamos botones
        self.btnLs.Disable()
        self.btnRepo.Disable()
        self.btnParticiones.Disable()
        self.btnEjecutar.Disable()
        self.txtComando.Disable()
        # self.txtConsola.Disable()

    #Establecemos la conexion con el Servidor
    def Conectar( self, event ):
        try:
            self.ip=str(self.txtIpServer.GetValue())  # Ingresamos la ip del server
            self.port = 2525  # Definimos un puerto 8080 es muy comun
            self.client = socket.socket()  # creamos nuestro objeto socket
            self.client.connect((self.ip, self.port))  # Establecemos la conexion con el server
            # Si se logro conextar el server nos enviara una respuesta
            respuesta = self.client.recv(bufzis)  # Recivimos la respuesta del server
            print respuesta
            # Mostramos un mensaje de dialogo indicando que se establecio la conexion
            dialogo=wx.MessageDialog(None, 'Conexion Establecida', 'Conexion con el Servidor', wx.OK | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
            # Activamos los botones
            self.btnLs.Enable()
            self.btnRepo.Enable()
            self.btnParticiones.Enable()
            self.btnEjecutar.Enable()
            self.txtComando.Enable()

            # Desactivamos elementos
            self.txtIpServer.Disable()
            self.btnConectar.Disable()
        except:
            # en caso de que la conexion falle
            print "Error al conectarse"
            # Mostramos un mensaje de dialogo indicando que hubo un error
            dialogo=wx.MessageDialog(None, 'Error al conectarse', 'Conexion con el Servidor', wx.OK | wx.ICON_ERROR)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()

    def Listar(self, event):
        comando = "ls -l"
        try:
            self.client.send(comando)
            respuesta = self.client.recv(bufzis)
            self.txtConsola.SetValue("")  #Limpiamos la consola
            self.txtConsola.SetValue(respuesta)
        except Exception as e:
            dialogo=wx.MessageDialog(None, 'Error al ejecutar', 'No se pudo ejecutar el comando', wx.OK | wx.ICON_ERROR)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
    def Repositorios(self, event):
        comando = "repo"
        try:
            self.client.send(comando)
            dialogo=wx.MessageDialog(None, 'Se accedio a los repositorios con gedit', 'Comando ejecutado con exito', wx.OK | wx.ICON_INFORMATION)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
        except Exception as e:
            dialogo=wx.MessageDialog(None, 'No se pudo ejecutar el comando' ,'Error al ejecutar', wx.OK | wx.ICON_ERROR)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()

    def Particiones(self, event):
        comando = "df -h"
        try:
            self.client.send(comando)
            respuesta = self.client.recv(bufzis)
            self.txtConsola.SetValue("")
            self.txtConsola.SetValue(respuesta)
        except Exception as e:
            dialogo=wx.MessageDialog(None, 'No se pudo ejecutar el comando' ,'Error al ejecutar' , wx.OK | wx.ICON_ERROR)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()

    def Ejecutar(self, event):
        comando = self.txtComando.GetValue()
        if comando == "":
            dialogo=wx.MessageDialog(None, 'Ingrese un comando', 'Error' , wx.OK | wx.ICON_ERROR)
            respuesta = dialogo.ShowModal()
            dialogo.Destroy()
        else:
            try:
                self.client.send(comando)
                respuesta = self.client.recv(bufzis)
                self.txtConsola.SetValue("")
                self.txtConsola.SetValue(respuesta)
            except Exception as e:
                dialogo=wx.MessageDialog(None, 'No se pudo ejecutar el comando' ,'Error al ejecutar' , wx.OK | wx.ICON_ERROR)
                respuesta = dialogo.ShowModal()
                dialogo.Destroy()


#Instanciamos el formulario Principal
class MyApp(wx.App):
    def OnInit(self):
        frame1 = Cliente(None)
        self.SetTopWindow(frame1)
        frame1.Show()
        return 1

# end of class MyApp
if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
