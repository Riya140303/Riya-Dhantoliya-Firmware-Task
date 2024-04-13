import serial
import time
count = 0
ser = serial.Serial('COM13', 2400) 

def calculate_speed(start_time, bytes_transferred):
    end_time = time.time()
    elapsed_time = end_time - start_time
    try:
        speed = (bytes_transferred * 8) / elapsed_time  # Calculate speed in bits per second    
    except:
        speed = 0
    return speed

text_data = "Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one. In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs, Rajan said in the note. Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently."
bytes_transferred = 0
start_time = time.time()

for byte in text_data.encode():
    ser.write(byte.to_bytes(1, byteorder='big'))
    bytes_transferred += 1
    current_time = time.time()
    speed = calculate_speed(start_time, bytes_transferred)
    print(f"Transmitting to MCU... Speed: {speed} bits/second", end='\r')

time.sleep(2)

while True:
    if ser.in_waiting > 0:
        byte = ser.read(1)
        count += 1
        print(byte)
        print(count)
        if(byte==b'\xff'):
            break

ser.close()