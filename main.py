import requests
import time
API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '6812909660:AAEq7qTQTbsuDYYZ2vIKxaEallvQV-2m9YE'
TEXT1 = 'Все говорят: '
TEXT2 = ', а ты купи слона!'
MAX_COUNTER = 100
offset = -2
counter = 0
chat_id: int
while counter < MAX_COUNTER:
    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            UTEXT = result['message'].get('text', ' ')
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT1 + UTEXT + TEXT2}')
    time.sleep(1)
    counter += 1