from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return Response({
        'message': 'Welcome to the tdevcommunity TEAM3 API.',
        'version': '1.0.0',
        'authors': {
            '1.': 'Charles GBOYOU',
            '2.': '',
            '3.': '',
            '4.': '',
        },
        'address': 'tdevcommunity TEAM3',
        'example': {
            'notice': '_______________________________________',
            'url': request.build_absolute_uri() + '____________'
        }
    }, status=201)
