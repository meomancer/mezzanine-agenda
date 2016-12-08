__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '08/12/16'
from modeltranslation.translator import translator, TranslationOptions
from .models import Event


class TranslatedEvent(TranslationOptions):
    fields = ('title',)


translator.register(Event, TranslatedEvent)
