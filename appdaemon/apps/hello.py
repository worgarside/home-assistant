from __future__ import annotations

import appdaemon.plugins.hass.hassapi as hass

#
# Hello World App
#
# Args:
#


class HelloWorld(hass.Hass):
    def initialize(self):
        self.log("Hello from AppDaemon")
        self.log("You are now ready to run Apps!")
