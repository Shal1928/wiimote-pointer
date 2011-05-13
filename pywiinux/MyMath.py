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



def Denary2Binary (n):
	bStr = ''
	if n<0:
		raise ValueError
	if n==0:
		return '0'
	while n>0:
		bStr = str(n % 2) + bStr
		n = n >> 1
	return bStr

def CompleteOctet(bin):
	octet = ''
	if len(bin) == 1:
		octet = '0000000' + bin
	if len(bin) == 2:
		octet = '000000' + bin
	if len(bin) == 3:
		octet = '00000' + bin
	if len(bin) == 4:
		octet = '0000' + bin
	if len(bin) == 5:
		octet = '000' + bin
	if len(bin) == 6:
		octet = '00' + bin
	if len(bin) == 7:
		octet = '0' + bin
	if len(bin) == 8:
		octet = bin
	return octet

