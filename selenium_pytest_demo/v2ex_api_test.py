import requests
import pytest

# class TestV2exApiWithParams(object):
#     """
#     使用fixture参数化接口入参
#     """
#     domain = 'https://www.v2ex.com/'

#     @pytest.fixture(params=['python', 'java', 'go', 'nodejs'])
#     def lang(self, request):
#         return request.param

#     def test_node(self, lang):
#         path = 'api/nodes/show.json?name=%s' % (lang)
#         url = self.domain + path
#         res = requests.get(url).json()
#         assert res['name'] == lang
#         assert 0

class TestV2exApiWithParams(object):
    """
    使用fixture参数化测试预期结果
    """
    domain = 'https://www.v2ex.com/'
    @pytest.mark.parametrize('name, node_id', [('python' ,90), ('java', 63), ('go', 375), ('nodejs', 436)])

    def test_node(self, name, node_id):
        path = 'api/nodes/show.json?name=%s' % (name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == name
        assert res['id'] == node_id
        assert 0