# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:15:59 2019

@author: Vovan-i-Venera
"""

import subprocess
import pstats
import cProfile
import random
import tracemalloc
import seaborn as sns
import pandas as pd
import matplotlib as plt
import scipy
import numpy as np
import timeit
import psutil
import time
import threading
import gc

Sequence_for_Estimation = ""
SubProcess_Filename = ""
SubProc = None

def drop_numerical_outliers(df, z_thresh=3):
    # Constrains will contain `True` or `False` depending on if it is a value below the threshold.
    constrains = df.select_dtypes(include=[np.number]) \
        .apply(lambda x: np.abs(scipy.stats.zscore(x)) < z_thresh, reduce=False) \
        .all(axis=1)
    # Drop (inplace) values set to be rejected
    df.drop(df.index[~constrains], inplace=True)

class memory_Time_Diagnostics():
    """
    класс в котором будут ТОЛЬКО методы для диагностики потребления памяти итд
    """
    def estimate(self,txt_estim_sequence,subp_filename,timeout = None):#TIMEOUT???
        if not timeout:
            timeout = 6.66
        gc.collect()
        with psutil.Popen(["python", subp_filename], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, shell = True) as process:#TIMEOUT???
            
            
            diagnosed_thread = threading.Thread(target = process.communicate, kwargs = {'input':bytes(txt_estim_sequence,'UTF-8')})
            diagnosed_thread.start()
            memories_vms = []
            times_system = []
            poll = process.poll()
            pause = 0.001
            total_time = 0
            
            while process.poll() is None and total_time < timeout:
                try:
                    
                    times_system.append(process.cpu_times().system)#этим пока не научился пользоваться - какую то херню выдаёт)
                    #memories_rss.append(process.memory_info().rss)   
                    memories_vms.append(process.memory_info().rss)
                    time.sleep(pause)
                    total_time += pause
                except psutil.NoSuchProcess:
                    diagnosed_thread.join()
                    break
                
            try:
                process.kill()
            except psutil.NoSuchProcess:
                pass
            gc.collect()
            print(subp_filename,total_time)
            system_time = total_time #если вдуматься то совсем смешной подход)))
            memory = sum(memories_vms)/len(memories_vms)-min(memories_vms) #очень сомнительный ход
            return [subp_filename, len(txt_estim_sequence),system_time,memory]
        
class thetta_Estimation(memory_Time_Diagnostics):
    """
    класс который принимает лимиты для сортируемых последовательностей и имена файлов
    который для них проводит оценки
    и выдаёт график
    """
    def __init__(self, repeatings = 10, custom_inputs = False):
        
        self.custom_input_flag = custom_inputs#когда нибудь сделаю - пока так
    
    def generate_estim_sequences(self, number_of_tests = 10, lowest = 0, highest = 1_000_000, min_seq_len = 10, multiplier = 2, repeatings = 1):
        def estim_sequences_iterator():
            for repeating in range(repeatings):
                for n_testing_sequence in range(number_of_tests):
                    seq_len = int(min_seq_len * multiplier**n_testing_sequence)
                    estim_sequence = [random.randint(lowest,highest) for num in range(seq_len)]
                    txt_estim_sequence = " ".join([str(num) for num in estim_sequence]) + "\n\r"
                    yield txt_estim_sequence
        self.estim_sequences_iterator = estim_sequences_iterator
    
    def acquire_subprocess_filenames(self, *args):
        self.subp_filenames = []
        for subp_filename in args:
            self.subp_filenames.append(subp_filename)
        print("acquired_filenames",self.subp_filenames)
        
    def run_estimations(self, timeout=180):
        self.estimation_results = []
        
        for txt_estim_sequence in self.estim_sequences_iterator():
            print("new sequence started")
            for subp_filename in self.subp_filenames:
                self.estimation_results.append(self.estimate(txt_estim_sequence,subp_filename,timeout))#TIMEOUT HOW TO ADD TIMEOUT????
                #self.estimation_results.append(estimate(estim_sequence,subp_filename,timeout=timeout))
        self.estimation_results_DF = pd.DataFrame(self.estimation_results) 
        self.estimation_results_DF.columns = ['filename','lenseq','time','memory']
        drop_numerical_outliers(self.estimation_results_DF)

    
    def plot_results(self):
        try:
            pairpl.fig.close()
        except: #Нужно ловить эксепшн
            pass
        pairpl = sns.pairplot(self.estimation_results_DF, 
                      x_vars = ["lenseq"], y_vars = ["time","memory"], 
                      height=4, aspect=11.7/8.27,kind = "scatter", hue = "filename")  
        
        
if __name__ == "__main__":
    
    estimator = thetta_Estimation()
    estimator.generate_estim_sequences(min_seq_len = 1, number_of_tests = 8, multiplier = 2,repeatings = 3)
    #estimator.acquire_subprocess_filenames(*[filename for filename in input().split()])
    estimator.acquire_subprocess_filenames(*"subprocquicksort.py subprocsort.py subprocmergesort.py pornsort.py".split()) #убрал subprocbubsort.py из списка поскольку на его фоне не видно разницы в скоростях)
    estimator.run_estimations(timeout = 10)
    estimator.plot_results()
            
        
            
    