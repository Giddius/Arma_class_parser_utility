import pytest
import lzma
from zipfile import ZipFile, ZIP_LZMA
from gidtools.gidfiles import pathmaker
import os
from tempfile import TemporaryDirectory
from arma_class_parser.extraction.cfg_processing import ConfigDataHolder
THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope='session')
def example_config_filepath():
    with TemporaryDirectory() as tempdir:
        with ZipFile(pathmaker(THIS_FILE_DIR, 'example_config.zip'), mode='r', compression=ZIP_LZMA) as zippy:
            config_path = zippy.extract("example_config.cpp", path=tempdir)
        yield config_path


@pytest.fixture(scope='session')
def cfg_holder(example_config_filepath):
    holder = ConfigDataHolder(example_config_filepath)
    yield holder
