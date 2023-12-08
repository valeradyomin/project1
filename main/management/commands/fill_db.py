from django.core.management import BaseCommand

from main.models import Student


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        students_list = [
            {'first_name': 'Sam', 'last_name': 'White'},
            {'first_name': 'Tom', 'last_name': 'Brown'},
            {'first_name': 'Alex', 'last_name': 'Watson'},
            {'first_name': 'Jane', 'last_name': 'Smith'},
        ]

        # for student in students_list:
        #     Students.objects.create(**student)

        students_lst_for_bulk_fill = []
        for student in students_list:
            students_lst_for_bulk_fill.append(
                Student(**student)
            )

        Student.objects.bulk_create(students_lst_for_bulk_fill)