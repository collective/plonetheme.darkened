Introduction
============

The ``plonetheme.darkened`` package uses the *theming & packaging* features
available in `plone.app.theming`_ to make the theme `darkened`_ easily
available in `Plone 4.1`_ or higher.

.. image:: https://raw.github.com/collective/plonetheme.darkened/master/plonetheme/darkened/static/preview.png

Installation
============

Buildout
--------

To install this with buildout:

* Add ``plonetheme.darkened`` to your ``plone.recipe.zope2instance`` section's ``eggs`` parameter::

    [instance]
    recipe = plone.recipe.zope2instance
    ...
    eggs =
        ...
        plonetheme.darkened

* Re-run buildout, e.g. with::

    $ ./bin/buildout


.. _`darkened`: http://www.freecsstemplates.org/preview/darkened/
.. _`plone.app.theming`: http://pypi.python.org/pypi/plone.app.theming
.. _`Plone 4.1`: http://pypi.python.org/pypi/Plone/4.1rc2
