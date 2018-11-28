#!/usr/bin/python3
import mailbox

def count_messages(mailbox_path, unread_only=True):
    m = mailbox.Maildir(mailbox_path, create=False)
    count = 0
    m.lock()
    try:
        if unread_only:
            for msg in m:
                if not 'S' in msg.get_flags():
                    count += 1
        else:
            count = len(m)
    finally:
        m.unlock()
    return count

def main():
    print (count_messages('/mnt/data-i/joshua/mail/gmail/INBOX'))
    print (count_messages('/mnt/data-i/joshua/mail/three-shaffers/INBOX'))


if __name__ == "__main__":
    main()
