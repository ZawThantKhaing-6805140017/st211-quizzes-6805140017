class PaymentGateway:
    def charge(self, amount):
        raise NotImplementedError("Real gateways not available in testing.")

class OrderProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_order(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        result = self.payment_gateway.charge(amount)
        return f"Order processed: {result}"