## 1. Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install django mysqlclient
```
> **Error** while trying to install mysqlclient:  
```bash
...
  Exception: Can not find valid pkg-config name.
  Specify MYSQLCLIENT_CFLAGS and MYSQLCLIENT_LDFLAGS env vars manually
  ----------------------------------------
ERROR: Command errored out with exit status 1:
...
```
> **Solution**
```bash
sudo apt install python3-dev default-libmysqlclient-dev build-essential
```
