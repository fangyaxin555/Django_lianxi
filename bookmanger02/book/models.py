from django.db import models

# Create your models here.
"""
1。模型类，一个表创建一个模型类
2。每个模型类都要继承models.Model
    2。1 属性名字 对应 字段名字 
        不要使用连续的下划线
        id 系统默认会生成
    2.3 选项 是否有默认值，是否唯一，是否为null
        CharField 必须设置max_length
        verbose_name 主要是在admin站点中使用
3.表的名称
    子应用名字_类的名字
    修改表的名字:
        class Meta:
        db_table = 'bookinfo'
"""
class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍名字'

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    #定义一个有序的字典
    gender_choice = (
        (1,'male'),
        (2,'female')
    )

    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=gender_choice,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)
    

    #外键
    #系统会自动为外键 添加 _id
    #外键的级联操作：当主表的数据删除了后，那么从表有关联的数据应该怎么办？主表删除则从表也要删除
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物名字'

    def __str__(self):
        return self.name