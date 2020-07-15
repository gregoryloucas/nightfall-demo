import stripe
stripe.api_key = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

auth_token = 'dbd1b2a5bd84476280caaff641f9d209'

stripe.Charge.create(
  amount=2000,
  currency="usd",
  source="tok_amex", # obtained with Stripe.js
  description="Charge for jenny.rosen@example.com"
)
