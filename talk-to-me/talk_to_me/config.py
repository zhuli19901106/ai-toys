import configparser
import json
from pathlib import Path
from typing import List, Optional

class Config:
    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        if not self.config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
       

        self.config = configparser.ConfigParser()
        self.config.read(config_path)
        self._validate_config()

    def _validate_config(self):
        required_sections = ['server', 'app', 'cors']
        for section in required_sections:
            if section not in self.config:
                raise ValueError(f"Missing required section in config: {section}")

    @property
    def server_host(self) -> str:
        return self.config['server']['host']

    @property
    def server_port(self) -> int:
        return int(self.config['server']['port'])

    @property
    def app_title(self) -> str:
        return self.config['app']['title']

    @property
    def app_description(self) -> str:
        return self.config['app']['description']

    @property
    def app_version(self) -> str:
        return self.config['app']['version']

    @property
    def cors_allow_origins(self) -> List[str]:
        return json.loads(self.config['cors']['allow_origins'])

    @property
    def cors_allow_credentials(self) -> bool:
        return self.config['cors'].getboolean('allow_credentials')

    @property
    def cors_allow_methods(self) -> List[str]:
        return json.loads(self.config['cors']['allow_methods'])

    @property
    def cors_allow_headers(self) -> List[str]:
        return json.loads(self.config['cors']['allow_headers'])

# Global config instance
config: Optional[Config] = None

def load_config(config_path: str) -> Config:
    global config
    config = Config(config_path)
    return config

def get_config() -> Config:
    if config is None:
        raise RuntimeError("Configuration not loaded. Call load_config() first.")
    return config
