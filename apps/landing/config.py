import os
from livesettings import config_register, ConfigurationGroup, StringValue
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

def _get_themes():
        s_path = settings.TEMPLATE_DIRS[0]
        result = os.listdir(s_path)
        result.remove('zero')
        return [(x,x) for x in result]

# First, setup a grup to hold all our possible configs
MYAPP_GROUP = ConfigurationGroup(
    'landing',               # key: internal name of the group to be created
    _('Landing Config'),  # name: verbose name which can be automatically translated
    ordering=0             # ordering: order of group in the list (default is 1)
    )

config_register(StringValue(
        MYAPP_GROUP,
        'THEME',
        description=_("Theme For The Web"),
        help_text=_("Default Theme."),
        choices=_get_themes(),
        default=_get_themes()[0][1]
    ))