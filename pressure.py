import gpiod
import time
import threading
LED_PIN = 18
chip = gpiod.Chip('gpiochip4')
led_line = chip.get_line(LED_PIN)
led_line.request(consumer="LED", type=gpiod.LINE_REQ_DIR_OUT)
pwm_time = 0.002
duty_cycle=0.2
set_pres = 150.0
curr_pres = 0.0

Kp=0.01
Ki=0.0001
Kd=0.001

def pwm_gen():
    global pwm_time, duty_cycle
    on_time = duty_cycle*pwm_time
    off_time= pwm_time - on_time
    
    try:
       while True:
           on_time = duty_cycle*pwm_time
           off_time= pwm_time - on_time
           led_line.set_value(1)
           time.sleep(on_time)
           led_line.set_value(0)
           time.sleep(off_time)
    finally:
       led_line.release()
       
def get_curr():
    global curr_pres
    curr_pres_int = 0.0
    while True:
        try:
            curr_pres_int = float(input())
            time.sleep(0.5)
            if(curr_pres_int>=0.0):
                curr_pres=curr_pres_int
        
        except:
            continue
        
def det_duty():
    global duty_cycle, set_pres, curr_pres, Kp,Ki,Kd
    
    err=0.0
    prev_err=0.0
    int_err = 0.0
    chng_err = 0.0
    duty_cycle_int = 0.0 
    
    while True:
        err= set_pres-curr_pres
        chng_err = err-prev_err
        prev_err = err
        
        if (((int_err> 300) and (err>0)) or ((int_err< -300) and (err<0))):
            int_err = int_err
        else:
            int_err = int_err + err
            
        
        duty_cycle_int = err*Kp + int_err*Ki + chng_err*Kd
        
        if err == 0.0:
            int_err = 0.0
            
        
        
        if duty_cycle_int>1.0:
            duty_cycle = 1.0
        elif duty_cycle_int<0.0:
            duty_cycle = 0.0
        else:
            duty_cycle = duty_cycle_int
            
        print("Current Pressure = ",curr_pres, "Setpoint_Pressure = ", set_pres )
        time.sleep(0.02)
            
        

if __name__ =="__main__":
    t1 = threading.Thread(target=pwm_gen)
    t2 = threading.Thread(target=det_duty)
    t3 = threading.Thread(target=get_curr)
 
    t1.start()
    t2.start()
    t3.start()
 
    t1.join()
    t2.join()
    t3.join()
 
    print("Done!")
