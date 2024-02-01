# space
Utility scripts for workspace container management.

## Usage

1) Clone this repo.
2) Set environment variable $SPACE refers to where the repo is.
3) Execute ```spacen```

### Host-side scripts
- spacen: Create container and mount host directories to the container.
  <br/>```$ spacen (image)```
- space-startup: Piece of script that used to prepare the container before starting it.
  <br/>```$ space-startup```
- space-authkey-add: Move the SSH private keys generated in ```$SPACE/opt/keys/``` to ```$HOME/.ssh/``` at host.
- space.py: Login as user $1 in container.
  <br/>```$ space (user) [command]```

Example
```shell
$ spacen fedora:39          # Create and setup the new container.
$ space root                # Login as root.
$ space root /bin/firefox   # Run FireFox as root.
```

### Container-side scripts

- authkey-gen: Generate SSH keypair for current user, invoked by *authkey-newuser*.
  <br/>```$ authkey-gen```
- authkey-newuser: Generate SSH keypair for user, and move the pubkey to ```/opt/keys``` in container. Run it as root in container.
  <br/>```$ authkey-newuser (user)```
