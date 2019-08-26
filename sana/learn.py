from sana import SANA_API_KEY, SANA_API_REGION
import requests
import json


#############
# Utilities #
#############


def get_base_url():
    if SANA_API_REGION == 'US':
        return 'https://us.api.sanalabs.com'
    else:
        return 'https://api.sanalabs.com'


####################
# Asset Management #
####################


class LearnAsset():

    def __init__(self, id, asset_type, tags=None, description='', content_url='', metadata=None):
        self.id = id
        self.type = asset_type

        self.tags = tags
        self.description = description
        self.content_url = content_url
        self.metadata = metadata


def create_or_update_asset(asset):
    url = '{0}/v1/assets/{1}'.format(get_base_url(), asset.id)
    r = requests.put(url, asset)

    return r.ok


def delete_asset(id):
    url = '{0}/v1/assets/{1}'.format(get_base_url(), id)
    r = requests.delete(url)

    return r.ok


def get_asset(id):
    url = '{0}/v1/assets/{1}'.format(get_base_url(), id)
    r = requests.get(url)

    return r.json()


def create_or_update_assets(assets):
    url = '{0}/v1/assets'.format(get_base_url())
    r = requests.put(url, assets)

    return r.ok()


def delete_assets(ids):
    url = '{0}/v1/assets?asset_ids={1}'.format(get_base_url(), json.dumps(ids))
    r = requests.delete(url)

    return r.ok


def get_assets(ids):
    url = '{0}/v1/assets?asset_ids={1}'.format(get_base_url(), json.dumps(ids))
    r = requests.get(url)

    return r.json()


####################
# Views Management #
####################

class LearnView():
    def __init__(self, name, path='', description='', ordered=False, items):
        self.name = name
        self.path = path
        self.description = description
        self.ordered = ordered
        self.items = items


def create_or_update_view(id, view):
    url = '{0}/v1/views/{1}'.format(get_base_url(), id)
    r = requests.put(url, view)

    return r.ok()


def delete_view(id):
    url = '{0}/v1/views/{1}'.format(get_base_url(), id)
    r = requests.delete(url)

    return r.ok()


def get_view(id):
    url = '{0}/v1/views/{1}'.format(get_base_url(), id)
    r = requests.get(url)

    return r.json()

def get_all_views(last_view_id=None,limit=None)
    url = '{0}/v1/views'.format(get_base_url())

    params = []

    if last_view_id is not None:
        params.append(('last_view_id',last_view_id))

    if limit is not None:
        params.append(('limit', limit))

    if len(params) > 0:
        url = url + '?'

        for param in params:
            url = url + '&{0}={1}'.format(param[0], param[1])

    r = requests.get(url)
    return r.json()

######################
# Realtime Endpoints #
######################
