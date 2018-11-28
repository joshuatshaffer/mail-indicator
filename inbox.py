#!/usr/bin/env python3

import mailbox
from file_observer import FileObserver

class InboxMonitor(object):
    def __init__(self, mailbox_path, unread_only=True):
        self.mailbox_path = mailbox_path
        self.unread_only = unread_only
        self.count = 0
        self.file_observer = FileObserver(self.mailbox_path, self.count_messages)
        self.count_messages()

    def count_messages(self):
        m = mailbox.Maildir(self.mailbox_path, create=False)
        self.count = 0
        m.lock()
        try:
            if self.unread_only:
                for msg in m:
                    if not 'S' in msg.get_flags():
                        self.count += 1
            else:
                self.count = len(m)
        finally:
            m.unlock()
        print("{} has {}".format(self.mailbox_path, self.count))
