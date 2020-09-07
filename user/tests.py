from django.test import TestCase

import user.models as usermodels
# Create your tests here.


def text_usermodels_fetchone():
    result = usermodels.fetchone('michol@gmail.com', '1234')
    print(result)

text_usermodels_fetchone()