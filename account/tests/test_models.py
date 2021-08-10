import pytest

from account.models import Profile, Address
from model_bakery import baker

@pytest.mark.django_db
def test_profile_create():
    profile = baker.make(Profile)
    assert Profile.objects.count() == 1

@pytest.mark.django_db
def test_address_create():
    address = baker.make(Address)
    assert Address.objects.count() == 1

@pytest.mark.django_db
def test_get_full_name_of_user():
    profile = baker.make(Profile)
    assert profile != None and profile != ''