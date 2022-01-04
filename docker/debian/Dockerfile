FROM debian:latest
USER root
RUN apt-get update && apt-get install -y ssh xauth neovim xfonts-75dpi xfonts-100dpi sudo git-buildpackage gnupg

# create and set up user
RUN id -u prismbuilder &>/dev/null || useradd --shell /bin/bash -m --user-group prismbuilder
RUN sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "prismbuilder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers;  su - prismbuilder -c id
RUN echo "prismbuilder:prism" | chpasswd

# copy source, build and install package
COPY . /mnt/Prism
RUN chown --recursive prismbuilder:prismbuilder /mnt/Prism && \
    (ls /mnt/Prism-deb-build || mkdir /mnt/Prism-deb-build) && \
    rm -Rf /mnt/Prism/debuild && \
    chown prismbuilder:prismbuilder /mnt/Prism-deb-build

USER prismbuilder

# build
RUN cd /mnt/Prism && \
    gbp dch --debian-branch=debian --upstream-branch=development --auto --git-author && \
    gbp buildpackage --no-sign --git-debian-branch=debian --git-upstream-branch=development --git-export-dir=../Prism-deb-build --git-ignore-new --git-export=WC --git-upstream-tag='%(version)s'

USER root
# install
RUN apt install -y /mnt/Prism-deb-build/prism_82f42f8a6487ee2746265db7433eb9aa806d6699-1_all.deb

# SSH setup
RUN sed -i -e 's/^UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && \
    sed -i -e 's/^#AddressFamily any/AddressFamily inet/g' /etc/ssh/sshd_config && \
    sed -i -e 's/^#X11Forwarding no/X11Forwarding yes/g' /etc/ssh/sshd_config && \
    sed -i -e 's/^#X11UseLocalhost yes/X11UseLocalhost no/g' /etc/ssh/sshd_config && \
    mkdir -p /run/sshd && \

# This is because python command does not exist by default on debian, only python3
# This should instead be handled correctly by Prism to select interpreter
RUN ls /usr/bin/python || ln -s /usr/bin/python3 /usr/bin/python

EXPOSE 22
RUN /usr/bin/ssh-keygen -A

USER prismbuilder
CMD ["sudo", "/usr/sbin/sshd", "-D"]
