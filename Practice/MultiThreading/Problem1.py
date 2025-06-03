import  threading
import time

def task():
   print(f"thread {threading.current_thread().name} is starting") 
   time.sleep(2)
   print(f"thread {threading.current_thread().name} is finishing")

threads = []
for i in range(5):
    thread = threading.Thread(target=task, name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("All threads have finished execution.")

