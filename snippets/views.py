from django.db.models           import query
from snippets.models            import Snippet
from snippets.serializers       import SnippetSerializer
from django.http                import Http404
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework             import status
from rest_framework             import mixins
from rest_framework             import generics
from django.contrib.auth.models import User
from snippets.serializers       import UserSerializer
from rest_framework             import permissions

""" Class-based view """
# class SnippetList(APIView):
#     def get(self, request, format = None):
#         snippets = Snippet.objects.all()
#         serializers = SnippetSerializer(snippets, many = True)
#         return Response(serializers.data)

#     def post(self, request, format = None):
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk = pk)
#         except Snippet.DoesNotExist:
#             return Http404

#     def get(self, request, pk, format = None):
#         snippet = self.get_object(pk)        
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format = None):
#         snippet = self.get_object(pk)        
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

""" Use Mixins """

# class SnippetList(mixins.ListModelMixin, 
#                   mixins.CreateModelMixin, 
#                   generics.GenericAPIView):
                  
#     queryset         = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):

#     queryset         = Snippet.objects.all()
#     serializer_class = SnippetSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

""" Use Generic Class-based View """

class SnippetList(generics.ListCreateAPIView):
    queryset           = Snippet.objects.all()
    serializer_class   = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset         = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

""" User View """

class UserList(generics.ListAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = UserSerializer