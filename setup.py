#!/usr/bin/env python
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

"""
Installer

@author:       Ángel Torrado Carvajal
@organization: Universidad Rey Juan Carlos
@copyright:    Ángel Torrado Carvajal (Madrid, Spain)
@license:      GNU GPL version 2 or any later version
@contact:      a.torrado@alumnos.urjc.es
"""

from distutils.core import setup

setup(name = "Wiinux",
      version = "1.0",
      author = "Ángel Torrado Carvajal",
      author_email = "a.torrado@alumnos.urjc.es",
      description = "Low cost virtual laser pointer and whiteboard using a Wiimote",
      long_description = "",
      url = "http://code.google.com/p/wiimote-pointer/",
      platforms = ["any"],
      packages = ["Wiinux"],
      scripts = ["wiinux"],
      data_files = [('share/Wiinux/bitmaps',['share/Wiinux/bitmaps/Wiimote.png'])],
      requires = ["matplotlib","pygtk","bluetooth"])
