## It is the mode frequent function that is used in the project or in the code

import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its contents as a ConfigBox.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: Any other error encountered while reading the file.

    Returns:
        ConfigBox: A ConfigBox containing the data from the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty.")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of paths of directories to create.
        verbose (bool, optional): Flag to log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Save data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file.

    Returns:
        ConfigBox: Data as class attributes instead of a dictionary.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary data to a file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary data from a file.

    Args:
        path (Path): Path to the binary file.

    Returns:
        Any: The object stored in the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Get the size of a file in KB.

    Args:
        path (Path): Path to the file.

    Returns:
        str: File size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"

def decode_image(img_string, filename):
    """Decode a base64 image string and save it as a file.

    Args:
        img_string (str): Base64 encoded image string.
        filename (str): Path where the image will be saved.
    """
    img_data = base64.b64decode(img_string)
    with open(filename, 'wb') as f:
        f.write(img_data)
    logger.info(f"Image decoded and saved to: {filename}")

def encode_image_to_base64(cropped_image_path: str) -> str:
    """Encode an image file to a base64 string.

    Args:
        cropped_image_path (str): Path to the image file.

    Returns:
        str: The base64 encoded image string.
    """
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
