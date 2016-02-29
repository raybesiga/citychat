from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

from twilio.access_token import AccessToken, IpMessagingGrant

def chat(request):
    return render(request, 'chat.html')

def token(request):
    device_id = request.GET.get('device', 'unknown')
    identity = request.GET.get('identity', 'guest').encode('utf-8')
    endpoint_id = "NeighborChat:{0}, {1}".format(device_id, identity)
    token = AccessToken(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_API_KEY, settings.TWILIO_API_SECRET, identity)
    grant = IpMessagingGrant()
    grant.service_sid = settings.TWILIO_IPM_SERVICE_SID
    grant.endpoint_id = endpoint_id
    token.add_grant(grant)
    response = {'identity': identity, 'token': token.to_jwt()}
    return JsonResponse(response)