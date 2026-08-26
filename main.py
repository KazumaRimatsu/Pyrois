"""
Test
A Class Widgets plugin.
"""

from ClassWidgets.SDK import CW2Plugin, PluginAPI


class Plugin(CW2Plugin):
    def __init__(self, api: PluginAPI):
        super().__init__(api)

    def on_load(self):
        super().on_load()
        print(f"Test loaded")

    def on_unload(self):
        print(f"Test unloaded")
