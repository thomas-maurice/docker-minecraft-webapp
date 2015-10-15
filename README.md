# Docker Minecraft Server -  Webapp
This documentation is pretty shitty for now, more to come :)

## TL;DR
This prokect aims at maintaining a self-contained solution to manage and control
your Minecraft server. Originally the idea was that I wanted a Minecraft server,
but not Java on my machine, that's why I started to build a Minecraft Docker.

In addition to the minecraft server, a webapp is shipped that allows you to
establish simple interactions with the game server, such as :
 * Changing time
 * Changing weather
 * Full console access over HTTP

## How to build it ?
You can build the image simply by launching the `./build_docker.sh` script.
The build can take some time since a transient docker is generated to generatedthe static
content for the webapp (Bower + Grunt). Once it is build just launch it with the
command `docker run -it minecraft`.

## How to run it persistently ?
You can run it persistently by adding a volume to it. The volume is extected to be
in the `/home/minecraft/volume` of the image, which leads you to the following :
`docker run --net host -v /some/dir:/home/minecraft/volume -it minecraft`.

All the needed directories will be created at runtime, and the default credentials
for the Webapp are admin:admin.

Also don't be affraid if the docker sets up strange modes on its volume directory
(UID: 4242, GID: 4242), this is because if the UID/GID aren't consistent inside or
outside of the container (since the minecraft server does not run as root), you would
be write/read denied.

You can run as many servers as you want, as long as you specify different directories.
To backup a server, just backup its directory.

## Contributing
Pull requests and help welcome ! If possible please include tests (I know I don't, but someday
I'll find the time !). Feel free to contact me via email or via my twitter [@thomas_maurice](https://twitter.com/thomas_maurice)

## Credits
 * Webapp, Dockerfiles, bash scripts and shit written by Thomas Maurice <thomas@maurice.fr>
 * The lib used to speak to the console server is written by [barneygale](https://github.com/barneygale/MCRcon)
