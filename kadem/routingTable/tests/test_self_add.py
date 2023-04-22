import routingTable.routingTable as rt
from routingTable.selfAddException import SelfAddException

import pytest

def test_self_add():
    table = rt.RoutingTable(0,3)
    with pytest.raises(SelfAddException) as e:
        table.insertNewNode(0)
    assert True