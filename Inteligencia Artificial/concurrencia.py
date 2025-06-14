import threading
import time

def process_request(request_id):
    print(f"Processing request {request_id}")
    time.sleep(3)
    print(f"Finished processing request {request_id}")
    
threads = []

for i in range(3):
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All requests are processed")