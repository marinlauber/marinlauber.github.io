## [marinlauber.gihub.io](https://marinlauber.github.io/)


#### How to solve the port in use error

```shell
'start_tcp_server': no acceptor (port is in use or requires root privileges) (RuntimeError)
```

Figure out what port ID is used by jekyll (in this case ruby)

```shell
lsof -i :4000
```

Then simply kill the specific port with its `PID`

```shell
kill -9 PID
```