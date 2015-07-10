#coding:utf-8
import MySQLdb,time,sys
reload(sys)
class ty2file:
    def __init__(self,host,user,passwd,dbname,dbprefix):
        self.host=host
        self.user=user
        self.passwd=passwd
        self.dbname=dbname
        self.dbprefix=dbprefix
        self.get_posts()
    def get_posts(self):
        sys.setdefaultencoding( "utf-8" )
        conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.dbname,charset="utf8")
        cu=conn.cursor()
        cx=cu.execute
        data=cx("select title,text,created from %s_contents;"%self.dbprefix)
        blogs=[]
        for row in cu.fetchall():      
            blogs.append(row)
        self.write_file(blogs)
    def write_file(self,blogs):
        for i in blogs:
            title=i[0]
            filename=title.replace("/"," ").replace("?"," ").replace(" ","")
            content=i[1]
            created=i[2]
            time1=time.strftime('%Y-%m-%d',time.localtime(created))
            time2=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(created))
            if content.find("markdown")!=-1:
                f=open("%s-%s.md"%(time1,filename),"w")
                f.write(('---\nlayout:   post\ntitle:  "%s"\ndate:   %s\n---\n'%(title,time2)+content.replace("<!--markdown-->","")))
                f.close()
            else:
                f=open("%s-%s.html"%(time1,filename),"w")
                f.write(('---\ntitle:  "%s"\ndate:   %s\n---\n'%(title,time2)+content))
                f.close()
ty2file("数据库地址","用户名","密码","数据库名","数据库前缀")
