============
INSTALLATION
============

Ces instructions décrivent l'installation de *Choucas* sur un serveur de développement.


Requirements
------------

* Ubuntu Server 12.04 Precise Pangolin (http://releases.ubuntu.com/12.04/) or
  Ubuntu Server 14.04 Trusty Tahr (http://releases.ubuntu.com/14.04/) or
  Ubuntu Server 16.04 Xenial (http://releases.ubuntu.com/16.04/)


A first estimation on system resources is :

* 1 Go RAM
* 10 Go disk space


Installation
------------

Once the OS is installed (basic installation, with OpenSSH server), install
the last version with the following commands :

::

    curl https://raw.githubusercontent.com/makinacorpus/Geotrek/master/install.sh > install.sh
    chmod +x install.sh
    ./install.sh


You will be prompt for editing the base configuration file (``settings.ini``),
using the default editor.

:notes:

    If you leave *localhost* for the database host (``dbhost`` value), a
    Postgresql with PostGis will be installed locally.

    In order to use a remote server (*recommended*), set the appropriate values
    for the connection.
    The connection must be operational (it will be tested during install).


To make sure the application runs well after a reboot, try now : ``sudo reboot``.
And access the application ``http://yourserver/``.

You will be prompted for login, jump to :ref:`loading data section <loading data>`,
to create the admin user and fill the database with your data!



Then edit `etc/settings.ini` to update host variable and `geotrek/settings/custom.py`
to update IGN key.

Install Geotrek on the new server:

::

    ./install.sh

Restore database on the new server:

::

    sudo service geotrek stop
    sudo -u postgres psql -c "drop database geotrekdb;"
    sudo -u postgres psql -c "create database geotrekdb owner geotrek;"
    sudo -u postgres pg_restore -d geotrekdb geotrekdb.backup
    make update
    sudo service geotrek start


Tips and Tricks
---------------

* Use symlinks for uploaded files and cached tiles to avoid duplicating them on disk:

::

    mv var/tiles ~/tiles
    ln -s ~/tiles `pwd`/var/tiles

    mv var/media ~/media
    ln -s ~/media `pwd`/var/media
