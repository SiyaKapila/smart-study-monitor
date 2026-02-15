import time

class StudyMonitor:

    def __init__(self):
        self.start_time = None
    def start(self):
        self.start_time = time.time()
        print("Study session started.")
    def end(self):
        if self.start_time is None:
            print("No session running.")
            return 0

        duration = int(time.time() - self.start_time)
        self.start_time = None

        print("Session ended:", duration, "seconds")
        return duration

