from unittest.mock import Mock
from payment import PaymentGateway, OrderProcessor

def test_order_processing():
    fake_gateway = Mock()
    fake_gateway.charge.return_value = "SUCCESS-12345"
    
    processor = OrderProcessor(fake_gateway)
    result = processor.process_order(100)
    assert result == "Order processed: SUCCESS-12345"