from lib.actions import BaseAction
import yaml

__all__ = [
    'ListCloudsAction'
]


class ListCloudsAction(BaseAction):

    def run(self):
        conf = None
        with open('/opt/stackstorm/packs/libcloud/config.yaml', 'r') as outfile:
            conf = yaml.load(outfile)
        return conf['credentials']
