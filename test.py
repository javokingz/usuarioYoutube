import unittest
from app import create_app
from app.responses import *
from config import config
from app import db
import json

class TestAPI(unittest.TestCase):
    def setUp(self):
        enviroment = config['test']
        self.app = create_app(enviroment)
        self.client = self.app.test_client()

        self.content_type = 'application/json'
        self.path = 'http://127.0.0.1:5000/api/usuarios'
    
    def tearDown(self):
        with self.app.app_context():
            pass
           
    def test_one_equals_one(self):
        self.assertEqual(1,1)
    
    def test_get_all_tasks(self):
        response = self.client.get(path=self.path)
        self.assertEqual(response.status_code, 200)

    def test_get_first_usuario(self):
        new_path = self.path + '/1'
        response = self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 200)

    def test_not_found(self):
        new_path = self.path + '/200'
        response = self.client.get(path=new_path, content_type=self.content_type)
        self.assertEqual(response.status_code, 404)

    def test_create_usuario(self):
        data = {
            'nombre': 'nombre', 'nickname': 'nickname'
        }

        response = self.client.post(path= self.path, data=json.dumps(data), content_type = self.content_type)
        self.assertEqual(response.status_code, 200)
        


        

if __name__ =='__main__':
    unittest.main()