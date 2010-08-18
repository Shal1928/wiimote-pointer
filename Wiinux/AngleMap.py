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



from Config import angles
from Config import moves

def angle_map(pos_byte, byte):
	if pos_byte == 5:
		angles['X'] = (ord(byte)-125)*3.6
		angles['Ax'] = angles['X'] - (ord(byte)-125)*3.6
		if angles['Ax'] <-60:
			moves['RM'] = moves['RM'] + 1
		if angles['Ax'] >60:
			moves['LM'] = moves['LM'] + 1
	if pos_byte == 6:
		angles['Ay'] = angles['Y'] - (ord(byte)-125)*3.6
		angles['Y'] = (ord(byte)-125)*3.6
	if pos_byte == 7:
		angles['Az'] = angles['Z'] - (ord(byte)-125)*3.6
		angles['Z'] = (ord(byte)-125)*3.6

