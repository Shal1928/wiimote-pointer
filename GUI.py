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

#
# @author:       Ángel Torrado Carvajal
# @organization: Universidad Rey Juan Carlos
# @copyright:    Ángel Torrado Carvajal (Madrid, Spain)
# @license:      GNU GPL version 2 or any later version
# @contact:      a.torrado@alumnos.urjc.es
#



import sys
import time

import pygtk
pygtk.require('2.0')
import gtk
# Initializing the gtk's thread engine
gtk.gdk.threads_init()

import matplotlib
matplotlib.use('GTK')
from matplotlib.figure import Figure
from matplotlib.axes import Subplot
from matplotlib.backends.backend_gtk import FigureCanvasGTK

from threading import Thread



class GUI(Thread):

	def __init__(self, parent_obj):

		self.__parent_obj = parent_obj
		self.__plots_started = False

		# Create a new window
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_border_width(5)
		window.set_default_size(640, 480)
		window.set_title("Wiinux")
		# With this we can close the program
		window.connect("destroy", lambda x: gtk.main_quit())

		root_window = window.get_root_window()
		self.geometry = root_window.get_geometry()

		# Create a Frame
		frame = gtk.Frame()
		window.add(frame)
		# Set the style of the frame
		frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
		frame.show()

		# Create a Vertical Box
		vbox = gtk.VBox(False, 0)
		vbox.set_border_width(0)
		frame.add(vbox)

		frame1 = gtk.Frame()
		frame1.set_shadow_type(gtk.SHADOW_NONE)
		hbox = gtk.HBox(False, 0)
		hbox.set_border_width(0)
		frame1.add(hbox)

		framel = gtk.Frame()
		bboxl = gtk.VButtonBox()
		bboxl.set_border_width(5)
		framel.add(bboxl)

		# Set the appearance of the Button Box
		bboxl.set_layout(gtk.BUTTONBOX_SPREAD)
		bboxl.set_spacing(10)

		self.buttonconnect = gtk.Button(stock=gtk.STOCK_CONNECT)
		self.buttonconnect.connect("clicked", self.open_connect)
		bboxl.add(self.buttonconnect)

		self.buttondisconnect = gtk.Button(stock=gtk.STOCK_DISCONNECT)
		self.buttondisconnect.connect("clicked", self.open_disconnect)
		bboxl.add(self.buttondisconnect)
		self.buttondisconnect.set_sensitive(False)

		self.buttonplots = gtk.Button(stock=gtk.STOCK_INFO)
		self.buttonplots.connect("clicked", self.open_plots)
		bboxl.add(self.buttonplots)
		self.buttonplots.set_sensitive(False)

		# Create the right frame
		framer = gtk.Frame()
		hboxconfig = gtk.HBox(False, 0)
		hboxconfig.set_border_width(0)
		framer.add(hboxconfig)

		frameimage = gtk.Frame()
		frameimage.set_shadow_type(gtk.SHADOW_NONE)
		image = gtk.Image()
		image.set_from_file("Wiimote.png")
		image.show()
		frameimage.add(image)

		framename = gtk.Frame()
		framename.set_shadow_type(gtk.SHADOW_NONE)
		bboxname = gtk.VButtonBox()
		bboxname.set_border_width(0)
		framename.add(bboxname)

		# Set the appearance of the name Box
		bboxname.set_layout(gtk.BUTTONBOX_CENTER)
		bboxname.set_spacing(12)

		labels = ["Up:", "Right:", "Down:", "Left:", "A:", "B:", "+:", "-:",
				"Home:", "1:", "2:"]

		for name in labels:
			label = gtk.Label(name)
			label.set_justify(gtk.JUSTIFY_LEFT)
			bboxname.add(label)

		frameselect = gtk.Frame()
		frameselect.set_shadow_type(gtk.SHADOW_NONE)
		bboxselect = gtk.VButtonBox()
		bboxselect.set_border_width(0)
		frameselect.add(bboxselect)

		# Set the appearance of the right Button Box
		# Combo box with options
		bboxselect.set_layout(gtk.BUTTONBOX_CENTER)
		bboxselect.set_spacing(10)

		self.combobox = []
		for i in range(4):
			self.combobox.append(gtk.combo_box_new_text())
			self.complete_keys(self.combobox[i])
			self.combobox[i].set_active(i)
			bboxselect.add(self.combobox[i])

		for i in range(2):
			self.combobox.append(gtk.combo_box_new_text())
			self.complete_mouse(self.combobox[i+4])
			self.combobox[i+4].set_active(i)
			bboxselect.add(self.combobox[i+4])

		for i in range(5):
			self.combobox.append(gtk.combo_box_new_text())
			self.complete_keys(self.combobox[i+6])
			self.combobox[i+6].set_active(i+4)
			bboxselect.add(self.combobox[i+6])

		vbox.pack_start(frame1, True, True, 0)
		hbox.pack_start(framel, True, True, 0)
		hbox.pack_start(framer, True, True, 0)
		hboxconfig.pack_start(frameimage, True, True, 0)
		hboxconfig.pack_start(framename, True, True, 0)
		hboxconfig.pack_start(frameselect, True, True, 0)

		# Create frame with button box
		frame2 = gtk.Frame()
		frame2.set_shadow_type(gtk.SHADOW_NONE)
		bbox = gtk.HButtonBox()
		bbox.set_border_width(5)
		frame2.add(bbox)
		# Set the appearance of the Button Box
		bbox.set_layout(gtk.BUTTONBOX_END)
		bbox.set_spacing(10)
		# Create "Help" button
		buttonhelp = gtk.Button(stock=gtk.STOCK_HELP)
		buttonhelp.connect("clicked", self.open_help)
		bbox.add(buttonhelp)
		# Create "Quit" button
		buttonquit = gtk.Button(stock=gtk.STOCK_CLOSE)
		# When the button is clicked, we call the main_quit function
		# and the program exits
		buttonquit.connect("clicked", self.exit_program)
		bbox.add(buttonquit)

		vbox.pack_start(frame2, True, True, 0)

		window.show_all()

		Thread.__init__(self)



