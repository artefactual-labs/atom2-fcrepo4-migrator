#!/usr/bin/env python3

import load_data


def test_get_db_config():
    config = load_data.get_db_config('--db=test')

    assert config['dbname'] == 'test'
