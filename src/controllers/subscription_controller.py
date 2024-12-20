from flask import request, jsonify
from src.services.subscription_service import SubscriptionService

# SubscriptionControllerを定義します
class SubscriptionController:
    def __init__(self):
        self.service = SubscriptionService()

    def create(self):
        # リクエストからデータを取得し、購読を作成します
        print("Inside SubscriptionController.create()")  # デバッグ用のログ
        email = request.json.get('email')
        industry = request.json.get('industry')
        print(f"Email: {email}, Industry: {industry}")  # デバッグ用のログ
        subscription = self.service.create_subscription(email, industry)
        return jsonify({
            'email': subscription.email,
            'industry': subscription.industry,
            'created_at': subscription.created_at,
            'updated_at': subscription.updated_at
        })
