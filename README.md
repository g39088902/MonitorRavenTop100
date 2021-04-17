# MonitorRavenTop100

This repo is designed to monitor the Top100 richest RavenCoin owner's sum wealth.

Users can see how the Raven whale change their positions.

Data from https://ravencoin.network/, thanks.

这个项目用于监视Raven前一百名最富有钱包的财产状况，普通投资者可以通过分析庄家状况加强自身权益保护

————————————————————————————————

Only the index.py and visualListener.py is my code, others is the sqlalchemy lib.

You need to set up a postgresql database to use(such as pull a image from docker).

The index.py of crawler should run in serverless platfrom like 'aws glue' or 'aliyun function calculate'.

The visualize module's generate directory should be your web server directory.

Don't put visualize.py on your web server directory, or you will reveal your database password.

You can use the XXX.sql to define your table.

I suggest you set the time trigger to 15mins per run or longer. 

只有index.py和visualListener.py是我写的，其他文件是sql依赖，需要自行搭建postgresql数据库(比如去Docker拉一个)

请把这个爬虫脚本部署在云平台，比如阿里云函数计算或者aws glue

把可视化模块的生成文件目录设为web服务器目录就行了，不要把脚本放在服务器内（会泄露数据库密码）

数据库定义参考.sql文件

脚本触发器建议设置在15分钟一次或者更长
