#!/usr/bin/env python3

# Use pyinotify to watch the mail directory for changes.
# Use a timeout to avoid recounting for events that occur close together.
import pyinotify
from gi.repository import GObject

class FileObserver(object):
    def __init__(self, path, callback, debounce_period=500):
        self.path = path
        self.callback = callback
        self.debounce_period = debounce_period
        self.dirty = False

        self.wm = pyinotify.WatchManager()
        self.notifier = pyinotify.ThreadedNotifier(self.wm,
                                                   self._handle_inotify_event)
        self.notifier.start()
        self.wm.add_watch(self.path,
                          pyinotify.ALL_EVENTS)

        GObject.timeout_add(self.debounce_period, self._update_if_dirty)

    def _handle_inotify_event(self, event):
        self.dirty = True

    def _update_if_dirty(self):
        if self.dirty:
            self.callback()
            self.dirty = False
        # Return true to keep the timeout alive.
        return True
