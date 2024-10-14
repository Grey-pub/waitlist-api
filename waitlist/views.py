from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.decorators import api_view
from .models import Waitlist
from .serializers import RecieveWaitlistSerializer, ViewWaitlistSerializer, RespondWaitlistSerializer
from .mails import send_confirmation_mail, send_response_mail
from django.shortcuts import get_object_or_404


@api_view(["POST"])
def waitlist_collection(request):
    flag = False

    if request.data.get("question"):
        flag = True

    serializer = RecieveWaitlistSerializer(data=request.data)
    if serializer.is_valid():
        new_waitlist = Waitlist.objects.create(**serializer.validated_data)
        new_waitlist.save()

        send_confirmation_mail(email=new_waitlist.email, first_name=new_waitlist.first_name, flag=flag)

        return Response({"message": "Waitlist saved successfully successfully."}, status=HTTP_200_OK)

    return Response({"message": serializer.errors}, status=HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def waitlist_view(request):
    waitlists = Waitlist.objects.all()
    serializer = ViewWaitlistSerializer(instance=waitlists, many=True)
    return Response({"message": "Found all lists.", "data": serializer.data}, status=HTTP_200_OK)


@api_view(["POST"])
def waitlist_respond(request):
    user = get_object_or_404(Waitlist, id=request.data['id'])

    serializer = RespondWaitlistSerializer(instance=user, data=request.data, partial=True)
    if serializer.is_valid():

        user.response = serializer.validated_data["response"]
        user.save()
        
        send_response_mail(email=user.email, first_name=user.first_name, question=user.question, response=user.response)

        user.responded = True
        user.save()

        return Response({"message": "Response sent successfully"}, status=HTTP_200_OK)
    return Response({"message": serializer.errors}, status=HTTP_400_BAD_REQUEST)    