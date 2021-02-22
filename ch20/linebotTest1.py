from flask import Flask
app = Flask(__name__)

from flask import Flask, request, abort
from linebot import  LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('Ma+cSlUN7avam0bNx/8Y/ptLWuTZWs0RB/B+JfPEIbAzZleElwpr8JaOeB6SHoEtS4bKtmE0SJN7prvdfTuJVRLdRyPbKqw7G2Lpvn0qczhwqV6RrIbLG3ILCqqz3CeaWa3FFr8O0cRsb0l5hZwRGQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('09b64f3102d93a60eb07d6cc46c4bde8')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

if __name__ == '__main__':
    app.run()
