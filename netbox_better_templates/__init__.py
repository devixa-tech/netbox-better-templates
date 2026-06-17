from netbox.plugins import PluginConfig
from .monkey_patches import (
    patch_config_templates,
    patch_export_templates,
    patch_custom_links,
)

__version__ = "1.0.2"
__description__ = "Adds some functionality to netbox templates and config render."
__authors__ = [
    {"name": "devixa-dev", "email": "hmohammad2520@gmail.com"},
]
__keywords__ = [
    "python",
    "netbox",
    "provisioning",
    "template",
    "jinja",
    "jinja2",
]


class NetboxBetterTemplatesConfig(PluginConfig):
    name = "netbox_better_templates"
    verbose_name = "Better Templates"
    description = __description__
    author = __authors__[0]["name"]
    author_email = __authors__[0]["email"]
    version = __version__
    base_url = "better-templates"

    def ready(self):
        super().ready()

        patch_config_templates()
        patch_export_templates()
        patch_custom_links()

    def __str__(self) -> str:
        return self.name

config = NetboxBetterTemplatesConfig