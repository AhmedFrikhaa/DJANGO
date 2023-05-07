from django.core.management.base import BaseCommand, CommandError
from base.models import Task


class Command(BaseCommand):
    help = 'Show all tasks for all users in the database'

    def add_arguments(self, parser):
        parser.add_argument('task_id', nargs='+', type=int)

    def handle(self, *args, **options):
       for task_id in options['task_id']:
           try:
               task = Task.objects.get(pk=task_id)
           except:
               raise CommandError(f'Task with ID {task_id} does not exist')


           self.stdout.write(self.style.SUCCESS(f'Task with ID {task_id} is {task.completed}'))