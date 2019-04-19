import requests

# response=requests.get('https://www.baidu.com')
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text.encode('utf-8'))
# print(response.cookies)

# 从字典类型传参数到get
# data={
#     'name':'xdream',
#     'age':42,
#     'sex':'male'
# }
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.text)

# 将返回值转换为json格式
# response = requests.get('http://httpbin.org/get')
# print(type(response.text))
# print(response.json())
# print(type(response.json()))

# 下载存储二进制格式文件
# response=requests.get('https://github.com/favicon.ico')
# with open('favicon.ico','wb') as f:
#     f.write(response.content)
#     f.close()

# 添加headers以防止被Server拒绝访问
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# response = requests.get('https://www.zhihu.com/explore', headers=headers)
# print(response.text)

# 使用Cookies维持会话、模拟登录
# s=requests.Session()
# s.get('http://httpbin.org/cookies/set/number/12345654321')
# response=s.get('http://httpbin.org/cookies')
# print(response.text)

# 捕获超时等各种读取异常
from requests.exceptions import ReadTimeout, HTTPError, RequestException, ConnectionError

try:
    response = requests.get('http://httpbin.org/get', timeout=0.5)
    print(response.status_code)
except ReadTimeout:
    print('Timeout')
except ConnectionError:
    print('Connection Error')
except HTTPError:
    print('Http error')
except RequestException:
    print('Error')
