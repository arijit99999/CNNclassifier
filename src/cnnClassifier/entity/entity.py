from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngesion:
    root_dir: Path  #under artifacts i created data ingestion folder
    source_URL: str  #donload url
    local_data_file: Path  #output=data.zip
    unzip_dir: Path #unzip in data ingestion folder


    #2nd upgrade this enitity.py file for data ingesion
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PrepareBaseModel:
    root_dir: Path
    base_model_path: Path         
    updated_base_model_path: Path
    params_include_top: bool
    params_weights: str
#3rd step for base model