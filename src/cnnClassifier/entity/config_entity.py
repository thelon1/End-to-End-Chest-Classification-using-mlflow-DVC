from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataInjectionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path