"""
Configuration Utility for CDA
PIOT-CDA-02-001: Configuration setup
"""

import json
import os

class ConfigUtil:
    """
    Configuration utility class
    """
    
    def __init__(self, config_file = "config/CDA_Config.json"):
        """
        Initialize configuration
        """
        self.config = {}
        self.config_file = config_file
        self.load_config()
        
    def load_config(self):
        """
        Load configuration from file
        """
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                # Default configuration
                self.config = {
                    "systemPerformance": {
                        "pollCycleSecs": 10,
                        "enableSystemPerformance": True
                    }
                }
        except Exception as e:
            print(f"Error loading config: {e}")
            self.config = {}
    
    def getValue(self, section, key):
        """
        Get configuration value
        """
        try:
            return self.config.get(section, {}).get(key)
        except:
            return None
    
    def hasSection(self, section):
        """
        Check if section exists
        """
        return section in self.config