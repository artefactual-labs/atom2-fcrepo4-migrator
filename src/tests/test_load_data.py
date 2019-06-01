#!/usr/bin/env python3

import os
import load_data


def test_parse_args():
    assert load_data.parse_args(['--db', os.environ.get('DB_NAME')]) == 'test'
