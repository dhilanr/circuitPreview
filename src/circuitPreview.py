#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, EvinceDocument, EvinceView

from pylatex import (Document, Package, NoEscape)
import os
import subprocess


class Paned(Gtk.Window):
    def __init__(self):
        self.wd = os.getcwd()
        Gtk.Window.__init__(self)
        self.set_title("circuit_macros editor")
        self.set_default_size(1125, 775)
        self.connect('destroy', Gtk.main_quit)

        ## Create Panes
        self.hpaned = Gtk.Paned()        # horizontal division
        self.hpaned.set_position(550)
        self.add(self.hpaned)

        self.create_toolbar()
        self.create_textview()
        self.create_preview()
    
    def create_toolbar(self):
        # Left Pane Vertical Division (Toolbar Space)
        self.vpaned_left = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        self.vpaned_left.set_position(50)
        self.hpaned.add1(self.vpaned_left)

        # Toolbar + Button
        toolbar = Gtk.Toolbar()
        save_button = Gtk.ToolButton()
        save_button.set_label("Generate PDF")
        save_button.set_is_important(True)
        save_button.set_icon_name("media-playback-start-symbolic")
        toolbar.add(save_button)
        save_button.connect("clicked", self.on_save_clicked)
        self.vpaned_left.add1(toolbar)

    def create_textview(self):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)

        self.textview = Gtk.TextView()
        self.textview.set_wrap_mode(True)
        
        self.textview.set_top_margin(20)
        self.textview.set_left_margin(20)
        self.textview.set_right_margin(20)
        self.textview.set_bottom_margin(20)

        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(
            "Replace this text with your circuit_macros M4 code."
        )
        scrolledwindow.add(self.textview)
        self.vpaned_left.add2(scrolledwindow)

    def create_preview(self):
        # Right Pane Division
        self.vpaned_right = Gtk.Paned(orientation=Gtk.Orientation.VERTICAL)
        self.vpaned_right.set_position(725)
        self.hpaned.add2(self.vpaned_right)

        # Right Top Division Scrolled PDF Preview Placeholder Creation
        self.scrollRight = Gtk.ScrolledWindow()
        EvinceDocument.init()
        doc = EvinceDocument.Document.factory_get_document("file:"+self.wd+"/placeholder.pdf")
        self.view = EvinceView.View()
        self.model = EvinceView.DocumentModel()
        self.model.set_document(doc)
        self.view.set_model(self.model)
        self.scrollRight.add(self.view)
        self.vpaned_right.add1(self.scrollRight)

        label = Gtk.Label(label='Created by Dhilan, for Dhilan :)')
        self.vpaned_right.add2(label)

    def getText(self):
        buffer = self.textview.get_buffer()
        startIter, endIter = buffer.get_bounds()    
        text = buffer.get_text(startIter, endIter, False) 
        return text

    def text2m4(self):
        with open("out.m4", "w+") as m4:
            m4.write(self.getText())
    
    def toPic(self):
        # m4 pgf.m4 figures/dff_latch.m4 > dff_latch.pic
        with open("out.pic", "w+") as outpic:
            # m4 pgf.m4 out.m4 > out.pic
            process = subprocess.run(['m4', 'pgf.m4', 'out.m4'],
                    stdout=outpic, 
                    stderr=subprocess.PIPE,
                    cwd=self.wd)
            self.returncode = process.returncode
            self.stderr = process.stderr.decode()
            print(f'm4 exit status:{self.returncode}')
            print(f'm4 stderr:{self.stderr}')

    def toRAWTeX(self):
        # dpic -g out.pic > out.tex
        process2 = subprocess.run(['dpic', '-g', 'out.pic'],
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                cwd=self.wd)
        self.returncode = process2.returncode
        self.stderr = process2.stderr.decode()
        print(f'dpic exit status:{self.returncode}')
        print(f'dpic stderr:{self.stderr}')  

        self.TeXoutput = process2.stdout.decode()

    def latexMaker(self):
        # create document
        doc = Document()
        doc.packages.append(Package('tikz'))
        doc.append(NoEscape(self.TeXoutput))
        doc.generate_pdf('out', clean_tex=False)

    def create_new_preview(self):
        # Update PDF Preview
        self.model.get_document().load("file:"+self.wd+"/out.pdf")
        self.view.reload()

    def on_save_clicked(self, widget):
        self.text2m4()
        self.toPic()
        if(self.returncode != 0):
            print("FAILED M4")
            return
        self.toRAWTeX()
        if(self.returncode != 0):
            print("FAILED DPIC")
            return
        self.latexMaker()
        self.create_new_preview()
        print("Done!")


window = Paned()
window.show_all()

Gtk.main()