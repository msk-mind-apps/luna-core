=========
luna-core
=========


.. image:: https://img.shields.io/pypi/v/luna_core.svg
        :target: https://pypi.python.org/pypi/luna_core

.. image:: https://img.shields.io/travis/msk-mind-apps/luna_core.svg
        :target: https://travis-ci.com/msk-mind-apps/luna_core

.. image:: https://readthedocs.org/projects/luna-core/badge/?version=latest
        :target: https://luna-core.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Core library for luna packages.


* Free software: Apache Software License 2.0
* Documentation: https://luna-core.readthedocs.io.


Features
--------

* TODO

Configuration
-------------

- Setup $LUNA_HOME environment variable to point to a location where luna configs can be stored.

``export LUNA_HOME=~/.luna_home``

- Copy `conf/` folder to $LUNA_HOME/conf

``cp -r conf/ $LUNA_HOME/conf``

- In the `conf/` folder, copy `logging.default.yml` to `logging.cfg` and `datastore.default.yml` to `datastore.cfg` and modify the `.cfg` files.

``cd $LUNA_HOME/conf``

``cp logging.default.yml logging.cfg``

``cp datastore.default.yml datastore.cfg``


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
