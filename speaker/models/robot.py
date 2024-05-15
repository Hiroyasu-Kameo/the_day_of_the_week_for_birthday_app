# Zeller's congruence

import sys
from decimal import *


"""Defined a robot model """
from speaker.views import console

DEFAULT_ROBOT_NAME = 'Lucia'


class Robot(object):
    """Base model for Robot."""

    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='', speak_color='blue'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color;

    def hello(self):
        """Returns words to the user that the robot speaks at the beginning."""
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({
                'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break

class TalkRobot(Robot):
    def __init__(self, name=DEFAULT_ROBOT_NAME):
        super().__init__(name=name)

    def _hello_decorator(func):
        """Decorator to say a greeting if you are not greeting the user."""
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @_hello_decorator
    def day_of_the_week_for_birthday(self):
        while True:
            template = console.get_template('what_year.txt', self.speak_color)
            year = input(template.substitute({'robot_name': self.name}))

            if year and(int(year) >= 1):
                break

        while True:
            template = console.get_template('what_month.txt', self.speak_color)
            month = input(template.substitute({'robot_name': self.name}))

            if month and(int(month) >= 1 and int(month) <= 12):
                break

        while True:
            template = console.get_template('what_day.txt', self.speak_color)
            date = input(template.substitute({'robot_name': self.name}))

            if date and(int(date) >= 1 and int(date) <= 31):
                break

        if int(month) <= 2:
            month = str(int(month) + 12)
            year = str(int(year) - 1)

        j = Decimal(year[0:2])
        k = Decimal(int(year) % 100)
        m = Decimal(month)
        q = Decimal(date)

        # ツェラーの公式
        h = (q + (((m + 1) * 26) // 10) + k + (k // 4) + (j // 4) - (2 * j)) % 7
        week = ('Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')# 値を変更することはないので、タプルにする。
        #week = ('土', '日', '月', '火', '水', '木', '金')

        template = console.get_template('birth_week.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name,
            'week': week[int(h)]
        }))

    @_hello_decorator
    def thank_you(self):
        """Show words of appreciation to users."""
        template = console.get_template('good_by.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name
        }))