pymitv
======

A Python 3 based control of the Mi Tv 3(s)

.. figure:: https://9to5google.files.wordpress.com/2016/03/xiaomi-mi-tv-3s.jpg?quality=82&w=1600&h=1000
   :alt: The Mi TV 3s 65-inch

   The Mi TV 3s 65-inch

Introduction
------------

This package was developed to interface with the Xiaomi TV 3 series
through their local HTTP API using Python. The package has both the
ability to discover TVs and control them. The TV lineup in question is
this `one.`_ It should be noted, that all the TV logic and hardware is
in the soundbar. Thus, if you have a soundbar that looks identical to
the one in the picture, you should be golden with this library.

Supported models
''''''''''''''''

-  Mi TV 3s (all sizes)

Not sure if supported models
''''''''''''''''''''''''''''

-  Mi TV 4A (all sizes)

Installing
----------

Easy as pie! Just use ``pip``.

**Most systems**

::

    pip install pymitv

**Or if you have multiple Python versions**

::

    python3 -m pip install pymitv

Usage
-----

The package includes three modules: ``Discover``, ``Control`` and
``TV``. Each have their role, as implied by their names.

Discovering TVs
~~~~~~~~~~~~~~~

``Discover.scan()``
^^^^^^^^^^^^^^^^^^^

This method is used to scan the local network for TVs.

**Arguments**

+-----------------+-----------------+-----------------+-----------------+
| Name            | Required        | Default value   | Purpose         |
+=================+=================+=================+=================+
| ``stop_on_first | No              | ``True``        | Whether or not  |
| ``              |                 |                 | the method      |
|                 |                 |                 | should continue |
|                 |                 |                 | scanning for    |
|                 |                 |                 | TVs after       |
|                 |                 |                 | finding its     |
|                 |                 |                 | first one. Only |
|                 |                 |                 | needed for      |
|                 |                 |                 | people with     |
|                 |                 |                 | multiple Xiaomi |
|                 |                 |                 | TVs.            |
+-----------------+-----------------+-----------------+-----------------+
| ``base_ip``     | No              | ``0``           | Instead of      |
|                 |                 |                 | looking for the |
|                 |                 |                 | base IP, you    |
|                 |                 |                 | can give it to  |
|                 |                 |                 | the function in |
|                 |                 |                 | the format of   |
|                 |                 |                 | ``192.168.0.``  |
+-----------------+-----------------+-----------------+-----------------+
| ``speedy_gonzal | No              | ``False``       | Speeds up the   |
| ez``            |                 |                 | scan            |
|                 |                 |                 | drastically at  |
|                 |                 |                 | the risk of     |
|                 |                 |                 | missing a TV.   |
+-----------------+-----------------+-----------------+-----------------+

**Example usage**

.. code:: python

    import Discover from pymitv

    discover = Discover.scan(speedy_gonzalez=True)
    print(discover)

``Discover.checkIp()``
^^^^^^^^^^^^^^^^^^^^^^

Used by ``Discover.scan()`` to check if a TV is present at the IP.

**Arguments**

+-----------------+-----------------+-----------------+-----------------+
| Name            | Required        | Default value   | Purpose         |
+=================+=================+=================+=================+
| ``ip``          | Yes             | None            | The IP to       |
|                 |                 |                 | check.          |
+-----------------+-----------------+-----------------+-----------------+
| ``fast``        | No              | ``False``       | Speeds up the   |
|                 |                 |                 | scan            |
|                 |                 |                 | drastically at  |
|                 |                 |                 | the risk of     |
|                 |                 |                 | missing a TV.   |
+-----------------+-----------------+-----------------+-----------------+

**Example usage**

.. code:: python

    import Discover from pymitv

    print(Discover().checkIp('192.168.0.45'))

--------------

Controlling TVs
~~~~~~~~~~~~~~~

This is where the ``Control`` class comes in handy. The class has a
bunch of predefined keystrokes: - ``turn_on`` - ``turn_off`` - ``sleep``
- ``wake`` - ``up`` - ``down`` - ``right`` - ``left`` - ``home`` -
``enter`` - ``back`` - ``menu`` - ``volume_up`` - ``volume_down``

``Control.sendKeystrokes(ip, keystrokes)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sends a set of keystrokes to a TV at ``ip``

**Arguments**

+-----------------+-----------------+-----------------+-----------------+
| Name            | Required        | Default value   | Purpose         |
+=================+=================+=================+=================+
| ``ip``          | Yes             | None            | The IP of the   |
|                 |                 |                 | TV to send      |
|                 |                 |                 | keystroke(s)    |
|                 |                 |                 | to.             |
+-----------------+-----------------+-----------------+-----------------+
| ``keystrokes``  | Yes             | None            | Keystroke(s) to |
|                 |                 |                 | send. E.g.      |
|                 |                 |                 | ``Control.sleep |
|                 |                 |                 | ``              |
+-----------------+-----------------+-----------------+-----------------+

**Using the ``wait`` keystroke**

Using this keyword in a sequence of keystrokes will make the method
sleep for 0.4 seconds which is the effective time it takes for the TV to
listen to new keystrokes.

**Example usage**

.. code:: python

    import Control from pymitv

    Control().sendKeystrokes(Control.sleep)

TV as a class
~~~~~~~~~~~~~

There is a class representation of the TV which will take an IP address.
It has a range of control functions, and will keep track of on/off state
(provided the script running is kept alive).

**Example usage**

.. code:: python

    from pymitv import TV

    tv = TV('192.168.0.41')

    tv.is_on() #Return False
    tv.wake() #Will wake the TV
    tv.up() #Will press key up

All keystrokes from the ``Control`` class are available with the
exception of ``turn_on``. This is because, you can’t actually turn on
the TV if it’s completely off. Instead, use ``wake`` and ``sleep``.

Accessing the local API exposed by the TV
-----------------------------------------

This can be useful if you don’t wish to use the Python package (this
one), but you’d rather implement your own version. Below you’ll find
everything you need.

Finding the TV IP
^^^^^^^^^^^^^^^^^

To find the IP of your TV you need to scan your network for clients. You
can use an application like `*Advanced IP Scanner*`_ for Windows and
`*LanScan*`_ for MacOS. Both these applications resolves the MAC address
to give you the name of the manufacturer. However, if you have multiple
Xiaomi products it can still prove difficult to find the right one.
**Fear not!** The MAC address should start with ``00:9E:C8``.

Check TV status
^^^^^^^^^^^^^^^

To check if the TV is on, use the following request:
``http://TV_IP:6095/request?action=isalive``

The above will return something along the lines of:

.. code:: json

    {
        "status": 0,
        "msg": "success",
        "data": {
            "devicename": "客厅的小米电视",
            "ip": "TV_IP:6095",
            "feature": ["power"],
            "url": ["http:\/\/bilibili.kankanews.com\/video\/av\\d+\/", "http:\/\/www.bilibili.tv\/video\/av\\d+\/"],
            "platform": 606,
            "build": 1381,
            "version": 16777500
        }
    }

**BEWARE! If the TV is in standby mode, this request will still return
as if it were on. Currently there is no way to check if the TV is
actually on.**

Send keystroke
^^^^^^^^^^^^^^

To send a keystroke use the following request:
``http://TV_IP:6095/controller?action=keyevent&keycode=KEYCODE``

Instead of ``KEYCODE``, you should write an actual keycode. These are
the available ones

.. _*Advanced IP Scanner*: http://www.advanced-ip-scanner.com/
.. _*LanScan*: https://itunes.apple.com/us/app/lanscan/id472226235?mt=12
.. _one.: http://www.mi.com/en/mitv3s/65/
