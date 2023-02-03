from urllib.request import urlopen
# from urllib.error import URLError

service_port = 12345
test_text = 'Test'
try:
    with urlopen(f"http://localhost:{service_port}/?text={test_text}") as response:
        #Обработчик ответа от второго сервиса

        result = response.read().decode()
        expected_res = test_text+' '+test_text
        if (expected_res in result):
            print(True)
        else:
            print(False)
except Exception as e: 
    # ConnectionError or URLError 
   print(False)
