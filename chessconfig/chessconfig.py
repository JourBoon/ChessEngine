import yaml
import os
from utils import logger

class ChessConfig:

    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def createFile(self):
        file_path = os.path.join('chessconfig', 'configs', f'{self.file_name}.chessconfig')

        if os.path.exists(file_path):
            # Le fichier existe, alors on le lit
            log = logger.Logger()
            logLevel = logger.LogLevel
            log.log("Reading existing config file...", logLevel.INFO)
            with open(file_path, 'r') as file:
                config_data = yaml.load(file, Loader=yaml.FullLoader)
            return config_data
        else:
            # Le fichier n'existe pas, alors on le crée
            config_data = {
                'ia_name': 'Alice',
                'difficulty_level': 'medium',
                'board_size': {
                    'rows': 8,
                    'columns': 8
                }
            }

            log = logger.Logger()
            logLevel = logger.LogLevel
            log.log("Creating new config file...", logLevel.INFO)
            with open(file_path, 'w') as file:
                yaml.dump(config_data, file, default_flow_style=False)

            print(f"Les configurations ont été écrites dans {file_path}")
            return config_data
