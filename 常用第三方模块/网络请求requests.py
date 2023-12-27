#  pip install requests

import requests

# GET
r = requests.get('https://www.douban.com/')
r.status_code
r.text
r.headers
r.cookies
cs = {'token': '12345', 'status': 'working'}
r = requests.get('https://www.douban.com/', cookies=cs)
r = requests.get('https://www.douban.com/', timeout=2.5)


r = requests.get('https://www.douban.com/search',
                 params={'q': 'python', 'cat': '1001'})
r.url
r.encoding
r.content
r.json()  # 将json格式数据直接格式化

r = requests.get('https://www.douban.com/', headers={
                 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})


# POST
r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})

params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params)

upload_files = {'file': open('report.xls', 'rb')}
r = requests.post('https://accounts.douban.com/login', files=upload_files)
