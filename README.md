# space
Utility scripts for workspace container management.

## Usage

1) Clone this repo.
2) Set environment variable $SPACE refers to where the ```container``` in the repo is.
3) Execute ```spacen fedora:39```

### Host-side scripts
- spacen: Create container and mount host directories to the container.
  <br/>```$ spacen (image)```
- space: Login as user $1 in container.
  <br/>```$ space (user) [command]```
- startup: Piece of script that used to prepare the container before starting it, add it to your Display Manager.
  <br/>```$ startup```
- shutdown: Piece of script that kill the running container.
  <br/>```$ shutdown```
- porter: Expose a port by SSH from container, listen on host. You have to prepare the ssh keypair for user ```porter``` first.
  <br/>```$ porter 2222```
- wlx: Start an Xwayland server with 777 mode X11 socket and authority disabled on Wayland display. No container needed.
  <br/>```$ wlx (X display number)```

### Container-side
- spacerc: Setup container environment by the information mounted from host.
- setup: Initialize container environment when /etc/setup does not exist.

Example
```shell
$ spacen fedora:39          # Create and setup the new container.
$ space                     # Login as root.
$ space root /bin/firefox   # Run FireFox as root.
```
