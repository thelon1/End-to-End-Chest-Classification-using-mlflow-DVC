from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataInjectionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config["artifacts_roots"]])

    def get_data_ingestion_config(self) -> DataInjectionConfig:
        config = self.config["data_ingestion"]  # Make sure this is a dict

        create_directories([config["root_dir"]])  # Create data ingestion folder

        data_ingestion_config = DataInjectionConfig(
            root_dir = config["root_dir"],
            source_url = config["source_url"],
            local_data_file = config["local_data_file"],
            unzip_dir = config["unzip_dir"]
        )

        return data_ingestion_config