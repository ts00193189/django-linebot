from django.conf import settings

from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent
from linebot.models import TextMessage, ImageMessage, StickerMessage
from linebot.models import TextSendMessage, ImageSendMessage

from messagebot.request_cat import CatRequester
from messagebot.request_weather import WeatherReportRequester

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    if event.message.text == '(emoji)':
        reply = '你給我一個表情貼(‧ω‧)?'
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    elif '給' in event.message.text and '貓' in event.message.text:
        requester = CatRequester()
        random_cat = requester.get_random_cat()
        line_bot_api.reply_message(event.reply_token,
                                   ImageSendMessage(original_content_url=random_cat['url'],
                                                    preview_image_url=random_cat['url']))
    elif '天氣' in event.message.text:
        requester = WeatherReportRequester()
        words = event.message.text.split(' ')
        locations = words[1:]
        if not locations:
            reply = '你沒有告訴我地點(′‧ω‧‵)'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
        else:
            report = requester.get_report(locations)
            reply = []
            for record in report:
                if record['time'][0]['start_time'].hour == 18:
                    day_night = '晚上'
                elif record['time'][0]['start_time'].hour == 6:
                    day_night = '白天'

                reply.append('今日 {}/{} {} {}:\n\n' \
                             '天氣狀況: {}\n' \
                             '降雨機率: {}%\n' \
                             '溫度: {}-{}度\n' \
                             '溫度感受: {}\n'.format(record['time'][0]['start_time'].month,
                                                 record['time'][0]['start_time'].day,
                                                 record['location'], day_night,
                                                 record['time'][0]['天氣狀況'],
                                                 record['time'][0]['降雨機率'],
                                                 record['time'][0]['最低溫度'], record['time'][0]['最高溫度'],
                                                 record['time'][0]['溫度感受']))
            reply = '\n\n'.join(reply)
            reply += '\n這就是今天天氣啦(‧ω‧)/'
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    else:
        reply = event.message.text
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))


@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    reply = '你好像傳了一張圖給我(‧ω‧)?'
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    reply = '你傳了一個貼圖給我(‧ω‧)'
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
