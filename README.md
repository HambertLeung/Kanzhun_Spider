# Kanzhun_Spider
正则爬取看准网面经，结果保存至csv文件

# How to use
使用之前须在Kanzhun_Config.py文件中设置传入的参数，包括：

KEYWORD = '数据库' # 这里输入关键词  
FILENAME = '看准网_' + str(KEYWORD) + '_面经收集.csv' # 保存的文件名，可不做修改  
FILEPATH = 'F:\Kanzhun' # csv结果保存目录，最好与代码存放目录一致  

GROUP_START = 1 # 爬取起始页数  
GROUP_END = 3 # 爬取结束页数，亲测最大1001

