import json
from django.http import HttpResponse
from django.contrib.auth.models import User
from studio_app.models import Manager

from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_user(request):
  """Handles the creation of a new user for authentication
  Method args:
    request -- the full HTTP request object
  """

  req_body = json.loads(request.body.decode())

  # make new user
  new_user = User.objects.create_user(
      username=req_body['username'],
      password=req_body['password'],
      email=req_body['email'],
      first_name=req_body['first_name'],
      last_name=req_body['last_name'],
  )
  # # make new customer for that user
  new_manager = Manager.objects.create(
      user=new_user,
      first_name=req_body['first_name'],
      last_name=req_body['last_name'],
      street_address=req_body['street'],
      city=req_body['city'],
      state=req_body['state'],
      zipcode=req_body['zip'],
  )

  token = Token.objects.create(user=new_user)

  data = json.dumps({"token": token.key})
  return HttpResponse(data, content_type='application/json')