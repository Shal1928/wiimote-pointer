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



from Config import buttons
from MyMath import *
from Actions import *

def button_map(pos_byte,byte):
	if pos_byte == 3:
		octet = CompleteOctet(Denary2Binary(ord(byte)))

		buttons['+']['state'] = buttons['+']['pressed']
		buttons['U']['state'] = buttons['U']['pressed']
		buttons['D']['state'] = buttons['D']['pressed']
		buttons['R']['state'] = buttons['R']['pressed']
		buttons['L']['state'] = buttons['L']['pressed']

		if octet[3] == '0':
			buttons['+']['pressed'] = False
		if octet[3] == '1':
			buttons['+']['pressed'] = True
		if octet[4] == '0':
			buttons['U']['pressed'] = False
		if octet[4] == '1':
			buttons['U']['pressed'] = True
		if octet[5] == '0':
			buttons['D']['pressed'] = False
		if octet[5] == '1':
			buttons['D']['pressed'] = True
		if octet[6] == '0':
			buttons['R']['pressed'] = False
		if octet[6] == '1':
			buttons['R']['pressed'] = True
		if octet[7] == '0':
			buttons['L']['pressed'] = False
		if octet[7] == '1':
			buttons['L']['pressed'] = True

	if pos_byte == 4:
		octet = CompleteOctet(Denary2Binary(ord(byte)))

		buttons['H']['state'] = buttons['H']['pressed']
		buttons['-']['state'] = buttons['-']['pressed']
		buttons['A']['state'] = buttons['A']['pressed']
		buttons['B']['state'] = buttons['B']['pressed']
		buttons['1']['state'] = buttons['1']['pressed']
		buttons['2']['state'] = buttons['2']['pressed']

		if octet[0] == '0':
			buttons['H']['pressed'] = False
		if octet[0] == '1':
			buttons['H']['pressed'] = True
		if octet[3] == '0':
			buttons['-']['pressed'] = False
		if octet[3] == '1':
			buttons['-']['pressed'] = True
		if octet[4] == '0':
			buttons['A']['pressed'] = False
		if octet[4] == '1':
			buttons['A']['pressed'] = True
		if octet[5] == '0':
			buttons['B']['pressed'] = False
		if octet[5] == '1':
			buttons['B']['pressed'] = True
		if octet[6] == '0':
			buttons['1']['pressed'] = False
		if octet[6] == '1':
			buttons['1']['pressed'] = True
		if octet[7] == '0':
			buttons['2']['pressed'] = False
		if octet[7] == '1':
			buttons['2']['pressed'] = True

