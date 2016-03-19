# slack-zabbix-python

Better Slack integration for Zabbix 3.0

1. Create a New Media Type

With 3 parameters:

  * {ALERT.SENDTO}
  * {ALERT.SUBJECT}
  * {ALERT.MESSAGE}

2. Create a New Action

Subject:

.. code-block:: json

    {"{TRIGGER.STATUS}": "{TRIGGER.NAME}"}

Message body:

.. code-block:: json

    {"IP":"{IPADDRESS}","Trigger":"{TRIGGER.NAME}","Status":"{TRIGGER.STATUS}","Severity":"{TRIGGER.SEVERITY}","URL":"{TRIGGER.URL}","Hostname":"{HOSTNAME}","ItemValues":["{ITEM.NAME1} {ITEM.KEY1} in {HOST.NAME1}: {ITEM.VALUE1}","{ITEM.NAME2} {ITEM.KEY2} in {HOST.NAME2}: {ITEM.VALUE2}","{ITEM.NAME3} {ITEM.KEY3} in {HOST.NAME3}: {ITEM.VALUE3}"],"EventID":"{EVENT.ID}"}

