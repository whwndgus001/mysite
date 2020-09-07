from django.test import TestCase
import guestbook.models as mysitemodel


def test():
    mysitemodel.delete(2, '1234')


test()