from django.conf import settings
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.settings import api_settings


class CustomBooksPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
               'next': self.get_next_link(),
               'previous': self.get_previous_link()
            },
            'total_products': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'products': data
        })