import zmail
import os
import time
from test201912.test1205.readYaml import ReadYaml


class SendEmail:
    '''
    zmail是一个用于收发邮件的python扩展包
    该类主要通过zmil实现发送邮件功能
    实例化该类支持可选参数defultPath的传递，若传递则邮件附件使用传递的路径文件，若不传递则使用该页面默认的路径文件
    '''

    cwd = os.getcwd()  # 当前文件所在文件夹地址
    # root = os.path.dirname(cwd)  # 父级目录
    path = os.path.join(cwd, r"report\result.html")  # 报告所在路径

    def __init__(self, defultPath = path):
        emailDIC = ReadYaml('email').readByKey()  # yaml配置文件中读取email相关地址及邮箱授权码
        self.servcieEmail = emailDIC['servcieEmail']  # 发送方邮箱
        self.serviceCode = emailDIC['serviceCode']  # 发送方邮箱授权码
        self.reciveEmail = emailDIC['reciveEmail']  # 接受邮箱
        self.reportPath = defultPath

    def sendText(self):
        '''
        发送纯文本的邮件
        :return:
        '''
        server = zmail.server(self.servcieEmail, self.serviceCode)
        mail = {
            'subject': '测试邮件标题-文本!'+time.strftime("%Y-%m-%d %X"),
            'content_text': 'By zmail.'
        }
        # 发送email
        server.send_mail(self.reciveEmail, mail)

    def sendHtml(self):
        '''
        发送html的邮件
        :return:
        '''
        with open(self.reportPath, 'r', encoding="utf-8") as f:
            content_html = f.read()
        mail = {
            'subject': '测试邮件标题-HTML!'+time.strftime("%Y-%m-%d %X"),  # Anything you want.
            'content_html': content_html,
        }
        server = zmail.server(self.servcieEmail, self.serviceCode)
        server.send_mail(self.reciveEmail, mail)

    def sendFJ(self):
        '''
        发送带附件的邮件
        :return:
        '''
        mail = {
            'subject': '接口功能自动化测试报告'+time.strftime("%Y-%m-%d %X"),  # Anything you want.
            'content_text': '您好，附件为xx系统接口功能自动化测试报告，请查收！',
            'attachments': [self.reportPath],  # Absolute path will be better.
        }
        server = zmail.server(self.servcieEmail, self.serviceCode)
        server.send_mail(self.reciveEmail, mail)


if __name__ == '__main__':
    SendEmail().sendFJ()
