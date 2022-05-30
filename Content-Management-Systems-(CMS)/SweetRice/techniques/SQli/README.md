# SweetRice - SQL injection

## Requirements

 - A valid **username and password** of a user with **admin rights** on the SweetRice.

## Exploitation

### Accessing the dashboard

Connect with a user with administrative rights on the SweetRice at [http://TARGET/as/](http://TARGET/as).

![](./imgs/dashboard.png)

### Go to DATA > SQL Execute page

You can go directly on this page http://TARGET/as/?type=data&mode=sql_execute

![](./imgs/SQLi_page.png)

### Capture a Request

We send a request from the page, capture it with Burp and save the request in a file

![](./imgs/Request_burp.png)

### Retreive data using sqlmap

To get data from the database, use sqlmap with the request.

![](./imgs/sqlmap.png)
![](./imgs/sqlmap2.png)

## References

- https://www.sweetrice.xyz/
- https://github.com/sqlmapproject/sqlmap
- https://portswigger.net/burp