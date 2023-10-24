---
title: "It's so <strong class='text-green'>easy</strong> to configure!"
layout: partials/home/install_code
overtitle: "Fast as lightning"
code: |
    ```caddyfile
    {
        # Enable FrankenPHP
        frankenphp
        # Configure when the directive must be executed
        order php_server before file_server
    }

    localhost {
        # Enable compression (optional)
        encode zstd gzip
        # Execute PHP files in the current directory and serve assets
        php_server
    }
    ```
---
Less than five lines of code: it's now all you need to start a production-grade PHP server (automatic HTTPS, HTTP/3, Zstandard compression...), powered by Caddy.