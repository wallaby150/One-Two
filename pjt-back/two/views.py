from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_list_or_404
from .serializers import RankingSerializer
from django.contrib.auth import get_user_model
from accounts.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def fail(request):
    User = get_user_model()
    user = User.objects.get(pk=request.user.id)
    if user.score < int(request.data['score']):
        user.score = int(request.data['score'])
        user.save()
    return Response(status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ranking(request):
    users = get_list_or_404(User)
    myuserlist = []
    scorelist = []
    if len(users) > 50:
        for i in users:
            if len(scorelist) < 50:
                myuserlist.append(i)
                scorelist.append(i.score)
            else:
                if i.score > min(scorelist):
                    a = reversed(scorelist)
                    idx = min(a).index
                    del myuserlist[idx]
                    del scorelist[idx]
                    myuserlist.append(i)
                    scorelist.append(i.score)
        tmp_dict = {}
        for i in range(len(myuserlist)):
            tmp_dict[myuserlist[i]] = scorelist[i]
        result = sorted(tmp_dict,key=lambda x:tmp_dict[x], reverse=True)[0:50]     
    else:
        for i in users:
            myuserlist.append(i)
            scorelist.append(i.score)
            tmp_dict = {}
            for i in range(len(myuserlist)):
                tmp_dict[myuserlist[i]] = scorelist[i]
            result = sorted(tmp_dict,key=lambda x:tmp_dict[x], reverse=True)
    serializer = RankingSerializer(result, many=True)
    return Response(serializer.data)