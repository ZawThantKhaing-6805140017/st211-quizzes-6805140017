from unittest.mock import Mock

def test_mock_returns_configured_value():
    mock = Mock()
    mock.next_id.side_effect = [1, 2, 3]
    
    assert mock.next_id() == 1
    assert mock.next_id() == 2
    assert mock.next_id() == 3