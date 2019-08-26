from httmock import urlmatch, HTTMock, all_requests
from sana.learn import create_or_update_asset, LearnAsset


@urlmatch(path='/v1/assets/1')
def create_mock(url, request):
    return {
        'status_code': 200
    }


def test_create_asset():
    asset = LearnAsset(
        1, 'unittest', ['test', 'test2'], content_url='www.google.com')

    with HTTMock(create_mock):
        assert create_or_update_asset(asset) == True
