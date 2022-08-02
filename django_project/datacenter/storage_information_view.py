from django_project.datacenter.models import Passcard
from django_project.datacenter.models import Visit
from django.shortcuts import render
from functions import get_duration, format_duration


def storage_information_view(request):
    none_closed_visits = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        hours, minutes, seconds = get_duration(visit)
        none_closed_visits.append({'who_entered': visit.passcard.owner_name,
                                   'entered_at': visit.entered_at,
                                   'duration': format_duration(hours,
                                                               minutes,
                                                               seconds)
                                   }
                                  )
    context = {
        'non_closed_visits': none_closed_visits
    }
    return render(request, 'storage_information.html', context)
