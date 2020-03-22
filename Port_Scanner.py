import socket
from datetime import datetime
import threading
from queue import Queue

# Prevent duplicate entries
print_lock = threading.Lock()
# Enter a host to scan.
host = input("Enter a victim (Host name or ip address e.g. www.wikipedia.com or 198.35.26.98): ")
ip = socket.gethostbyname(host)  # Translate host name to ipv4

f = open("results.txt", 'w')
print("       Please wait, Scanning The Victim........ -> ", ip, file=f)
f.close()

print("-" * 70)
print("      Please wait, Scanning The Victim........ -> ", ip)
print("-" * 70)

# starting time
t1 = datetime.now()
f = open("results.txt", 'a')
print("\nStart date and time: ",t1, file=f)
print("\nStart date and time: ",t1)
f.close()

# Port scan
def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create sock stream
        result = sock.connect_ex((ip,port))
        if result == 0:
            f = open("results.txt", 'a')
            print("\n Port %d is Open <--------------------------------------------------X\n" % port, file=f) #if socket is listening it will print the port
            f.close()
            print("\n Port %d is Open <--------------------------------------------------X\n" % port)
            sock.close()
        else:
            print("\n Port %d is Closed :( " % port)
    except:
        pass

# Threader function
def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()

q = Queue()

for x in range(99):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1,1025):
    q.put(worker)

q.join()


t2 = datetime.now() # end of execution time
total = t2 - t1

f = open("results.txt", 'a')
print("\nEnd date and time: ", t2, file=f)
print("\nTotal Scanning Time: ", total, file=f)
f.close()
print("\nTotal Scanning Time: ", total)