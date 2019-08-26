def test_base_url():
    import sana
    sana.SANA_API_REGION = 'US'

    from sana.learn import get_base_url

    assert get_base_url() == 'https://us.api.sanalabs.com'