#
#
# GUI ACTIONS
#
#

	# If CONNECT is pressed...
	def open_connect(self, widget, data=None):
		self.open_connect_aux()
		selected = self.read_options()
		self.__parent_obj.notify_start_connection(selected, self.geometry)

	def open_connect_aux(self):
		# Disable all buttons
		self.buttonconnect.set_sensitive(False)
		for i in range (11):
			self.combobox[i].set_sensitive(False)

		# Create a new window
		self.windowconnect = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windowconnect.set_border_width(5)
		self.windowconnect.set_title("Connection progress")
		self.windowconnect.set_default_size(500,20);

		# Create a new progress bar
		self.progressbar = gtk.ProgressBar()
		self.progressbar.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
		self.progressbar.set_text("Connecting...")
		self.progressbar.show()

		vboxconnect = gtk.VBox(False, 0)
		vboxconnect.set_border_width(5)

		vboxconnect.pack_start(self.progressbar, True, True, 0)
		vboxconnect.show()

		self.windowconnect.add(vboxconnect)
		self.windowconnect.show_all()

	# Read combobox selected options
	def read_options(self):
		options = []
		for i in range (11):
			options.append(self.get_active_text(self.combobox[i]))
		return options

	# Set progress
	def set_progress(self, progress):
		self.progressbar.set_fraction(progress)

	def end_connection_dialog(self):
		self.windowconnect.destroy()
		self.buttondisconnect.set_sensitive(True)
		self.buttonplots.set_sensitive(True)



	# If DISCONNECT is pressed...
	def open_disconnect(self, widget, data=None):
		self.open_disconnect_aux()
		self.__parent_obj.notify_finish_connection()

	def open_disconnect_aux(self):
		self.buttondisconnect.set_sensitive(False)

		# Enable all buttons
		self.buttonconnect.set_sensitive(True)
		for i in range (11):
			self.combobox[i].set_sensitive(True)
		# Disable Info button
		self.buttonplots.set_sensitive(False)



	# If SENSORS is pressed...
	def open_plots(self, widget, data=None):
		# Create a new window
		self.windowplots = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windowplots.set_border_width(5)
		self.windowplots.set_default_size(800, 600)
		self.windowplots.set_title("Sensors")

		self.x_angles = []
		self.y_angles = []
		self.z_angles = []

		# Create a Frame
		frameplots = gtk.Frame()
		self.windowplots.add(frameplots)
		# Set the style of the frame
		frameplots.set_shadow_type(gtk.SHADOW_NONE)
		frameplots.show()
		frameplots.set_label_align(0.5, 0.0)

		self.vboxplots = gtk.VBox(False, 0)
		self.vboxplots.set_border_width(5)
		frameplots.add(self.vboxplots)

		# Create a Frame
		self.framecontent = gtk.Frame()
		# Set the style of the frame
		self.framecontent.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
		self.framecontent.set_label_align(0.5, 0.0)
		self.vboxcontent = gtk.VBox(False, 0)
		self.vboxcontent.set_border_width(5)
		self.vboxcontent.set_reallocate_redraws(True)

		# Create Plots
		self.figure = Figure(figsize=(4,4), dpi=72)
		self.figure.subplots_adjust(left=0.125, bottom=0.1, right= 0.9, top=0.9, wspace=0.3, hspace=0.4)

		# X axis
		self.x_axis = self.figure.add_subplot(221)
		self.x_axis.hold(False)

		# Y axis
		self.y_axis = self.figure.add_subplot(222)
		self.y_axis.hold(False)

		# Z axis
		self.z_axis = self.figure.add_subplot(223)
		self.z_axis.hold(False)

		# IR axis
		self.ir_axis = self.figure.add_subplot(224)
		self.ir_axis.hold(False)

		self.canvas = FigureCanvasGTK(self.figure)
		self.canvas.show()
		self.vboxcontent.pack_start(self.canvas, True, True, 0)
		self.framecontent.add(self.vboxcontent)

		self.vboxplots.pack_start(self.framecontent, True, True, 0)

		# Create a Frame
		framequit = gtk.Frame()
		bbox = gtk.HButtonBox()
		bbox.set_border_width(5)
		framequit.add(bbox)
		# Set the appearance of the Button Box
		bbox.set_layout(gtk.BUTTONBOX_SPREAD)
		# Set the style of the frame
		framequit.set_shadow_type(gtk.SHADOW_NONE)

		# Create "Ok" button
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_plots)
		bbox.add(button)

		self.vboxplots.pack_start(framequit, False, True, 0)
		self.windowplots.show_all()
		self.__plots_started = True

	def replot(self, x_angle, y_angle, z_angle, x_pos, y_pos):
		if self.__plots_started:
			if len(self.x_angles) == 25:
				self.x_angles.remove(self.x_angles[0])
				self.y_angles.remove(self.y_angles[0])
				self.z_angles.remove(self.z_angles[0])

			self.x_angles.append(x_angle)
			self.y_angles.append(y_angle)
			self.z_angles.append(z_angle)

			# X axis
			self.x_axis.plot(self.x_angles, 'r', linewidth=2)
			self.x_axis.set_title("Eje X")
			self.x_axis.set_xlabel("Muestras")
			self.x_axis.set_ylabel("Ángulo")
			self.x_axis.grid(True)
			self.x_axis.axis([0, 24, -100, 100])

			# Y axis
			self.y_axis.plot(self.y_angles, 'b', linewidth=2)
			self.y_axis.set_title("Eje Y")
			self.y_axis.set_xlabel("Muestras")
			self.y_axis.set_ylabel("Ángulo")
			self.y_axis.grid(True)
			self.y_axis.axis([0, 24, -100, 100])

			# Z axis
			self.z_axis.plot(self.z_angles, 'g', linewidth=2)
			self.z_axis.set_title("Eje Z")
			self.z_axis.set_xlabel("Muestras")
			self.z_axis.set_ylabel("Ángulo")
			self.z_axis.grid(True)
			self.z_axis.axis([0, 24, -100, 100])

			# IR
			self.ir_axis.plot([-10, x_pos], [-10, y_pos], '*r')
			self.ir_axis.set_title("Cámara infrarroja")
			self.ir_axis.set_xlabel("X axis")
			self.ir_axis.set_ylabel("Y axis")
			self.ir_axis.grid(True)
			self.ir_axis.axis([0, 1024, 0, 768])

			self.vboxcontent.reorder_child(self.canvas,1)

	def close_plots(self, widget, data=None):
		self.__plots_started = False
		self.windowplots.destroy()



	# If HELP is pressed...
	def open_help(self, widget, data=None):
		# Create a new window
		self.windowhelp = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windowhelp.set_border_width(5)
		self.windowhelp.set_title("Help")

		# Create a Frame
		framehelp = gtk.Frame()
		self.windowhelp.add(framehelp)
		# Set the style of the frame
		framehelp.set_shadow_type(gtk.SHADOW_NONE)
		framehelp.show()
		framehelp.set_label_align(0.5, 0.0)

		vboxhelp = gtk.VBox(False, 0)
		vboxhelp.set_border_width(5)
		framehelp.add(vboxhelp)

		# Create a Frame
		framecontent = gtk.Frame("HELP")
		# Set the style of the frame
		framecontent.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
		framecontent.set_label_align(0.5, 0.0)
		# Create Label
		labelhelp = gtk.Label("\nConfiguración:\n"
						"Para configurar el Wiimote selecciona el\n"
						"mapeo de los botones en los desplegables\n"
						"de la derecha.\n"
						"\nConexión:\n"
						"Para iniciar la conexión con el Wiimote,\n"
						"pulsa el botón de conexión y simultáneamente\n"
						"los botones 1 y 2 del Wiimote. Cuando la\n"
						"conexión haya finalizado, el Wiimote vibrará.\n"
						"\nDesconexión:\n"
						"Para finalizar la conexión con el Wiimote,\n"
						"pulsa el botón de desconexión.\n"
						"\nInformación:\n"
						"Si quieres conocer el estado de los sensores\n"
						"del Wiimote, pulsa el botón de información y\n"
						"podrás conocer valores relacionados con los\n"
						"acelerómetros y la cámara infrarroja.\n"
						)
		labelhelp.set_justify(gtk.JUSTIFY_CENTER)
		labelhelp.set_line_wrap(True)
		framecontent.add(labelhelp)

		vboxhelp.pack_start(framecontent, True, True, 0)

		# Create a Frame
		framequit = gtk.Frame()
		bbox = gtk.HButtonBox()
		bbox.set_border_width(5)
		framequit.add(bbox)
		# Set the appearance of the Button Box
		bbox.set_layout(gtk.BUTTONBOX_END)
		bbox.set_spacing(10)
		# Set the style of the frame
		framequit.set_shadow_type(gtk.SHADOW_NONE)

		# Create "About" button
		button = gtk.Button("About")
		button.connect("clicked", self.open_about)
		bbox.add(button)
		
		# Create "Licence" button
		button = gtk.Button("Licence")
		button.connect("clicked", self.open_licence)
		bbox.add(button)
		
		# Create "Ok" button
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_help)
		bbox.add(button)

		vboxhelp.pack_start(framequit, True, True, 0)

		self.windowhelp.show_all()

	def close_help(self, widget, data=None):
		self.windowhelp.destroy()



	# If ABOUT is pressed...
	def open_about(self, widget, data=None):
		# Create a new window
		self.windowabout = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windowabout.set_border_width(5)
		self.windowabout.set_title("About")

		# Create a Frame
		framecredits = gtk.Frame()
		self.windowabout.add(framecredits)
		# Set the style of the frame
		framecredits.set_shadow_type(gtk.SHADOW_NONE)
		framecredits.show()
		framecredits.set_label_align(0.5, 0.0)

		vboxcredits = gtk.VBox(False, 0)
		vboxcredits.set_border_width(5)
		framecredits.add(vboxcredits)

		# Create a Frame
		framecontent = gtk.Frame("WIINUX.PY VERSION 1.0")
		# Set the style of the frame
		framecontent.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
		framecontent.set_label_align(0.5, 0.0)
		# Create Label
		labelabout = gtk.Label("\nPrograma desarrollado para el PFC"
						" 'Diseño e\n"
						"Implementación de Librerías para la"
						" Adaptación\n"
						"del Wiimote como Pizarra Digital\n"
						"Interactiva'\n"
						"\nAutor: Ángel Torrado Carvajal\n"
						"Tutor: Israel Herraiz Tabernero\n"
						"Co-Tutor: Gregorio Robles Martínez\n"
						"\nEscuela Técnica Superior de\n"
						"Ingeniería de Telecomunicación\n"
						"\nUniversidad Rey Juan Carlos\n"
						)
		labelabout.set_justify(gtk.JUSTIFY_CENTER)
		labelabout.set_line_wrap(True)
		framecontent.add(labelabout)

		vboxcredits.pack_start(framecontent, True, True, 0)

		# Create a Frame
		framequit = gtk.Frame()
		bbox = gtk.HButtonBox()
		bbox.set_border_width(5)
		framequit.add(bbox)
		# Set the appearance of the Button Box
		bbox.set_layout(gtk.BUTTONBOX_SPREAD)
		# Set the style of the frame
		framequit.set_shadow_type(gtk.SHADOW_NONE)

		# Create "Ok" button
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_about)
		bbox.add(button)

		vboxcredits.pack_start(framequit, True, True, 0)

		self.windowabout.show_all()

	def close_about(self, widget, data=None):
		self.windowabout.destroy()



	# If LICENCE is pressed...
	def open_licence(self, widget, data=None):
		# Create a new window
		self.windowlicence = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.windowlicence.set_border_width(5)
		self.windowlicence.set_title("Licence")

		# Create a Frame
		framelicence = gtk.Frame()
		self.windowlicence.add(framelicence)
		# Set the style of the frame
		framelicence.set_shadow_type(gtk.SHADOW_NONE)
		framelicence.show()
		framelicence.set_label_align(0.5, 0.0)

		vboxlicence = gtk.VBox(False, 0)
		vboxlicence.set_border_width(5)
		framelicence.add(vboxlicence)

		# Create a Frame
		framecontent = gtk.Frame()
		# Set the style of the frame
		framecontent.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
		framecontent.set_label_align(0.5, 0.0)
		# Create Label
		labelabout = gtk.Label("\nEste programa es sotware libre. Puede"
						" redistribuirlo y/o modificarlo bajo los"
						" términos de la Licencia Pública General"
						" de GNU según se encuentra publicada por"
						" la Free Software Foundation, bien de la"
						" versión 2 de dicha Licencia o bien (según"
						" su elección) de cualquier versión"
						" posterior.\n"
						"\nEste programa se distribuye con la"
						" esperanza de que sea útil, pero SIN"
						" NINGUNA GARANTÍA, incluso sin la garantía"
						" MERCANTIL implícita o sin garantizar"
						" ADECUACIÓN A UN PROPÓSITO PARTICULAR."
						" Véase la Licencia Pública General de GNU"
						" para más detalles.\n"
						"\nDebería haber recibido una copia de la"
						" Licencia Pública General junto con este"
						" programa. Si no ha sido así, escriba a la"
						" Free Software Foundation, Inc., 59 Temple"
						" Place - Suite 330, Boston, MA 02111-1207,"
						" USA.\n"
						)
		labelabout.set_justify(gtk.JUSTIFY_CENTER)
		labelabout.set_line_wrap(True)
		framecontent.add(labelabout)

		vboxlicence.pack_start(framecontent, True, True, 0)

		# Create a Frame
		framequit = gtk.Frame()
		bbox = gtk.HButtonBox()
		bbox.set_border_width(5)
		framequit.add(bbox)
		# Set the appearance of the Button Box
		bbox.set_layout(gtk.BUTTONBOX_SPREAD)
		# Set the style of the frame
		framequit.set_shadow_type(gtk.SHADOW_NONE)

		# Create "Ok" button
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_licence)
		bbox.add(button)

		vboxlicence.pack_start(framequit, True, True, 0)

		self.windowlicence.show_all()

	def close_licence(self, widget, data=None):
		self.windowlicence.destroy()


	# If CLOSE is pressed...
	def exit_program(self, widget, data=None):
		try:
			self.__parent_obj.notify_finish_connection()
		except:
			pass
		time.sleep(0.1) # Wait for disconnection
		sys.exit(1)


	# ComboBox operations
	def complete_keys(self, combo):
		self.keys=["Up key", "Right key", "Down key", "Left key",
				"Plus key" ,"Minus key", "Escape",
				"Page Up", "Page Down"]
		pos = 0
		for key in self.keys:
			combo.append_text(self.keys[pos])
			pos = pos + 1

	def complete_mouse(self, combo):
		combo.append_text("Left Button")
		combo.append_text("Right Button")
		combo.append_text("Center Button")		

	def get_active_text(self, combobox):
		model = combobox.get_model()
		active = combobox.get_active()
		if active < 0:
			return None
		return model[active][0]



	# Error dialogs
	def no_wiimote_dialog(self):
		self.dialog = gtk.Dialog("Error", None)
		self.dialog.flags="DIALOG_DESTROY_WITH_PARENT"
		label = gtk.Label("\nCould not find Wiimote nearby\n")
		self.dialog.vbox.pack_start(label, True, True, 0)
		label.show()
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_dialog)
		self.dialog.action_area.pack_start(button, True, True, 0)
		button.show()
		self.dialog.show()

	def wiimote_interruption_dialog(self):
		self.dialog = gtk.Dialog("Error", None)
		self.dialog.flags="DIALOG_DESTROY_WITH_PARENT"
		label = gtk.Label("\nConnection interrumped by Wiimote\n")
		self.dialog.vbox.pack_start(label, True, True, 0)
		label.show()
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_dialog)
		self.dialog.action_area.pack_start(button, True, True, 0)
		button.show()
		self.dialog.show()

	def bluetooth_error_dialog(self):
		self.dialog = gtk.Dialog("Error", None)
		self.dialog.flags="DIALOG_DESTROY_WITH_PARENT"
		label = gtk.Label("\nError accessing bluetooth device\n")
		self.dialog.vbox.pack_start(label, True, True, 0)
		label.show()
		button = gtk.Button(stock=gtk.STOCK_OK)
		button.connect("clicked", self.close_dialog)
		self.dialog.action_area.pack_start(button, True, True, 0)
		button.show()
		self.dialog.show()

	def close_dialog(self, widget, data=None):
		self.dialog.destroy()

