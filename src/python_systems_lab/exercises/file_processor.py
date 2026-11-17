from pathlib import Path
import logging

from python_systems_lab.exercises.file_reader import read_text_file

logger = logging.getLogger(__name__)

def process_text_file(path: Path) -> int:
    filename = path.name
    logger.info('Attempting to read file: %s', filename)

    contents = read_text_file(path)
    characters = len(contents)

    logger.info('Successfully read file: %s', filename)
    logger.info('Character Count: %s', characters)

    return characters