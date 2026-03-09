#from graphene_django.views import GraphQLView
#from django.views.decorators.csrf import csrf_exempt
from .jwt_views import CustomTokenObtainPairView
from django.urls import path, include

urlpatterns = [
    # JWT personalizado
    path('auth/jwt/login/', CustomTokenObtainPairView.as_view(), name='jwt_login'),
    # ... resto
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]