from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import customUser
from django.contrib.auth.models import Permission


# Create your views here.


@csrf_exempt
def permission_user(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        id = data['id']
        permission1 = Permission.objects.get(name='Create Permission')
        permission2 = Permission.objects.get(name='Update Permission')

        print(permission1.id)
        print(permission2.id)

        for ids in id:
            user = customUser.objects.get(identification=ids)
            print(user.identification)
            if user.identification is None:
                print('doesn´t exist user')
            else:
                print('exist user')
                user.user_permissions.add(permission1)
                user.user_permissions.add(permission2)

    return JsonResponse({'response': 'OK'})
