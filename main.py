import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from cnnClassifier import logger
from cnnClassifier.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx ===============x")
except Exception as e:
    logger.info(f"Error {e}")

