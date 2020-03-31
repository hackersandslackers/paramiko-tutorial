# Paramiko SSH & SCP Tutorial

![Python](https://img.shields.io/badge/Python-v^3.8-blue.svg?logo=python&longCache=true&logoColor=white&colorB=5e81ac&style=flat-square&colorA=4c566a)
![Paramiko](https://img.shields.io/badge/Paramiko-v^2.7.0-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![SCP](https://img.shields.io/badge/SCP-v0.13.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)
![GitHub Last Commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat-square&colorA=4c566a&colorB=a3be8c&logo=GitHub)
[![GitHub Issues](https://img.shields.io/github/issues/hackersandslackers/paramiko-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/paramiko-tutorial/issues)
[![GitHub Stars](https://img.shields.io/github/stars/hackersandslackers/paramiko-tutorial.svg?style=flat-square8&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/paramiko-tutorial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/hackersandslackers/paramiko-tutorial.svg?style=flat-square&colorA=4c566a&logo=GitHub&colorB=ebcb8b)](https://github.com/hackersandslackers/paramiko-tutorial/network)

![Paramiko Tutorial](https://github.com/hackersandslackers/paramiko-tutorial/blob/master/.github/paramiko-4-1@2x.jpg)

Source code for the accompanying tutorial found here: https://hackersandslackers.com/ssh-scp-in-python-with-paramiko/

## Getting Started

Installation is recommended with Pipenv:

```shell
$ git clone https://github.com/hackersandslackers/paramiko-tutoral.git
$ cd paramiko-tutorial
$ pipenv shell
$ pipenv update
$ python3 main.py
```

Alternatively, try installing via `setup.py`:

```shell
$ git clone https://github.com/hackersandslackers/paramiko-tutoral.git
$ cd paramiko-tutorial
$ python3 setup.py run
```

The following environment variables are required to run this script:

* `REMOTE_HOST`: IP address or URL of remote host.
* `REMOTE_USERNAME`: Username for remote host.
* `SSH_KEY`: /path/to/remote/host/sshkey.pem
* `REMOTE_PATH` _(optional)_: Remote directory to serve as destination for file uploads.


-----

**Hackers and Slackers** tutorials are free of charge. If you found this tutorial helpful, a [small donation](https://www.buymeacoffee.com/hackersslackers) would be greatly appreciated to keep us in business. All proceeds go towards coffee, and all coffee goes towards more content.
