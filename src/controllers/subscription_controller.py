from flask import request, jsonify
from services.subscription_service import SubscriptionService

# SubscriptionControllerを定義します
class SubscriptionController:
    def __init__(self):
        self.service = SubscriptionService()

    def create(self):
        # リクエストからデータを取得し、購読を作成します
        email = request.json.get('email')
        industry = request.json.get('industry')
        subscription = self.service.create_subscription(email, industry)
        return jsonify({
            'email': subscription.email,
            'industry': subscription.industry,
            'created_at': subscription.created_at,
            'updated_at': subscription.updated_at
        })
