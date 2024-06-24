import unittest
from app import create_app, db
from models import User, Task

class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post('/register', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

        with self.app.app_context():
            # Verifys the user was created
            user = User.query.filter_by(username='testuser').first()
            self.assertIsNotNone(user)
            self.assertTrue(user.check_password('testpassword'))

    def test_login(self):
        with self.app.app_context():
            # First, registers a user
            user = User(username='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()

        # Then, attempts to log in
        response = self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)  # Checks for the presence of the dashboard page

    def test_add_task(self):
        with self.app.app_context():
            # Registers and logs in a user
            user = User(username='testuser')
            user.set_password('testpassword')
            db.session.add(user)
            db.session.commit()

        self.client.post('/login', data=dict(
            username='testuser',
            password='testpassword'
        ), follow_redirects=True)

        # Adds a task
        response = self.client.post('/addTask', data=dict(
            title='Test Task',
            description='This is a test task.',
            due_date='2024-06-30',
            priority='High',
            status='Incomplete'
        ), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

        with self.app.app_context():
            # Verifys the task was created
            task = Task.query.filter_by(title='Test Task').first()
            self.assertIsNotNone(task)
            self.assertEqual(task.description, 'This is a test task.')

if __name__ == '__main__':
    unittest.main()
