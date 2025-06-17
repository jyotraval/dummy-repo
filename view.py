from django.http import HttpResponse
from django.shortcuts import render

import temp

def aboutus(request):
    return HttpResponse("About us")

def homepage(request):
    result = temp.get_contests_from_supabase()
    if not result:
        return HttpResponse("Failed to load contest data", status=500) #500-- internal server side error
    
    column_name, contests_content_raw = result

    # NOTE: redudancancy remove while deploying -->
    contests_content_raw= contests_content_raw + contests_content_raw

    return render(request, 'index.html', {
        'column_name': column_name,
        'contests_content_raw': contests_content_raw
    })
    
