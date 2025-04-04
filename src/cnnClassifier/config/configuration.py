from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml,create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_filepath: str = CONFIG_FILE_PATH,
                 params_filepath: str = PARAMS_FILE_PATH):
        # Read configuration and parameters from the YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create required directories for artifacts
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Read the data_ingestion section from the configuration
        config = self.config.data_ingestion

        # Create required directories for data ingestion
        create_directories([config.root_dir])

        # Create a DataIngestionConfig object with the required values
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config