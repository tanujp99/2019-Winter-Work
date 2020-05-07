import os                                                                       
from multiprocessing import Pool                                                
                                                                                
                                                                                
processes = ('1218form.py','newwindow.py')                                    
#other = ('newwindow.py')
#another = ('college.py')
                                                  
                                                                                
def run_process(process):                                                             
    os.system('python {}'.format(process))                                       
                                                                                
                                                                                
pool = Pool(processes=2)                                                        
pool.map(run_process, processes) 
#pool.map(run_process, other) 
#pool.map(run_process, another) 