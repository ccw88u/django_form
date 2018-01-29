import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_forms.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from form_basic.models import Reguser
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']


def populate(N=5):
    for entry in range(N):
        ## get the topic for the entry
        
        fake_first_name = fakegen.name()
        fake_last_name = fakegen.name()
        fake_addr = fakegen.address()
        fake_tel = fakegen.phone_number()
        fake_email = fakegen.email()

        ## Create the new Reguser entry
        add_Reguser = Reguser.objects.get_or_create(first_name=fake_first_name,
                                                last_name=fake_last_name, addr=fake_addr,
                                                tel=fake_tel, email=fake_email)[0]


if __name__ == '__main__':
    addNum = 30
    print("populating script!")    
    populate(addNum)
    print("add:%s doned" % addNum)
    print("populating complete!")
