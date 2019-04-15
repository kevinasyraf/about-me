from django.shortcuts import render

def index(request):
	context = {
	'foto' : 'img/KevinAsyraf.jpg',
	}
	return render(request, 'home.html', context)