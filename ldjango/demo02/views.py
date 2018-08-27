from django.shortcuts import render, HttpResponse
from django.views import View
from demo02 import models
from random import randint
from django.core.paginator import Paginator


# FBV (function-based view)
def test(request):
    # ------------------------ create data ------------------------
    # models.UserType.objects.create(title='first class user')
    # models.UserType.objects.create(title='second class user')
    # models.UserType.objects.create(title='third class user')
    # models.UserType.objects.create(title='fourth class user')

    # models.UserInfo.objects.create(name='alex', age=23, ut_id=1)
    # models.UserInfo.objects.create(name='patrick', age=21, ut_id=2)
    # models.UserInfo.objects.create(name='joy', age=26, ut_id=3)
    # models.UserInfo.objects.create(name='amy', age=28, ut_id=4)
    # models.UserInfo.objects.create(name='jim', age=29, ut_id=1)

    # ------------------------ get data ------------------------
    rsts = models.UserInfo.objects.all()
    for user in rsts:
        # we just user . to access fields at interlinked tables
        print(user.name, user.age, user.ut_id, user.ut.title)

    print("----- testing UserInfo one rst")
    # UserInfo, ut 是 FK 字段 - 正向操作
    user_info = models.UserInfo.objects.all().first()
    print(user_info.name, user_info.age, user_info.ut.title)

    print("----- testing UserType one rst")
    '''
    this test is trying to say even though UserType doesn't have 
    UserInfo as Foreign key, it still can have access to UserInfo
    UserTyp， 表名小写_set.all() 反向操作
    '''

    user_type = models.UserType.objects.all().first()
    print(user_type.id, user_type.title, user_type.userinfo_set.all())
    for user in user_type.userinfo_set.all():
        print(user.name)

    # 数据获取多个数据的时候
    # 1. [obj, obj,...]  -> obj 只有这种 obj 的形式才可以跨表 access
    models.UserInfo.objects.all()
    models.UserInfo.objects.filter(id__gt=1)

    # 2. [{id:1, name:fd}, {id:1, name:fd} ...}  -> dict 通过双下划线也能跨表访问
    models.UserInfo.objects.all().values('id', 'name', 'ut__title')
    models.UserInfo.objects.filter(id__gt=1).values('id', 'name')

    # 3/ [(1, df), {2,fd)...]  -> tuple
    models.UserInfo.objects.all().values_list('id', 'name')
    models.UserInfo.objects.filter(id__gt=1).values_list('id', 'name')

    # ------------------------ ORM More ------------------------

    user_list = models.UserInfo.objects.all().order_by('-id', 'name')
    print(user_list)
    from django.db.models import Count, Sum, Min, Max
    v = models.UserInfo.objects.values('ut_id').annotate(xxxx=Count('id'))
    print("######")
    print(v.query)

    return HttpResponse("test()....")


# CBV (class-based view)
class Login(View):
    """
    get     list
    post    add
    put     update
    delete  delete
    """

    def dispatch(self, request, *args, **kwargs):
        """
        acting like a decorator for our http request and response
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        print("Before every request !!!")
        dispatcher = super().dispatch(request, *args, **kwargs)  # you can just write super here
        print("After every response !!! ")
        return dispatcher

    def get(self, request):
        print("? Running test CBV get function")
        return render(request, "login.html")

    def post(self, request):
        print("getting a post request value as: " + request.POST.get('user'))
        return HttpResponse("testing: CBV post request")


def index(request):
    # injecting data
    # for i in range(400):
    #     name = "user" + str(i)
    #     age = randint(0, 40)
    #     ut_id = randint(1, 4)
    #     models.UserInfo.objects.create(name=name, age=age, ut_id=ut_id)

    user_list = models.UserInfo.objects.all()
    paginator = Paginator(user_list, 10)
    # for paginator
    # per_page, count, num_pages, page_range, page(object)

    posts = paginator.page(1)
    # (paginator) has_next, next_page_number, has_previous, previous_page_number, object_list(分页后的数据), number, paginator

    current_page = request.GET.get('page')
    if current_page:
        posts = paginator.page(int(current_page))

    return render(request, 'index.html', {'posts': posts})


class PageInfo(object):
    def __init__(self, current_page, all_count, per_page, show_page=11):
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.per_page = per_page
        a, b = divmod(all_count, per_page)
        if b:
            a = a + 1
        self.all_pager = a
        self.show_page = show_page

    def start(self):
        return (self.current_page - 1) * self.per_page

    def end(self):
        return self.current_page * self.per_page

    def pager(self):
        page_list = []
        half = int(self.show_page - 1) / 2
        begin = self.current_page - half
        stop = self.current_page + half + 1

        for i in range(begin, stop):
            if i == self.current_page:
                temp = "<a style='display:inline-block;padding:5px; margin: 5px; background:red' href='custom.html?page=%s'>%s</a>" % (
                    i, i)
            else:
                temp = "<a style='display:inline-block;padding:5px; margin: 5px' href='custom.html?page=%s'>%s</a>" % (
                    i, i)
            page_list.append(temp)
        return ''.join(page_list)


def custom(request):
    all_count = models.UserInfo.objects.all().count()

    page_info = PageInfo(request.GET.get('page'), all_count, 10)
    user_list = models.UserInfo.objects.all()[page_info.start(): page_info.end()]

    return render(request, 'custom.html', {'user_list': user_list})
