# GitHub Multi-Repo Management Monolith

This is sample code for a OSCON 2019 tutorial: https://conferences.oreilly.com/oscon/oscon-or/public/schedule/detail/76039

## Pre-requisites

* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
  * [OS X](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0.8-130520-OSX.dmg)
  * [Windows](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0.8-130520-Win.exe)
  * [Ubuntu 18.04 / 18.10 / 19.04 / Debian 10](https://download.virtualbox.org/virtualbox/6.0.8/virtualbox-6.0_6.0.8-130520~Ubuntu~bionic_amd64.deb)
  * [openSUSE 15.0](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0-6.0.8_130520_openSUSE150-1.x86_64.rpm)
  * [Fedora 29 / 30](https://download.virtualbox.org/virtualbox/6.0.8/VirtualBox-6.0-6.0.8_130520_fedora29-1.x86_64.rpm)
* [Docker](https://docs.docker.com/install)
  * [OS X](https://download.docker.com/mac/stable/Docker.dmg)
  * [Windows](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe)
  * [Linux x86](https://download.docker.com/linux/static/stable/x86_64/docker-17.03.0-ce.tgz)
* [Clone GitHub Microservices](https://github.com/thinkingserious/github-microservices)

## Installation

```bash
git clone https://github.com/thinkingserious/github-monolith.git
cd github-monolith
```

* Update `.env_example`.
* Open `examples/*` and update the repos in `all_repos`.
* Open `examples/send_emails` and update the email in the `send_email` function.
* Open `examples/send_sms` and update the to and from phone numbers in the `send_sms` function.

```bash
mv ./.env_example ./.env
source .env
docker-machine create -d virtualbox github-manager-monolith
eval "$(docker-machine env github-manager-monolith)"
export GITHUB_MANAGER_IP="$(docker-machine ip github-manager-monolith)"
docker-compose -f docker-compose-dev.yml up -d --build
curl http://$GITHUB_MANAGER_IP
```

## Quickstart

Go to `http://<$GITHUB_MANAGER_IP>` in your browser. If you see "Hello World", you're good to go.

Run the examples

```bash
virtualenv venv
source ./venv/bin/activate
pip install -r web/requirements.txt
python examples/get_all_issues.py
python examples/get_all_prs.py
python examples/send_email.py
python examples/send_sms.py
```

# References
* https://github.com/sendgrid/github-automation
* https://github.com/sendgrid/dx-automator
* https://github.com/miguelgrinberg
* https://github.com/testdrivenio/testdriven-app-2.5
* https://github.com/realpython/orchestrating-docker
* http://flask.pocoo.org/docs/1.0
