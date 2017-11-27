from django.shortcuts import render,HttpResponse

    def index(request):
            return render(request,'index.html')

	        def africa(request):
		        return HttpResponse('非洲xxxxxxx专区')

def live():
    print('加入直播的功能的bug的修复')

#开发测试进行中

def change():
    print('测试功能完成')

def change2():
    print('测试功能完成')
<<<<<<< HEAD
def change3():
    print('测试功能3')
=======

def change4():
    print('测试功能4')
>>>>>>> b84a91f0ff8b4d115b5e57513fabf429c857f140
