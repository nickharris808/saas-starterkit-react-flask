import stripe
from flask import jsonify, request
from src.utils.config import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def create_customer():
    """
    Create a new customer in Stripe.
    
    Returns:
        dict: A dictionary containing the customer ID and status.
    """
    try:
        customer = stripe.Customer.create(
            email=request.json.get('email'),
            source=request.json.get('source')  # This is the token from the frontend
        )
        return jsonify({"customer_id": customer.id, "status": "success"}), 201
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400

def create_subscription():
    """
    Create a new subscription for a customer.
    
    Returns:
        dict: A dictionary containing the subscription details and status.
    """
    try:
        subscription = stripe.Subscription.create(
            customer=request.json.get('customer_id'),
            items=[{'price': request.json.get('price_id')}],
        )
        return jsonify({
            "subscription_id": subscription.id,
            "status": subscription.status,
            "current_period_end": subscription.current_period_end
        }), 201
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400

def update_subscription():
    """
    Update an existing subscription.
    
    Returns:
        dict: A dictionary containing the updated subscription details and status.
    """
    try:
        subscription = stripe.Subscription.modify(
            request.json.get('subscription_id'),
            items=[{'price': request.json.get('new_price_id')}],
        )
        return jsonify({
            "subscription_id": subscription.id,
            "status": subscription.status,
            "current_period_end": subscription.current_period_end
        }), 200
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400

def cancel_subscription():
    """
    Cancel an existing subscription.
    
    Returns:
        dict: A dictionary containing the cancellation status.
    """
    try:
        subscription = stripe.Subscription.delete(
            request.json.get('subscription_id')
        )
        return jsonify({"status": "cancelled", "subscription_id": subscription.id}), 200
    except stripe.error.StripeError as e:
        return jsonify({"error": str(e)}), 400

def handle_webhook():
    """
    Handle Stripe webhooks for events like 'payment_succeeded' or 'payment_failed'.
    
    Returns:
        dict: A dictionary containing the webhook handling status.
    """
    payload = request.data
    sig_header = request.headers.get('Stripe-Signature')

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        return jsonify({"error": "Invalid payload"}), 400
    except stripe.error.SignatureVerificationError as e:
        return jsonify({"error": "Invalid signature"}), 400

    if event['type'] == 'payment_intent.succeeded':
        # Handle successful payment
        pass
    elif event['type'] == 'payment_intent.payment_failed':
        # Handle failed payment
        pass

    return jsonify({"status": "success"}), 200

async def get_all_billing_info():
    billing_info = await BillingInfo.all().prefetch_related('user')
    return [
        {
            "id": info.id,
            "user": info.user.email,
            "amount": info.amount,
            "date": info.date
        }
        for info in billing_info
    ]