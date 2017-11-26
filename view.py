from django.shortcuts import render,HttpResponse

    def index(request):
            return render(request,'index.html')

	        def africa(request):
		        return HttpResponse('非洲专区')
