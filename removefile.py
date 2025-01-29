import time, subprocess

def remove():
    time.sleep(20)
    processo = subprocess.call(["rm *.mp3"], shell=True)