"""Controller for speaking with robot"""
from speaker.models import robot


def talk():
    """Function to speak with hello"""
    talk_robot = robot.TalkRobot()
    talk_robot.hello()
    talk_robot.day_of_the_week_for_birthday()
    talk_robot.thank_you()