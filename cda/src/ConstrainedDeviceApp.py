#!/usr/bin/env python3
"""
Constrained Device Application (CDA) - Main Application
PIOT-CDA-02-001: CDA main application template
"""

import logging
import time
import sys
import os

# Add the labs directory to the Python path
sys.path.append(os.path.dirname(__file__))

from labs.common import ConfigUtil
from labs.module02 import SystemPerformanceManager

class ConstrainedDeviceApp:
    """
    Main application class for the Constrained Device App
    """
    
    def __init__(self):
        """
        Initialize the CDA application
        """
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.info("Initializing CDA...")
        
        self.config = ConfigUtil.ConfigUtil()
        self.sysPerfManager = None
        
    def start(self):
        """
        Start the CDA application
        """
        self.logger.info("Starting CDA...")
        
        # Initialize System Performance Manager
        self.sysPerfManager = SystemPerformanceManager.SystemPerformanceManager()
        
        # Start system performance monitoring
        self.sysPerfManager.startManager()
        
        self.logger.info("CDA started successfully.")
        
    def stop(self):
        """
        Stop the CDA application
        """
        self.logger.info("Stopping CDA...")
        
        if self.sysPerfManager:
            self.sysPerfManager.stopManager()
            
        self.logger.info("CDA stopped successfully.")

def main():
    """
    Main function to run the CDA
    """
    # Create and start the application
    app = ConstrainedDeviceApp()
    
    try:
        app.start()
        
        # Keep the application running
        app.logger.info("CDA running. Press Ctrl+C to stop.")
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        app.logger.info("Ctrl+C received. Shutting down...")
    except Exception as e:
        app.logger.error("Error in CDA: %s", e)
    finally:
        app.stop()

if __name__ == "__main__":
    main()