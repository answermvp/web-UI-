import pytest
import json

# fixture
class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read())

    def test_user_password(self, users):
        for user in users:
            passwd = user['password']
            assert len(passwd) >= 6
            msg = 'user %s has a weak passpword' % (user['name'])
            assert passwd != 'password', msg
            assert passwd != '123456', msg
