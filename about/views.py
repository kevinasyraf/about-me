from django.shortcuts import render

def about(request):
	context = {
	'foto' : 'img/Kevin Asyraf.jpg',
	}
	return render(request, 'about.html', context)