import itchat
import requests
def get_response(msg):
    # 这里我们就像在“3. 实现最简单的与图灵机器人的交互”中做的一样
    # 构造了要发送给服务器的数据
    url='http://www.tuling123.com/openapi/api'
    KEY='27424c5d162a4a53a70b41e9275f215d'
    data={
        'key':KEY,
        'info':msg,
        'userid':'shuai'
        }
    # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
    try:
        r=requests.post(url,data).json()
        return r.get('text')
    # 为了防止服务器没有正常响应导致程序异常退出，这里用try-except捕获了异常
    # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
    except:
        # 将会返回一个None
        return
@itchat.msg_register(itchat.content.TEXT)        
def information_reply(msg):
    defaultreply='i received'+msg['Text']
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    reply=get_response(msg['Text'])
    return reply or defaultreply
# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
