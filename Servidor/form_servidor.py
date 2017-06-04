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
## Class Servidor
###########################################################################

class Servidor ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Comandos de sistema - Servidor", pos = wx.DefaultPosition, size = wx.Size( 800,420 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

		Principal = wx.FlexGridSizer( 5, 5, 0, 0 )
		Principal.SetFlexibleDirection( wx.BOTH )
		Principal.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		Principal.AddSpacer( ( 40, 40), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.lblCliente = wx.StaticText( self, wx.ID_ANY, u"Conectado desde:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCliente.Wrap( -1 )
		Principal.Add( self.lblCliente, 0, wx.ALL, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )


		Principal.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )

		self.txtResultado = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 700,250 ), wx.TE_MULTILINE )
		self.txtResultado.SetForegroundColour( wx.Colour( 52, 226, 226 ) )
		self.txtResultado.SetBackgroundColour( wx.Colour( 85, 87, 83 ) )

		Principal.Add( self.txtResultado, 0, wx.ALL, 5 )


		self.SetSizer( Principal )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass
