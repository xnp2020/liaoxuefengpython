import chardet


chardet.detect(b'Hello, world!')


data = '离离原上草，一岁一枯荣'.encode('gbk')
chardet.detect(data)

data = '离离原上草，一岁一枯荣'.encode('utf-8')
chardet.detect(data)


data = '最新の主要ニュース'.encode('euc-jp')
chardet.detect(data)
