from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles.models import Article
from articles.serializers import ArticleSerializer
from drf_yasg.utils import swagger_auto_schema



class ArticleList(APIView): # class 함수를 쓰게 되면서 더 많은 요소를 상속으로 받아올 수 있다

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticleSerializer)
    def post(self, request, format=None):
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    def get(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#@api_view(['GET', 'POST'])
#def articleAPI(request): # 여러개의 데이터
#    if request.method == 'GET':
#        articles = Article.objects.all()
#        serializer = ArticleSerializer(articles, many=True)
#        return Response(serializer.data) # 시리얼라이즈된 데이터 혹은 에러 등을 명시해줘야 함
#    elif request.method == 'POST':
#        serializer = ArticleSerializer(data = request.data)
#        if serializer.is_valid(): # 유효성 검사
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        else:
#            print(serializer.errors)
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # drf 웹 프론트에서 확인

#@api_view(['GET']) 
#def index(request):# 하나의 데이터
#    articles = Article.objects.all()
#    article = articles[0]
#    serializer = ArticleSerializer(article)
#    return Response(serializer.data) # 시리얼라이즈 된 데이터 혹은 에러 등을 명시해줘야 함

#@api_view(['GET', 'PUT', 'DELETE'])
#def articleDetailAPI(request, article_id):
#    if request.method == 'GET':
##        article = Article.objects.get(id=article_id) # 상세 페이지에 게시된 글을 조회하여 보여줌
#        article = get_object_or_404(Article, id=article_id)
#        serializer = ArticleSerializer(article)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        article = get_object_or_404(Article, id=article_id)
#        serializer = ArticleSerializer(article, data=request.data) # 원래 데이터를 새로운 데이터로 바꿈
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#    elif request.method == 'DELETE':
#        article = get_object_or_404(Article, id=article_id)
#        article.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)