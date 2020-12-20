import pytest
from arma_class_parser.extraction.cfg_processing import ConfigDataHolder
from gidtools.gidfiles import pathmaker, readbin, readit, loadjson
import hashlib
import os

THIS_FILE_DIR = os.path.abspath(os.path.dirname(__file__))


def test_base_attributes(cfg_holder, example_config_filepath):
    assert cfg_holder.config_file == example_config_filepath
    assert cfg_holder.hash == hashlib.md5(bytes(readit(example_config_filepath), 'utf-8')).hexdigest()
    assert cfg_holder.raw_content == readit(example_config_filepath)
    assert len(cfg_holder.cfg_names) == len(cfg_holder.cfg_pairs)
    assert cfg_holder.cfg_names == loadjson(pathmaker(THIS_FILE_DIR, "example_cfg_names.json"))
    assert cfg_holder.cfg_pairs == list(map(tuple, loadjson(pathmaker(THIS_FILE_DIR, "example_cfg_pairs.json"))))


def test_serialize(cfg_holder, example_config_filepath):
    assert os.path.exists('config_data_holder.pkl') is True
    cfg_holder = ConfigDataHolder.unserialize()
    assert cfg_holder.config_file == example_config_filepath
    assert cfg_holder.hash == hashlib.md5(bytes(readit(example_config_filepath), 'utf-8')).hexdigest()
    assert cfg_holder.raw_content == readit(example_config_filepath)
    assert len(cfg_holder.cfg_names) == len(cfg_holder.cfg_pairs)
    assert cfg_holder.cfg_names == loadjson(pathmaker(THIS_FILE_DIR, "example_cfg_names.json"))
    assert cfg_holder.cfg_pairs == list(map(tuple, loadjson(pathmaker(THIS_FILE_DIR, "example_cfg_pairs.json"))))
    if os.path.exists('config_data_holder.pkl'):
        os.remove('config_data_holder.pkl')
