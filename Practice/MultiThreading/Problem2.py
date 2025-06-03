import threading
import time 

class myThread(threading.Thread):
    def run(self):
        print(f"Started {self.name}")
        time.sleep(2)
        print(f"ending {self.name}")

a = myThread(name = "Hassan")
a.start()
a.join()
print("Main Finished")