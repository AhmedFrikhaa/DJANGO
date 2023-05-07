from django.core.management.base import BaseCommand, CommandError
from base.models import Task


class Command(BaseCommand):
    help = "see if the task is completed or not by ID"

    def add_arguments(self, parser):
        parser.add_argument('task_id', nargs='+', type=int)

    def handle(self, *args, **options):
        task_id = options['task_id'][0]
        try:
            task = Task.objects.get(id=task_id)
        except:
            raise CommandError(f'Task with ID {task_id} does not exist')

        if task.complete:
            self.stdout.write(self.style.SUCCESS(f'Task with ID {task_id} is completed'))
        else:
            self.stdout.write(self.style.WARNING(f'Task with ID {task_id} is not completed'))
