#!/usr/bin/env python3

import os
import sys

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(
    os.path.abspath(os.path.join(THIS_DIR, '../src/')))

import load_data

def test_get_db_config():
    config = load_data.get_db_config('--db=test')

    assert config['dbname'] == 'test'
