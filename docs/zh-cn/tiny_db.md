## 简介
`TinyDB` 依托于json文件，像操作数据库一样去操作json文件。适合少量数据，单线程操作。比如客户端的配置文件、控件的记忆能力等。

******
## 官网
  - [官方文档](https://tinydb.readthedocs.io/en/latest/)
  - [GitHub](https://github.com/msiemens/tinydb)
********
## 安装
  - `pip install tinydb`
******
## 示例代码

```python
from tinydb import TinyDB, Query
# 初始化DB
db: TinyDB = TinyDB(path='config.json', ensure_ascii=False, encoding='utf-8')
# 表句柄
table = db.table('WeChatGroupList')
# 截断表
table.truncate()
# 插入数据
table.insert_multiple([
    {
        "name": "Erupt 框架交流群",
        "yield": 10
    },
    {
        "name": "比亚迪宋DMi总群(5群)",
        "yield": 10
    },
    {
        "name": "Chat2DB交流群48",
        "yield": 10
    },
    {
        "name": "CSDN读者俱乐部11群",
        "yield": 10,
        "leader": {
            'name': "Alex"
        },
        "friends": [
            {
                "name": "Alex"
            },
            {
                "name": "Lucy"
            }
        ]
    },
    {
        "name": "南京金牛湖景区探店群",
        "yield": 5,
        "leader": {
            'name': "Lily"
        },
        "friends": [
            {
                "name": "Lily"
            },
            {
                "name": "Lucy"
            }
        ]
    }
])
# 删除数据
table.remove(Query().name == 'Erupt 框架交流群')
table.remove(doc_ids=[2])
# 修改数据
table.update({"yield": 20}, Query().name == 'Chat2DB交流群48')
table.update({"yield": 21}, doc_ids=[3])
# 查询数据
result = table.all()
search1 = table.search(Query()['yield'] == 21)
search2 = table.search(Query()['yield'] >= 10)
search3 = table.search(Query().name == 'CSDN读者俱乐部11群')
search4 = table.search(Query().leader.name == 'Lily')
search5 = table.search(Query().leader.name.matches('Al*'))
search6 = table.search(Query().name.search('群'))
print(result)
print(search1)
print(search2)
print(search3)
print(search4)
print(search5)
print(search6)
```