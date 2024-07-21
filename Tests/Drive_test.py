import pytest
from pytest_mock import mocker
from Scripts.DriveMounting import Drive

def test_addExt4Entry_appendsFstabEntryToFstab(mocker):
    