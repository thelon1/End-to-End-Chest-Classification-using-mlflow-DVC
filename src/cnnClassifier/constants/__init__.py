'''

In constant we are reading two files:
# 1. config.yaml: This file contains the configuration settings for the project, such as
# 2. params.yaml: This file contains the parameters for the model training, such as learning rate, batch size, etc.

# These two files are wont be changing frequently, so we can read them once and use them throughout the project.

'''

from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")