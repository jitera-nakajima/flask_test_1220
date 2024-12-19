from datetime import datetime
from models.subscription import Subscription

# SubscriptionServiceを定義します
class SubscriptionService:
    def create_subscription(self, email: str, industry: str) -> Subscription:
        # 現在の日時を取得して購読を作成します
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        created_at = updated_at = current_time
        return Subscription(email, industry, created_at, updated_at)
