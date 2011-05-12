#coding: utf-8 -*-

# Copyright (C) 2010 Ángel Torrado Carvajal
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
# 02111-1307, USA.
#
# Authors : Ángel Torrado Carvajal <a.torrado@alumnos.urjc.es>

#
# @author:       Ángel Torrado Carvajal
# @organization: Universidad Rey Juan Carlos
# @copyright:    Ángel Torrado Carvajal (Madrid, Spain)
# @license:      GNU GPL version 2 or any later version
# @contact:      a.torrado@alumnos.urjc.es
#



import bluetooth
import time
from threading import Thread
import Xlib.display

from Config import *
from ButtonMap import *
from AngleMap import *
from IrMap import *
from Actions import *

class WiimoteConnect(Thread):

	def __init__(self, parent_obj, geometry):
		self.__parent_obj = parent_obj
		self.__geometry = geometry
		self.__finish_con = False
		
		self.__display = Xlib.display.Display()
		self.__screen = self.__display.screen()
		self.__root = self.__screen.root
		
		Thread.__init__(self)
		
	def run(self):
		self.connect()
		
	def connect(self):

		try:	# Search only for Wiimotes
			target_name = "Nintendo RVL-CNT-01"
			target_address = None

			nearby_devices = bluetooth.discover_devices()

			for bdaddr in nearby_devices:
				if target_name == bluetooth.lookup_name(bdaddr):
					target_address = bdaddr
					break

			if target_address is not None:
				print "Found Wiimote device with address ", target_address

				# Bluetooth sockets creation
				wiimote_control_chanel = wiimote['control_chanel']
				wiimote_data_chanel = wiimote['data_chanel']
				print 'Beginning connection with Wiimote MAC: ' + target_address
				control_socket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
				data_socket = bluetooth.BluetoothSocket(bluetooth.L2CAP)
				print 'Socket Bluetooth created successfully!'
				control_socket.connect((target_address, wiimote_control_chanel))
				print 'Connected with Wiimote at control port ' + str(wiimote_control_chanel)
				data_socket.connect((target_address, wiimote_data_chanel))
				print 'Connected with Wiimote at data port ' + str(wiimote_data_chanel)
				packet_size = 1024

				# Initialization sequence
				control_socket.send(control['act_IR'])
				self.__parent_obj.notify_progress(0.1)
				print 'led'
				control_socket.send(control['led2']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.2)
				print 'clk'
				control_socket.send(control['act_CLK']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.3)
				print 'cam'
				control_socket.send(control['led1'])
				control_socket.send(control['act_CAM']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.4)
				print 'reg1'
				control_socket.send(control['act_REG']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.5)
				print 'secuencia1'
				control_socket.send(control['led2'])
				control_socket.send(control['act_SB1']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.6)
				print 'secuencia2'
				control_socket.send(control['act_SB2']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.7)
				print 'mode'
				control_socket.send(control['led1'])
				control_socket.send(control['act_MN']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.8)
				print 'reg2'
				control_socket.send(control['act_REG']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(0.9)
				control_socket.send(control['rumble']);	time.sleep(0.05)
				self.__parent_obj.notify_progress(1);	time.sleep(0.4)
				control_socket.send(control['led1'])


				print '----- Receiving packets -----'
				s = data_socket.recv(packet_size)
				if s == '':
					raise RuntimeError, 'Broken connection'


				self.__parent_obj.notify_progress(1)

				self.__parent_obj.notify_end_connection()

				loop = 1
				while s and not self.__finish_con:

					#moving()
					self.__parent_obj.notify_sensors(angles['X'], angles['Y'], angles['Z'],	ir['XT'], ir['YT'])
				
					if s == '':
						raise RuntimeError, 'Broken connection'



					pos_byte = 1
					for byte in s:
						if (pos_byte == 3) or (pos_byte == 4):
							button_map(pos_byte,byte)
						if (pos_byte == 5) or (pos_byte == 6) or (pos_byte == 7):
							angle_map(pos_byte,byte)
						if (pos_byte > 7):
							ir_map(pos_byte,byte)
						pos_byte = pos_byte + 1
					pressing()
					positioning(self.__geometry[2], self.__geometry[3], self.__root)
					self.__display.sync()

					s = data_socket.recv(packet_size)
					#loop = loop + 1

			else:
				# Could not find Wiimote nearby
				self.__parent_obj.notify_no_wiimote()
		except RuntimeError, e:
		  	# Connection interrumped by Wiimote
		  	self.__parent_obj.notify_wiimote_interruption()
		except bluetooth.btcommon.BluetoothError, e:
			# Error accessing bluetooth device
			self.__parent_obj.notify_bluetooth_error()

	def stop(self):
		self.__finish_con = True

