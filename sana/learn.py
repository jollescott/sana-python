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


SANA_HEADERS = {'X-API-KEY': SANA_API_KEY}


####################
# Asset Management #
####################


class AssetTag():

    def __init__(self, name, value):
        self.name = str(name)
        self.value = str(value)


class LearnAsset():

    def __init__(self, id, asset_type, tags=None, description='', content_url='', metadata=None):
        self.id = str(id)
        self.type = asset_type

        self.tags = tags
        self.description = str(description)
        self.content_url = str(content_url)
        self.metadata = metadata


def create_or_update_asset(asset):
    url = '{0}/v1/assets/{1}'.format(get_base_url(), asset.id)
    r = requests.put(url, json=asset.__dict__, headers=SANA_HEADERS)

    return r.ok


def delete_asset(id):
    url = '{0}/v1/assets/{1}'.format(get_base_url(), id)
    r = requests.delete(url, headers=SANA_HEADERS)

    return r.ok


def get_asset(id):
    url = '{0}/v1/assets/{1}'.format(get_base_url(), str(id))
    r = requests.get(url, headers=SANA_HEADERS)

    if r.ok:
        return r.json()
    else:
        raise BaseException(r.text)

def create_or_update_assets(assets):
    url = '{0}/v1/assets'.format(get_base_url())

    bulk = {
        'assets': [asset.__dict__ for asset in assets]
    }

    r = requests.put(url, json=bulk, headers=SANA_HEADERS)

    return r.ok


def delete_assets(ids):
    url = '{0}/v1/assets?asset_ids={1}'.format(get_base_url(), json.dumps(ids))
    r = requests.delete(url, headers=SANA_HEADERS)

    return r.ok


def get_assets(ids):
    query = ''

    for id in ids:
        if query != '':
            query = query + ','

        query = query + str(id)

    url = '{0}/v1/assets?asset_ids={1}'.format(get_base_url(), query)
    r = requests.get(url, headers=SANA_HEADERS)

    if r.ok:
        return r.json()
    else:
        raise BaseException(r.text)


####################
# Views Management #
####################


class ViewItemAttribute():
    def __init__(self, partner_difficulty=0):
        self.partner_difficulty = partner_difficulty


class ViewItem():
    def __init__(self, asset_id, path, attributes=None):
        self.asset_id = asset_id

        if path.startswith('/') is False:
            raise BaseException('Paths must start with a forward slash')

        self.path = path
        self.attributes = attributes


class LearnView():
    def __init__(self, name, items, path='', description='', ordered=False):
        self.name = str(name)
        self.path = str(path)
        self.description = str(description)
        self.ordered = ordered
        self.items = [item.__dict__ for item in items]


def create_or_update_view(id, view):
    url = '{0}/v1/views/{1}'.format(get_base_url(), id)
    r = requests.put(url, json=view.__dict__, headers=SANA_HEADERS)

    return r.ok


def delete_view(id):
    url = '{0}/v1/views/{1}'.format(get_base_url(), id)
    r = requests.delete(url, headers=SANA_HEADERS)

    return r.ok


def get_view(id):
    url = '{0}/v1/views/{1}'.format(get_base_url(), id)
    r = requests.get(url, headers=SANA_HEADERS)

    if r.ok:
        return r.json()
    else:
        raise BaseException(r.text)


def get_all_views(last_view_id=None, limit=None):
    url = '{0}/v1/views'.format(get_base_url())

    params = []

    if last_view_id is not None:
        params.append(('last_view_id', last_view_id))

    if limit is not None:
        params.append(('limit', limit))

    if len(params) > 0:
        url = url + '?'

        for param in params:
            url = url + '&{0}={1}'.format(param[0], param[1])

    r = requests.get(url, headers=SANA_HEADERS)

    if r.ok:
        return r.json()
    else:
        raise BaseException(r.text)


######################
# Realtime Endpoints #
######################


class UserEventAttribute():
    def __init__(self, view_id, asset_id, result, score=None, time_spent_ms=None):
        self.view_id = str(view_id)
        self.asset_id = str(asset_id)
        self.result = str(result)
        self.score = float(score)
        self.time_spent_ms = int(time_spent_ms)


class LearnUser():
    def __init__(self, id, user_type, test_cell=None):
        self.id = str(id)
        self.type = str(user_type)
        self.test_cell = str(test_cell)


class UserEventTag():
    def __init__(self, name, value):
        self.name = name
        self.value = value


class UserEvent():
    def __init__(self, user, event_type, attributes, timestamp, recommendation_context=None, tags=None, is_offline_event=None, metadata=None):
        self.user = user
        self.type = str(event_type)
        self.attributes = [attribute.__dict__ for attribute in attributes]
        self.timestamp = str(timestamp)
        self.recommendation_context = str(recommendation_context)
        
        if tags is not None:
            self.tags = [tag.__dict__ for tag in tags]
        
        self.is_offline_event = is_offline_event
        self.metadata = metadata


def post_user_events(user_events):
    url = '{0}/v1/user-events'.format(get_base_url())

    bulk = {
        'user_events': [event.__dict__ for event in user_events]
    }

    r = requests.post(url, json=bulk, headers=SANA_HEADERS)

    return r.ok


class AssetFilter():
    def __init__(self, asset_types, paths, tags=None):
        self.asset_types = asset_types
        self.paths = paths
        self.tags = tags


class Mode():
    def __init__(self, mode_type, attributes):
        self.type = mode_type
        self.attributes = attributes


def next_assets(user, view_id, asset_filter, mode, limit, user_events=None):
    url = '{0}/v1/next-assets'.format(get_base_url())

    data = {
        'user': user,
        'view_id': str(view_id),
        'filter': asset_filter.__dict__,
        'mode': mode.__dict__,
        'limit': limit
    }

    if user_events is not None:
        data['user_events'] = user_events

    r = requests.post(url, json=data, headers=SANA_HEADERS)

    if r.ok:
        return r.json()
    else:
        raise BaseException(r.text)


def user_filter_status(user_id, view_id, filters):
    url = '{0}/v1/user-filter-status'.format(get_base_url())

    data = {
        'user_id': user_id,
        'view_id': view_id,
        'filters': filters
    }

    r = requests.post(url, json=data, headers=SANA_HEADERS)

    if r.ok:
        return r.json()
    else:
        raise BaseException(r.text)
