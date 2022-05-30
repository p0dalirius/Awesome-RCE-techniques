# SweetRice - Upload a plugin

## Requirements

 - A valid **username and password** of a user with **admin rights** on the SweetRice.

## Exploitation

### Accessing the dashboard

Connect with a user with administrative rights on the SweetRice at [http://TARGET/as/](http://TARGET/as).

![](./imgs/dashboard.png)

### Installing the plugin

Then go on the "Plugin list" page.

![](./imgs/upload_plugin_sweetrice.png)

### Get you favorite PHP Reverse shell, zip it, and upload it

Here we using the pentestmonkey's reverse shell (https://github.com/pentestmonkey/php-reverse-shell)

![](./imgs/upload_plugin_sweetrice2.png)

![](./imgs/upload_wp_term.png)

### Using the plugin

To use the webshell plugin, just access this page http://TARGET/wordpress/wp-admin/tools.php?page=wpterm

![](./imgs/wpterm_webshell.png)

## References