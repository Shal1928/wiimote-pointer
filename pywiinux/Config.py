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


#								#
#								#
#		   INTERNAL VARIABLES				#
#								#
#								#

# Bluetooth channels
wiimote = {
	'control_chanel' : 17,
	'data_chanel' : 19
}

mapped = {
	#	Mouse		#
	'A': '',
	'B': '',
	#	Keyboard	#
	'H': '',
	'+': '',
	'-': '',
	'1': '',
	'2': '',
	'U': '',
	'D': '',
	'L': '',
	'R': '',
	'LM': 'page_down',
	'RM': 'page_up'
}

control = {

	'led1': chr(0x52) + chr(0x11) + chr(0x10),
	
	'led2': chr(0x52) + chr(0x11) + chr(0x20),
	
	'rumble' : chr(0x52) + chr(0x11) + chr(0x21),

	'act_CLK' : chr(0x52) + chr(0x13) + chr(0x04),

	'act_CAM' : chr(0x52) + chr(0x1a) + chr(0x04),

	'act_REG' : chr(0x52) + chr(0x16) + chr(0x04) + chr(0xb0) + chr(0x00) + chr(0x30) + chr(0x01) + chr(0x08) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00),

	'act_SB1' : chr(0x52) + chr(0x16) + chr(0x04) + chr(0xb0) + chr(0x00) + chr(0x00) + chr(0x09) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x90) + chr(0x00) + chr(0xc0) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00),

	'act_SB2' : chr(0x52) + chr(0x16) + chr(0x04) + chr(0xb0) + chr(0x00) + chr(0x1a) + chr(0x01) + chr(0x40) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00),

	'act_MN' : chr(0x52) + chr(0x16) + chr(0x04) + chr(0xb0) + chr(0x00) + chr(0x33) + chr(0x01) + chr(0x03) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00) + chr(0x00),
	'act_IR': chr(0x52) + chr(0x12) + chr(0x00) + chr(0x33)
}

buttons = {
	'A': {
		'state': False,
		'pressed': False
	},
	'B': {
		'state': False,
		'pressed': False
	},
	'H': {
		'state': False,
		'pressed': False
	},
	'+': {
		'state': False,
		'pressed': False
	},
	'-': {
		'state': False,
		'pressed': False
	},
	'1': {
		'state': False,
		'pressed': False
	},
	'2': {
		'state': False,
		'pressed': False
	},
	'U': {
		'state': False,
		'pressed': False
	},
	'D': {
		'state': False,
		'pressed': False
	},
	'L': {
		'state': False,
		'pressed': False
	},
	'R': {
		'state': False,
		'pressed': False
	}
}

angles = {
	'Ax': 0,
	'X': 0,
	'Ay': 0,
	'Y': 0,
	'Az': 0,
	'Z':-90
}

moves = {
	'LM': 0,
	'RM': 0
}

ir = {
	'X1' : 0,
	'Y1' : 0,
	'S1' : 0,
	'X2' : 0,
	'Y2' : 0,
	'S2' : 0,
	'XT' : 400,
	'YT' : 400,
	'counter' : 0
}

