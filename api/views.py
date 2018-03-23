# Create your views here.
from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import (HTMLFormRenderer,
                                      JSONRenderer, BrowsableAPIRenderer)


from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewSet(NestedViewSetMixin, ViewSet):
    serializer_class = AuthorSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request):
        queryset = Author.objects.filter()
        serializer = AuthorSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.filter()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(
            author, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data,
                                      context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk, format=None):
        queryset = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(queryset,
                                      context={'request': request},
                                      data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)


class BookViewSet(NestedViewSetMixin, ViewSet):
    serializer_class = BookSerializer
    renderer_classes = (BrowsableAPIRenderer, JSONRenderer, HTMLFormRenderer)

    def list(self, request, parent_lookup_author=None):
        queryset = Book.objects.filter(author=parent_lookup_author)
        serializer = BookSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, parent_lookup_author=None):
        queryset = Book.objects.filter(
            author=parent_lookup_author)
        book = get_object_or_404(queryset, pk=pk)
        serializer = BookSerializer(
            book, context={'request': request})
        return Response(serializer.data)

    def create(self, request, parent_lookup_author=None):
        serializer = BookSerializer(data=request.data,
                                    context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
