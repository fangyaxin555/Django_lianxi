from django.shortcuts import render
from book.models import BookInfo,PeopleInfo

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse('ok')

#数据的增加
BookInfo.objects.create(
    name = '运维开发',
    pub_date = '2020-1-1',
    readcount = 100
)

#数据的更新
BookInfo.objects.filter(id=5).update(commentcount=666)

#数据的删除
BookInfo.objects.filter(id=6).delete()

#数据的查询
BookInfo.objects.all()
BookInfo.objects.all().count()
#id为1的
BookInfo.objects.filter(id__exact=1)
#书名包含湖的
BookInfo.objects.filter(name__contains='湖')
#书名以部结尾的
BookInfo.objects.filter(name__endswith='部')
#搜索姓名为null的图书
BookInfo.objects.filter(name__isnull=True)
#查询编号为1，3，5的图书
BookInfo.objects.filter(id__in=[1,3,5])
#查询编号大于3的图书
BookInfo.objects.filter(id__gt=3)
##查询编号不等于3的图书
BookInfo.objects.exclude(id__exact=3)
#查询1995年出版的书籍
BookInfo.objects.filter(pub_date__year=1995)
#查询1990年1月1日出版的书籍
BookInfo.objects.filter(pub_date__gt='1995-1-1')

#查询阅读量大于20，或者编号小于3的图书
from django.db.models import Q
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

#关联查询
#一对多的查询
booK = BookInfo.objects.get(name='天龙八部')
booK.peopleinfo_set.all()

#多对一的查询
person = PeopleInfo.objects.get(id=1)
person.book.readcount

#子查询
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
PeopleInfo.objects.filter(book__name__exact='天龙八部')
#分页查询
from django.core.paginator import Paginator
people = PeopleInfo.objects.all().order_by("id")#必须要进行排序，不然会出现报错
page = Paginator(people,4)
page1 = page(1)