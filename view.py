from django.shortcuts import render,HttpResponse

    def index(request):
            return render(request,'index.html')

	        def africa(request):
		        return HttpResponse('非洲xxxxxxx专区')
<<<<<<< Updated upstream
def live():
    print('加入直播的功能的bugxxxxxx的修复')
=======
#开发测试进行中
>>>>>>> Stashed changes
