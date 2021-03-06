python-logging-extra
====================

Additional handlers for the Python standard logging facility.


JabberHandler
-------------

::

  import logging
  from loggingx import JabberHandler, Account

  sender = Account(username = 'your-account@gmail.com',
                   password = 'your-password')

  destination = 'target-account@gmail.com'

  jabber_handler = JabberHandler(sender=sender, to=destination)

  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  logger.addHandler(jabber_handler)

  logger.debug("debug message")


SMTP_SSLHandler
---------------

Including SSL support, so it is able to send mail with gmail.

::

  import logging
  from loggingx import SMTP_SSLHandler, Server, Account

  sender = Account(username = 'your-account@gmail.com',
                   password = 'your-password')

  destination = 'target-account@gmail.com'

  gmail_smtp = Server(hostname='smtp.gmail.com',
                      port=587, ssl=True)

  smtp_handler = SMTP_SSLHandler(server  = gmail_smtp,
                                 sender  = sender,
                                 toaddrs = [destination],
                                 subject = 'SSL SMTP notification')

  logger = logging.getLogger()
  logger.addHandler(smtp_handler)

  logger.debug("debug message")


Notify handler
--------------




Debian
======

python-logging-extra is available as official Debian package.


- binary: http://packages.debian.org/sid/python-loggingx
- source: http://packages.debian.org/source/sid/python-logging-extra

Source repository
-----------------

- http://http://anonscm.debian.org/viewvc/python-modules/packages/python-logging-extra/
- svn+ssh://${ALIOTH_USER}@svn.debian.org/svn/python-modules/packages/python-logging-extra/


.. Local Variables:
..  coding: utf-8
..  mode: flyspell
..  ispell-local-dictionary: "american"
.. End:
