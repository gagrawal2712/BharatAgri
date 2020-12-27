import logging
from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.encoding import force_text

log = logging.getLogger(__name__)


class Exception400(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = '400 Exception'
    
    def __init__(self, detail=None, status_code=None):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = force_text(detail)
        log.error('Exception : %s' % self.detail)
    