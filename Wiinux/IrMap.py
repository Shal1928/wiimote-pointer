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



from Config import ir
from MyMath import *

def ir_map(pos_byte, byte):
	if pos_byte == 8:
		ir['X1'] = ord(byte)
	if pos_byte == 9:
		ir['Y1'] = ord(byte)
	if pos_byte == 10:
		octet = CompleteOctet(Denary2Binary(ord(byte)))
		ir['X1'] = 512*int(octet[2])+256*int(octet[3])+ir['X1']
		ir['Y1'] = 512*int(octet[0])+256*int(octet[1])+ir['Y1']
		ir['S1'] = 8*int(octet[4])+4*int(octet[5])+2*int(octet[6])+int(octet[7])
	if pos_byte == 11:
		ir['X2'] = ord(byte)
	if pos_byte == 12:
		ir['Y2'] = ord(byte)
	if pos_byte == 13:
		octet = CompleteOctet(Denary2Binary(ord(byte)))
		ir['X2'] = 512*int(octet[2])+256*int(octet[3])+ir['X2']
		ir['Y2'] = 512*int(octet[0])+256*int(octet[1])+ir['Y2']
		ir['S2'] = 8*int(octet[4])+4*int(octet[5])+2*int(octet[6])+int(octet[7])

		ir['XT'] = (ir['X1']+ir['X2'])/2
		ir['YT'] = (ir['Y1']+ir['Y2'])/2

