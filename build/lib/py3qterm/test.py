from py3qterm.backend import Session

session = Session()
# print(dir(session))
session.start("/bin/bash")
session.write(b"HELLO\n")
lc = session.last_change()
print(session.dump(), lc)
