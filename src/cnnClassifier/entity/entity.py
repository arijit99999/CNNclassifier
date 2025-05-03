from pathlib import Path
from dataclasses import dataclass

@dataclass
class DataIngesion:
    root_dir: Path  #under artifacts i created data ingestion folder
    source_URL: str  #donload url
    local_data_file: Path  #output=data.zip
    unzip_dir: Path #unzip in data ingestion folder