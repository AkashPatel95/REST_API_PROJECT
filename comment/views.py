from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

@api_view(['GET'])
def get_comments(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

def get_custom_comments(request):
    data = [
        {
            "postId": 1,
            "id": 1,
            "name": "id labore ex et quam laborum",
            "email": "Eliseo@gardner.biz",
            "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
        },
        {
            "postId": 1,
            "id": 2,
            "name": "quo vero reiciendis velit similique earum",
            "email": "layne_Kuhic@sydney.com",
            "body": "est natus enim nihil est dolore omnis voluptatem numquam\net omnis occaecati quod ullam at\nvoluptatem error expedita pariatur\nnihil sint nostrum voluptatem reiciendis et"
        }
    ]

    json_response = ""
    for entry in data:
        json_response += f'"postId": {entry["postId"]},\n"id": {entry["id"]},\n"name": "{entry["name"]}",\n"email": "{entry["email"]}",\n"body": "{entry["body"]}"\n\n'

    return HttpResponse(f'{{\n{json_response}}}')
