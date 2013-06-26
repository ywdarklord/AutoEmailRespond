#Auto Email Processing
======================

本程序使用Python实现邮件的自动接受和处理。可以设置为每15分钟，每30分钟以及每小时接收并处理一次邮件。

通过2个主要的类：Mail和InBox,每封邮件为一个Mail的实例并储存于InBox的实例中。

Mail类内容如下：

    class myMail:

	    fro=''  #  发件人
	    header='' #  主题
	    content='' # 内容
	    trackNumber='' # 位于服务器上的邮件号
	    webURL=[] # 对内容进行处理后提取出来的匹配号的网址
	
	    def processFROM(self): # 处理发件人得到纯的email地址
	    def processContent(self): # 处理邮件内容（本处理方法用于提取网宿CDN给七牛发来邮件中的匹配好的网址）

InBox类内容如下：

    class InBox:

	    mailAmount=0 #统计受到的邮件总数
	    emails=[]    #存放Mail对象
	    __conn=None  #与服务器建立连接的对象
	    
	    def getAccountOnline(self): # 连接到邮件服务器
	    def getAccountOffline(self): # 断开连接
	    def getMail_15(self): # 每15分钟收一次邮件
	    def getMail_30(self): # 每30分钟收一次邮件
	    def getMail_1h(self): # 每1小时收一次邮件
	
	    def __getMail(self): # 收邮件的方法
	
	        def extract_body(payload):
	        
还需要一个配置文件存放邮件服务器的用户名和密码：config.py:

     host='imap.gmail.com'  #收件服务器
     username='example@gmail.com' #用户名 
     password='*******' #密码
     
     
     
 使用方法：
 
     #首先初始化一个InBox类的对象：
     gmail=InBox()
     #让帐户上线
     gmail.getAccountOnline()
     #设置每15分钟收一次邮件
     gmail.getMail_15()
     #退出（这将中断与收件服务器的连接以及终止收件）
     gmail.getAccountOffline()
     
     
完成后，所有的邮件将被存于InBox对象的emails属性中。emails对象是一个二维数组，存放者每次(15,30或60分钟)收到的一批邮件，每批邮件中存放者多个Mail对象。
例如：查询第一批收到的邮件中的第一封：

     message=gmail.emails[0][0]

然后我们就可以调用message既Mail对象的方法来对message进行处理：

     #下面方法将会获得纯粹的发件人地址，例如本来的发件人信息为：John Smith<JohnSmith@gmail.com>，经过处理后只提取 "JohnSmith@gmail.com"
     
     message.processFROM()
     
     #下面方法将会获得邮件内容中匹配好的网址：
     
     message.processContent()
     
     #查询webURL即可获得网址：
     
     message.webURL
     
     


            