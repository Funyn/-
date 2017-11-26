from django.shortcuts import render,HttpResponse

    def index(request):
            return render(request,'index.html')

	        def africa(request):
		        return HttpResponse('非洲专区')
def live():
    print('加入直播的功能的bug的修复')
