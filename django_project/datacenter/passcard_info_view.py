from django_project.datacenter.models import Passcard
from django_project.datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from functions import get_duration, format_duration,\
                      is_visit_long, MAX_VISIT_DURATION
from django.conf import settings


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard=passcard):
        hours, minutes, seconds = get_duration(visit)
        this_passcard_visits.append({
                                     'entered_at': visit.entered_at,
                                     'duration': format_duration(hours,
                                                                 minutes,
                                                                 seconds),
                                     'is_strange': is_visit_long(
                                                                visit, 
                                                                MAX_VISIT_DURATION
                                                                )
                                     }
                                    )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)


