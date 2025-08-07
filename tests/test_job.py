# tests/test_job.py
from etl.job import transform

def test_transform():
    assert transform([1, 2]) == [2, 4]
