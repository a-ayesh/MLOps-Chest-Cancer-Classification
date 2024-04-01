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
    """
    Read a YAML file and return its content as a Box object.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        Box: A Box object containing the content of the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs while reading the YAML file.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'Loaded yaml file: {path_to_yaml}')
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('YAML file is empty')
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories at the specified paths.

    Args:
        path_to_directories (list): A list of paths where directories should be created.
        verbose (bool, optional): If True, logs the path of each created directory. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f'Created directory at: {path}')

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary as a JSON file.

    Args:
        path (Path): The path to save the JSON file.
        data (dict): The dictionary to be saved as JSON.

    Returns:
        None

    Raises:
        None
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'Saved json file at: {path}')

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load a JSON file from the given path and return its content as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file.

    Returns:
        ConfigBox: The content of the JSON file as a ConfigBox object.

    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f'Loaded json file at: {path}')
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save binary data to a file using joblib.

    Args:
        data (Any): The data to be saved.
        path (Path): The path where the binary file will be saved.

    Returns:
        None
    """
    joblib.dump(value=data, filename=path)
    logger.info(f'Saved binary file at: {path}')

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file using joblib.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The content of the binary file.
    """
    data = joblib.load(path)
    logger.info(f'Loaded binary file at: {path}')
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Returns the size of a file in kilobytes.

    Args:
        path (Path): The path to the file.

    Returns:
        str: A string representation of the file size in kilobytes.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f'~{size_in_kb} KB'

def decodeImage(imgString, fileName):
    """
    Decode the given image string and save it as a file.

    Args:
        imgString (str): The base64 encoded image string.
        fileName (str): The name of the file to save the decoded image.

    Returns:
        None
    """
    imgdata = base64.b64decode(imgString)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    """
    Encodes an image file into base64 format.

    Args:
        croppedImagePath (str): The path to the image file.

    Returns:
        str: The base64 encoded string representation of the image.

    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())