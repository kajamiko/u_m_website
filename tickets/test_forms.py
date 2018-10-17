from django.test import TestCase
from .forms import TicketForm, CommentForm
from django.contrib.auth.models import User


class TestTicketForm(TestCase):
     
     
     def test_for_posting_variety_only(self):
          form = TicketForm({'variety': 'F'})
          self.assertFalse(form.is_valid())
          
     def test_for_posting_issue_only(self):
          form = TicketForm({'issue': 'some issue'})
          self.assertFalse(form.is_valid())
          
     def test_for_posting_description_only(self):
          form = TicketForm({'description': 'some issue'})
          self.assertFalse(form.is_valid())
          
     def test_for_posting_invalid_variety(self):
          form = TicketForm({'variety': 'c', 'description': 'some issue', 'issue': 'some issue'})
          self.assertFalse(form.is_valid())
          
     def test_for_posting_normal(self):
          form = TicketForm({'variety': 'B', 'description': 'some issue', 'issue': 'some issue'})
          self.assertTrue(form.is_valid())

class TestCommentForm(TestCase):
     
     def test_for_comment_with_no_user(self):
          form = CommentForm({'author': 'some', 'title': 'title', 'content': 'content'})
          self.assertTrue(form.is_valid())

     # def test_for_comment_with_a_user(self):
     #      user = User.objects.create_user('foo', 'myemail@test.com', 'bar')
     #      self.client.login(username='foo', password='bar')
     #      form = CommentForm({'user': user, 'author': 'some', 'title': 'title', 'content': 'content'})
     #      self.assertTrue(form.is_valid())

     def test_for_comment_with_no_author(self):
          form = CommentForm({'title': 'title', 'content': 'content'})
          self.assertFalse(form.is_valid())