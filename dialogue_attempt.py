# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:31:42 2019

@author: Vovan-i-Venera
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
'''
from example:
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
'''
from Thetta_Estimation import thetta_Estimation, drop_numerical_outliers
from Thetta_Estimation_GUI_3 import Ui_Thetta_Main_Window
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QApplication, QAction, QFileDialog
from PyQt5.QtCore import QSize 
#from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import pandas as pd
import scipy
import random
import gc

class Dialogue_GUI(QtWidgets.QMainWindow,Ui_Thetta_Main_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.f_choose_button.clicked.connect(self.tell_us)
        self.filenames = set()
        self.manual_radiobutton.toggled.connect(lambda:self.btnstate(self.manual_radiobutton))
    def btnstate(self,button):
         if button.isChecked() == True:
            print("manual input was selected")
            self.min_val = int(self.min_inp_val.toPlainText())
            self.max_val = int(self.max_inp_val.toPlainText())
            self.min_seq_len = int(self.starting_quantity.toPlainText())
            self.number_of_tests = int(self.n_tests_input.toPlainText())
            self.multiplier = float(self.quantity_multiplier.toPlainText())
            self.repeatings = int(self.n_repeating_input.toPlainText())
            self.timelimit = int(self.time_limit_input.toPlainText())#renamed from time_limit to time_limit_input
            print(
                  '\nself.min_val =', int(self.min_inp_val.toPlainText()),
                  '\nself.max_val =', int(self.max_inp_val.toPlainText()),
                  '\nself.min_seq_len =', int(self.starting_quantity.toPlainText()),
                  '\nself.number_of_tests =', int(self.n_tests_input.toPlainText()),
                  '\nself.multiplier =', float(self.quantity_multiplier.toPlainText()),
                  '\nself.repeatings =', int(self.n_repeating_input.toPlainText()),
                  '\nself.timelimit =', int(self.time_limit_input.toPlainText())
                  )
         else:
            print("preset values will be used")
    def tell_us(self):
        #не нужный метод!
        print("the button has been clicked")
        filename = QFileDialog.getOpenFileName()[0]
        print(filename, "has been acquired")
        try:
            self.filenames.add(filename)
        except AttributeError:
            self.filenames = {filename}
        finally:
            print(self.filenames)
        #self.menuChoose_Files.menuAction()
        return
    def tell_us_2(self):
        #не нужныйй метод!!!
        print("entering file menubar")
        return
    
class Dialogue_with_Estimation(Dialogue_GUI,thetta_Estimation):
    def __init__(self):
        super().__init__()
        #self.setupUi(self)
        self.start_button.clicked.connect(self.start_estimation)
        #default settings:
        self.min_seq_len = 5
        self.number_of_tests = 20
        self.multiplier = 2
        self.repeatings = 3
        self.max_val = 1_000_000
        self.min_val = 0
        self.manual_radiobutton.toggled.connect(lambda:self.btnstate(self.manual_radiobutton))
        self.timelimit = 10
    def start_estimation(self):
        self.btnstate(self.manual_radiobutton)
        self.acquire_subprocess_filenames()
        self.generate_estim_sequences(min_seq_len = self.min_seq_len, lowest = self.min_val, 
                                      highest = self.max_val, number_of_tests = self.number_of_tests,
                                      multiplier = self.multiplier,repeatings = self.repeatings)
        self.run_estimations()
        #self.plot_results()
        
    def acquire_subprocess_filenames(self):
        self.subp_filenames = list(self.filenames)
        print("acquired_filenames",self.subp_filenames)
        
    def run_estimations(self):
        self.estimation_results = []
        
        for txt_estim_sequence in self.estim_sequences_iterator():
            print("new sequence started")
            for subp_filename in self.subp_filenames:
                self.estimation_results.append(self.estimate(txt_estim_sequence,subp_filename,self.timelimit))#TIMEOUT HOW TO ADD TIMEOUT????
                #self.estimation_results.append(estimate(estim_sequence,subp_filename,timeout=timeout))
            self.estimation_results_DF = pd.DataFrame(self.estimation_results) 
            self.estimation_results_DF.columns = ['filename','lenseq','time','memory']
            #drop_numerical_outliers(self.estimation_results_DF)
            gc.collect()
        self.plot_results()
    
    def plot_results(self):
        self.graphicsView = pg.PlotWidget()
        self.graphicsView.setLabel('left','Time','Seconds')
        self.graphicsView.setLabel('bottom','sequence_length')
        self.graphicsView.setBackground('w')
        self.setCentralWidget(self.graphicsView)
        for number,current_subp_filename in enumerate(self.subp_filenames):
            color_tuple= (random.randint(0,256), random.randint(0,256), random.randint(0,256))
            #pen = pg.mkPen(number,len(self.subp_filenames),width = 7)
            
            corresponding_part_of_df = self.estimation_results_DF[self.estimation_results_DF['filename'] == current_subp_filename]
            lengths_seqs = list(corresponding_part_of_df['lenseq'])
            times_seqs = list(corresponding_part_of_df['time'])
            self.graphicsView.plot(lengths_seqs,times_seqs,name=current_subp_filename,
                                   pen=None, symbol = 'o', symbolBrush = color_tuple)
            self.graphicsView.addLegend()
        self.memoryView = pg.plot()
        self.memoryView.setLabel('left','Memory','bytes')
        self.memoryView.setLabel('bottom','sequence_length')
        for number,current_subp_filename in enumerate(self.subp_filenames):
            color_tuple= (random.randint(0,256), random.randint(0,256), random.randint(0,256))
            #pen = pg.mkPen(number,len(self.subp_filenames),width = 7)
            
            corresponding_part_of_df = self.estimation_results_DF[self.estimation_results_DF['filename'] == current_subp_filename]
            lengths_seqs = list(corresponding_part_of_df['lenseq'])
            mem_seqs = list(corresponding_part_of_df['memory'])
            self.memoryView.plot(lengths_seqs,mem_seqs,name=current_subp_filename,
                                   pen=None, symbol = 'o', symbolBrush = color_tuple)
            self.memoryView.addLegend()
  

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    #window = preoperating_GUI()  # Это только длля проверки интерфейса, чтобы убедиться что нормально собирает ввод
    window = Dialogue_with_Estimation()
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение