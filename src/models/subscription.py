# Subscriptionモデルを定義します
class Subscription:
    def __init__(self, email: str, industry: str, created_at: str, updated_at: str):
        self.email = email
        self.industry = industry
        self.created_at = created_at
        self.updated_at = updated_at
