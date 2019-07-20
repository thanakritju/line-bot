import os
import re

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from app.models import Task
from app.parsers import task_parser


app = Flask(__name__)

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

# init todo list
TODOs = Task()

@app.route("/ping", methods=['GET'])
def hello():
    return 'pong'

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    incoming_message = event.message.text
    # If not in the command list, echo the message
    returning_message = event.message.text

    if incoming_message.startswith("todo ") or incoming_message.startswith("Todo "):
        returning_message = tasks_handler(incoming_message)
        
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=returning_message),
    )

def tasks_handler(incoming_message):
    command, value = task_parser(incoming_message)
    if command == "show":
        return TODOs.show_task()
    elif command == "add":
        return TODOs.add_task(value)
    elif command == "del":
        return TODOs.delete_task(value)
    elif command == "delall":
        return TODOs.delete_all_tasks()
    elif command == "done":
        return TODOs.done_task(value)
    return TODOs.help()

    
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000)
