from django.test import TestCase
from django.urls import reverse
from .models import Productos, Empleado
from .views import MainPageView
from django.contrib.auth.models import User
from datetime import datetime
import tempfile


class TestBlog(TestCase):

    def setUp(self):
        
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name

        self.user = User.objects.create_user(username='user', email='email@example.com', password='pass')
        self.user.save()
        
        self.empleado = Empleado(user=self.user)
        self.empleado.save()
        
        self.producto = Productos(marca="marca", categoria="categoria", tipo="tipo", 
                                author=self.empleado, is_headline=True,
                                image=image,
                                date_published=datetime.now())
        self.producto.save()
    
        self.user_1 = User.objects.create_user(username='user_1', email='email_1@example.com', password='pass')
    
    def test_list_all_articles(self):
        response = self.client.get(reverse('main-page'))
        self.assertEqual(response.resolver_match.func.view_class.__name__,  MainPageView.__name__)