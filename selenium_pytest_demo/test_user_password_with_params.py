import pytest
import json
users = json.loads(open('./users.test.json', 'r').read())
# 参数化的 fixture
class TestUserPasswordWithParam(object):
    @pytest.fixture(params=users)
    def user(self, request):
        return request.param

    def test_user_password(self, user):
        passwd = user['password']
        assert len(passwd) >= 6
        msg = 'user %s has a weak password' %(user['name'])
        assert passwd != 'password', msg
        assert passwd != '123456', msg