# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:37:45 2021

@author: TAKA
"""

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

app = Flask(__name__)

ACCESS_TOKEN = "+cnmY7axt/ecdu3pgac9/uKLA8iKpnRjGZmBQp13KzgWEjtDTdDA67qAohTlBuJoBSzHvZljWAyOmLicwfFM56wTB4yW8fCpIpOJfdTXigF3ezYAGwm+QEOl2llcttJWdtm3o+xgoj4bTWI2MNiDmwdB04t89/1O/w1cDnyilFU="
SECRET = "e6e085abd27af5f89ec6bf52955074ca"

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

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
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

if __name__ == "__main__":
    app.run()
