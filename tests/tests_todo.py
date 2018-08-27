from unittest import TestCase, mock
from flask import url_for
from app import app


class TestsTodos(TestCase):
    def setUp(self):
        self.app = app
        self.app.config["SERVER_NAME"] = "localhost:5000"
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.testing = True

    def test_when_put_task_in_todo_should_return_201(self):
        expected = 201
        task_sample = 'Comer'
        request = self.client.put(url_for('todo.put_task'),
                                  json={'task': task_sample})
        self.assertEqual(expected, request.status_code)

    @mock.patch('app.todo.tasks_queue')
    def test_put_task_should_call_tasks_queue(self, mocked_queue):
        task_sample = 'Comer'
        request = self.client.put(url_for('todo.put_task'),
                                  json={'task': task_sample})

        mocked_queue.append.assert_called()


    def test_put_task_should_return_400_when_put_invalid_key(self):
        task_sample = 'Comer'
        request = self.client.put(url_for('todo.put_task'),
                                  json={'batata': task_sample})

        self.assertEqual(request.status_code, 400)


    def test_get_tasks_should_return_blank_tasks_when_dont_have_tasks(self):
        request = self.client.get(url_for('todo.get_tasks'))
        self.assertEqual(request.json, {'tasks': []})

    def test_get_tasks_should_return_tasks_when_put_then(self):
        task_samples = ['Comer', 'Dormir', 'Codar']

        for task in task_samples:
            self.client.put(url_for('todo.put_task'),
                            json={'task': task})

        request = self.client.get(url_for('todo.get_tasks'))
        self.assertEqual(request.json, {'tasks': task_samples})

    def test_modify_should_result_404_when_has_blank_queue(self):
        request = self.client.get(url_for('todo.modify_tasks',
                                          old_task='batata',
                                          new_task='Oi'))
        self.assertEqual(request.status_code, 404)

    def test_modify_should_modify_existent_task_in_queue(self):
        task_sample = 'Comer'
        task_result = 'Chorar'
        self.client.put(url_for('todo.put_task'), json={'task': task_sample})

        request = self.client.get(url_for('todo.modify_tasks',
                                          old_task=task_sample,
                                          new_task=task_result))

        self.assertEqual(request.status_code, 201)

        request = self.client.get(url_for('todo.get_tasks'))

        self.assertIn(task_result, request.json['tasks'])
