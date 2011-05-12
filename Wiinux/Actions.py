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

import os

from Config import buttons
from Config import moves
from Config import mapped
from Config import ir

def moving():
	if moves['RM'] > moves['LM']:
		os.system("xte 'key " + mapped['RM'] + "'")
		moves['RM'] = 0
		moves['LM'] = 0
	if moves['RM'] < moves['LM']:
		os.system("xte 'key " + mapped['LM'] + "'")
		moves['RM'] = 0
		moves['LM'] = 0

def pressing():
	if (buttons['A']['pressed'] == True) and (buttons['A']['state'] == False):
		os.system("xte 'mousedown " + mapped['A'] + "'")
	if (buttons['A']['pressed'] == False) and (buttons['A']['state'] == True):
		os.system("xte 'mouseup " + mapped['A'] + "'")

	if (buttons['B']['pressed'] == True) and (buttons['B']['state'] == False):
		os.system("xte 'mousedown " + mapped['B'] + "'")
	if (buttons['B']['pressed'] == False) and (buttons['B']['state'] == True):
		os.system("xte 'mouseup " + mapped['B'] + "'")

	if (buttons['H']['pressed'] == True) and (buttons['H']['state'] == False):
		os.system("xte 'keydown " + mapped['H'] + "'")
	if (buttons['H']['pressed'] == False) and (buttons['H']['state'] == True):
		os.system("xte 'keyup " + mapped['H'] + "'")

	if (buttons['+']['pressed'] == True) and (buttons['+']['state'] == False):
		os.system("xte 'keydown " + mapped['+'] + "'")
	if (buttons['+']['pressed'] == False) and (buttons['+']['state'] == True):
		os.system("xte 'keyup " + mapped['+'] + "'")

	if (buttons['-']['pressed'] == True) and (buttons['-']['state'] == False):
		os.system("xte 'keydown " + mapped['-'] + "'")
	if (buttons['-']['pressed'] == False) and (buttons['-']['state'] == True):
		os.system("xte 'keyup " + mapped['-'] + "'")

	if (buttons['1']['pressed'] == True) and (buttons['1']['state'] == False):
		os.system("xte 'keydown " + mapped['1'] + "'")
	if (buttons['1']['pressed'] == False) and (buttons['1']['state'] == True):
		os.system("xte 'keyup " + mapped['1'] + "'")

	if (buttons['2']['pressed'] == True) and (buttons['2']['state'] == False):
		os.system("xte 'keydown " + mapped['2'] + "'")
	if (buttons['2']['pressed'] == False) and (buttons['2']['state'] == True):
		os.system("xte 'keyup " + mapped['2'] + "'")

	if (buttons['U']['pressed'] == True) and (buttons['U']['state'] == False):
		os.system("xte 'keydown " + mapped['U'] + "'")
	if (buttons['U']['pressed'] == False) and (buttons['U']['state'] == True):
		os.system("xte 'keyup " + mapped['U'] + "'")

	if (buttons['D']['pressed'] == True) and (buttons['D']['state'] == False):
		os.system("xte 'keydown " + mapped['D'] + "'")
	if (buttons['D']['pressed'] == False) and (buttons['D']['state'] == True):
		os.system("xte 'keyup " + mapped['D'] + "'")

	if (buttons['L']['pressed'] == True) and (buttons['L']['state'] == False):
		os.system("xte 'keydown " + mapped['L'] + "'")
	if (buttons['L']['pressed'] == False) and (buttons['L']['state'] == True):
		os.system("xte 'keyup " + mapped['L'] + "'")

	if (buttons['R']['pressed'] == True) and (buttons['R']['state'] == False):
		os.system("xte 'keydown " + mapped['R'] + "'")
	if (buttons['R']['pressed'] == False) and (buttons['R']['state'] == True):
		os.system("xte 'keyup " + mapped['R'] + "'")

def positioning(width, height, root_window):
	if (ir['XT'] > 200 and ir['XT'] < 823 and ir['YT'] > 0 and ir['YT'] < 750):

		horiz = width-int((float(width)/623.000)*(ir['XT']-200))
		vert = int((float(height)/750.000)*ir['YT'])

		root_window.warp_pointer(horiz,vert)
