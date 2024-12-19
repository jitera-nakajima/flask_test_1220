from flask import Flask
from controllers.subscription_controller import SubscriptionController

app = Flask(__name__)
subscription_controller = SubscriptionController()

# POSTリクエストで購読を作成するエンドポイントを設定します
@app.route('/api/subscription', methods=['POST'])
def create_subscription():
    return subscription_controller.create()

if __name__ == '__main__':
    app.run(debug=True)
