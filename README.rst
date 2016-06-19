Example project
===============

This is an example project for `issue #138 of django-admin-sortable <https://github.com/iambrandontaylor/django-admin-sortable/issues/138>`_

Setup
-----

In a virtualenv::

    pip install -r requirements.txt
    ./manage.py migrate --run-syncd
    ./manage.py createsuperuser --username admin --email admin@example.com
    ./manage.py loaddata fixtures/project.json
    ./manage.py runserver

Then go to `<http://localhost:8000/admin/project/album/1/change/>`_ and you'll see these extra drag / drop markers:

.. image:: https://raw.githubusercontent.com/jaap3/adminsortable-issue-138/master/screenshot.png
    :align: center
