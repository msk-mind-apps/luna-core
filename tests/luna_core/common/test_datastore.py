import os
import pytest

from luna_core.common.DataStore import DataStore_v2

@pytest.fixture()
def datastore2():
    os.environ['LUNA_HOME'] = 'tests/luna_core/common/testdata/'
    datastore2 = DataStore_v2('tests/luna_core/common/testdata/store')
    yield datastore2

def test_datastore_v2_init():
    os.environ['LUNA_HOME'] = ''
    with pytest.raises(RuntimeError):
        DataStore_v2('tests/luna_core/common/testdata/store')
