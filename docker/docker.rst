========================================================
 Docker images for packaging and testing Prism on Linux
========================================================

These docker images build and install deb, rpm, and arch packages of Prism. They run respectively on Debian  Fedora, and Arch containers.

They are meant as a *demonstration* of the build process. Note the resulting packages are *not signed*, and thus unsuitable for distribution. It is not too difficult to import your own gpg key into the container, and use it to build a signed package if you need it. Instructions for this below.

Once the image is built, run a container, and connect to it via ssh. Try running ``PrismProjectBrowser``.

-----------
Build image
-----------
You could use the provided shell script to trigger the build::

  cd Prism/
  docker/docker.sh build debian

When building the image, the flow is roughly:

* Install programs that will be needed to operate the machine. This does not include Prism's dependencies - they will be installed by the package. Only stuff like OpenSSH, xauth, rpmbuild.
* Create and set up OS user. Certain operations such as rpmbuild should not be done as root.
* Copy source code to container.
* Build package for corresponding distribution.
* Install resulting package.
* Set up ssh server so user can connect. Use X11 forwarding, in order to be able to test Prism's gui windows. More instructions for this below.

-------------
Run container
-------------
Using included script::

  docker/docker.sh run debian

The container has the ssh server launched automatically on startup.

-------
Connect
-------

The container runs sshd on port 2222 by default, so::

  ssh -p 2222 -X prismbuilder@localhost

Password is ``prism``.

If you start ``PrismProjectBrowser`` now, you should see the browser window!

----------------------------------------
Importing your gpg key to sign a package
----------------------------------------
Software packages need to be signed in order to guarantee
You need your private key to sign a software package.
Here is how to transfer it to the container.

On the machine where keys are located::

  gpg --export-secret-keys

Inside container::

   gpg --import private_key.key

Then, for example on Debian ``gbp buildpackage`` uses ``-k`` to pass a key to sign with.

-------------------------
Setting up X11 forwarding
-------------------------

Forwarding might require you to share the host machine's xauth cookie.

On the host machine::

  xauth list

Copy one of the lines (not sure if it matters which one).

In the container::

  xauth add <paste cookie>
