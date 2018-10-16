import threading

class ThreadingClass(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print(self.name + " <-- Printed using thread")

thread = ThreadingClass("Tejas")
thread.start()
