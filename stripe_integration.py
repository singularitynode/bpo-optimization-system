class StripeIntegration:
    def __init__(self):
        self.prices = {
            'pro_monthly': 9900,  # $99 in cents
            'pro_yearly': 94800,   # $948 (20% discount)
        }
    
    def create_checkout_session(self, tier, customer_email):
        """Simulate Stripe checkout"""
        import uuid
        return {
            'session_id': str(uuid.uuid4()),
            'tier': tier,
            'price': self.prices.get(tier, 0),
            'customer_email': customer_email,
            'checkout_url': f"https://checkout.stripe.com/simulated/{uuid.uuid4()}",
            'status': 'created'
        }
    
    def create_subscription(self, tier, customer_info):
        """Simulate subscription creation"""
        return {
            'subscription_id': f"sub_{uuid.uuid4().hex[:12]}",
            'tier': tier,
            'status': 'active',
            'current_period_end': '2024-12-31',
            'customer': customer_info
        }