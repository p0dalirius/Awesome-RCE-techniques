# Wordpress - Upload a plugin

## Requirements

 - A valid **username and password** of a user with **admin rights** on the Wordpress.

## Exploitation

### Installing the plugin

Connect with a user with administrative rights on the Wordpress at [http://TARGET/wp-login.php](http://TARGET/wp-login.php).

![](./imgs/)

Then go on the "Manage plugins" page.

![](./imgs/)

Now, upload the plugin [wpterm](./wpterm.1.1.9.zip) to get a webshell plugin into Wordpress admin console.

![](./imgs/)

### Using the plugin



## References
 - https://wordpress.org/plugins/wpterm/