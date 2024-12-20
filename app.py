from flask import Flask
from config import Config
from src.controllers.subscription_controller import SubscriptionController


app = Flask(__name__)
app.config.from_object(Config)

subscription_controller = SubscriptionController()

# POSTリクエストで購読を作成するエンドポイントを設定します
@app.route('/api/subscription', methods=['POST'])
def create_subscription():
    print("Received request for subscription creation")  # デバッグ用のログ
    return subscription_controller.create()

if __name__ == '__main__':
    app.run(debug=True)
