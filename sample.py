import stripe
stripe.api_key = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

stripe.api_key = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"

stripe.Charge.create(
  amount=2000,
  currency="usd",
  source="tok_amex", # obtained with Stripe.js
  description="Charge for jenny.rosen@example.com"
)
