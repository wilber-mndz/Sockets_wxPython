# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Cliente
###########################################################################

class Cliente ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Comandos de Sistema - cliente ", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.Size( 800,600 ) )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		Conenedor_Principal = wx.FlexGridSizer( 4, 5, 0, 0 )
		Conenedor_Principal.SetFlexibleDirection( wx.BOTH )
		Conenedor_Principal.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		Conenedor_Principal.AddSpacer( ( 40, 60), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"IP del servidor", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetForegroundColour( wx.Colour( 0, 0, 0 ) )
		self.m_staticText4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		Conenedor_Principal.Add( self.m_staticText4, 0, wx.ALL, 10 )

		self.txtIpServer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		Conenedor_Principal.Add( self.txtIpServer, 0, wx.ALL, 5 )

		self.btnConectar = wx.Button( self, wx.ID_ANY, u"Conectar", wx.DefaultPosition, wx.DefaultSize, 0 )
		Conenedor_Principal.Add( self.btnConectar, 0, wx.ALL, 5 )


		Conenedor_Principal.AddSpacer( ( 60, 90), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Conenedor_Principal.AddSpacer( ( 180, 0), 1, wx.EXPAND, 5 )

		self.btnLs = wx.Button( self, wx.ID_ANY, u"Listar directorio", wx.DefaultPosition, wx.DefaultSize, 0 )
		Conenedor_Principal.Add( self.btnLs, 0, wx.ALL, 10 )

		self.btnRepo = wx.Button( self, wx.ID_ANY, u"Abrir repositorios", wx.DefaultPosition, wx.DefaultSize, 0 )
		Conenedor_Principal.Add( self.btnRepo, 0, wx.ALL, 10 )

		self.btnParticiones = wx.Button( self, wx.ID_ANY, u"Mostrar Particiones", wx.DefaultPosition, wx.DefaultSize, 0 )
		Conenedor_Principal.Add( self.btnParticiones, 0, wx.ALL, 10 )


		Conenedor_Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		bSizer1.Add( Conenedor_Principal, 1, wx.EXPAND, 5 )

		Consola = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Consola Remota" ), wx.VERTICAL )

		Consola.SetMinSize( wx.Size( -1,450 ) )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer3.SetMinSize( wx.Size( -1,50 ) )
		self.m_staticText2 = wx.StaticText( Consola.GetStaticBox(), wx.ID_ANY, u"Comando", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		self.m_staticText2.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 10 )

		self.txtComando = wx.TextCtrl( Consola.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtComando.SetMinSize( wx.Size( 200,-1 ) )

		bSizer3.Add( self.txtComando, 0, wx.ALL, 5 )

		self.btnEjecutar = wx.Button( Consola.GetStaticBox(), wx.ID_ANY, u"Ejecutar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnEjecutar, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.VERTICAL )

		bSizer4.SetMinSize( wx.Size( -1,400 ) )
		self.txtConsola = wx.TextCtrl( Consola.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		self.txtConsola.SetForegroundColour( wx.Colour( 52, 226, 226 ) )
		self.txtConsola.SetBackgroundColour( wx.Colour( 85, 87, 83 ) )
		self.txtConsola.SetMinSize( wx.Size( -1,350 ) )

		bSizer4.Add( self.txtConsola, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )


		Consola.Add( bSizer2, 1, wx.EXPAND, 5 )


		bSizer1.Add( Consola, 1, wx.EXPAND, 100 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnConectar.Bind( wx.EVT_BUTTON, self.Conectar )
		self.btnLs.Bind( wx.EVT_BUTTON, self.Listar )
		self.btnRepo.Bind( wx.EVT_BUTTON, self.Repositorios )
		self.btnParticiones.Bind( wx.EVT_BUTTON, self.Particiones )
		self.btnEjecutar.Bind( wx.EVT_BUTTON, self.Ejecutar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Conectar( self, event ):
		event.Skip()

	def Listar( self, event ):
		event.Skip()

	def Repositorios( self, event ):
		event.Skip()

	def Particiones( self, event ):
		event.Skip()

	def Ejecutar( self, event ):
		event.Skip()
