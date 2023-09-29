---
title: "The Modern Php App Server, written in Go"
layout: home
blocs:
  - image: "img/box.svg"
    title: "Batteries included"
    content: >
      Shipped with a production-grade web server built on top of <a href="https://caddyserver.com/" target="_blank" rel="noreferrer noopener" class="link">Caddy</a>: automatic HTTPS, HTTP/2, HTTP/3, advanced logging, zstd and gzip compression...
  - image: "img/worker.svg"
    title: "Worker mode"
    content: >
      Boot your application once and keep it in memory! It is ready to handle incoming requests in a few milliseconds. FrankenPHP relies on Go's iconic feature: goroutines!
  - image: "img/one.svg"
    title: "Only one service"
    content: >
      FrankenPHP has been designed with simplicity in mind: only one service, only one binary! FrankenPHP doesn't need PHP-FPM, it uses its own SAPI specially handcrafted for Go web servers.
  - image: "img/rocket.svg"
    title: "Easy deploy"
    content: >
      FrankenPHP is a Cloud Native application shipped as a ready-to-use single Docker image. It is compatible with Kubernetes and all modern cloud platforms. If you don't want to use Docker, it's also supported.
  - image: "img/bulb.svg"
    title: "103 Early Hints"
    content: >
      <a href="https://httpwg.org/specs/rfc8297.html" target="_blank" rel="noreferrer noopener" class="link">Early Hints</a> are a brand new feature of the web platform that can improve <a href="https://blog.cloudflare.com/early-hints/" target="_blank" rel="noreferrer noopener" class="link">website load times by 30%</a>. FrankenPHP is the only PHP SAPI with Early Hints support!
  - image: "img/clock.svg"
    title: "Real-time"
    content: >
      FrankenPHP has a built-in <a href="https://mercure.rocks" target="_blank" rel="noreferrer noopener" class="link">Mercure</a> hub. Send events from your PHP apps to all connected browsers, they instantly receive the payload as a JavaScript event!
---
