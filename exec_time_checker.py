# python_exe_time_checker

import os
import time

def exe_time_starter():
    tic = time.time()
    
    return tic

def exec_time_checker(init_tic):
    exec_time = time.time() - init_tic

    if(exec_time >= 60): # more than 1 min
        min_time = int(exec_time/60)
        sec = exec_time % 60
        sec_detail = exec_time - (60*min_time)

        print("Execution Time: %d min %d sec" %(min_time, sec))
        print("Details %f " %(sec_detail))
    else:
        sec = exec_time
        sec_detail = exec_time

        print("Execution Time: %d sec" %(sec))
        print("Details %f " %(sec_detail))

    if(exec_time < 60): # more than 1 min
        sec = exec_time
        sec_detail = exec_time

        print("Execution Time: %d sec" %(sec))
        print("Details %f " %(sec_detail))
    else:
        min_time = int(exec_time/60)
        sec = exec_time % 60
        sec_detail = exec_time - (60*min_time)

        print("Execution Time: %d min %d sec" %(min_time, sec))
        print("Details %f " %(sec_detail))


if __name__=="__main__":
    tic = exe_time_starter()

    time.sleep(10)

    exec_time_checker(tic)
