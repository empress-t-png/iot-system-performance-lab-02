import sys
import os

# Add the system directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'system'))

from SystemPerformanceManager import SystemPerformanceManager

class ConstrainedDeviceApp:
    def __init__(self):
        print("Initializing CDA...")
        self.sysPerfManager = SystemPerformanceManager(pollRate=5)
        
    def startApp(self):
        print("Starting CDA...")
        self.sysPerfManager.startManager()
        
    def stopApp(self):
        print("Stopping CDA...")
        self.sysPerfManager.stopManager()

if __name__ == '__main__':
    app = ConstrainedDeviceApp()
    
    try:
        app.startApp()
        
        # Keep running for 30 seconds to see data
        import time
        time.sleep(30)
        
    except KeyboardInterrupt:
        print("\nReceived interrupt signal...")
    finally:
        app.stopApp()
        print("CDA application stopped.")