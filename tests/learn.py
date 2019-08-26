from sana import SANA_API_KEY, SANA_API_REGION

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
    pass

def delete_asset(id):
    pass

def get_asset(id):
    pass

def create_or_update_assets(assets):
    pass

def delete_assets(ids):
    pass

def get_assets(ids):
    pass


####################
# Views Management #
####################


######################
# Realtime Endpoints #
######################