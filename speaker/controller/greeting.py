"""Controller for speaking with guide"""
from speaker.models import guide


def talk():
    """Function to speak with hello"""
    talk_guide = guide.TalkGuide()
    talk_guide.hello()
    talk_guide.the_day_of_the_week_for_birthday()
    talk_guide.thank_you()