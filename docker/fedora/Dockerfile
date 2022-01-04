FROM fedora:latest
USER root
RUN dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
RUN dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

RUN dnf -y install rsync rpm-build rpmlint openssh-server sudo xorg-x11-xauth neovim xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi ffmpeg


# create and set up user
RUN id -u prismbuilder &>/dev/null || useradd -m prismbuilder
RUN sed -i /etc/sudoers -re 's/^%sudo.*/%sudo ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^root.*/root ALL=(ALL:ALL) NOPASSWD: ALL/g' && \
    sed -i /etc/sudoers -re 's/^#includedir.*/## **Removed the include directive** ##"/g' && \
    echo "prismbuilder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers;  su - prismbuilder -c id
RUN echo "prismbuilder:prism" | chpasswd

# copy source, build and install package
COPY . /mnt/Prism
RUN chown --recursive prismbuilder:prismbuilder /mnt/Prism && \
    chmod --recursive 775 /mnt/Prism

USER prismbuilder
RUN cd /mnt/Prism && \
    rpmbuild -bb prism.spec

USER root

# SSH setup
RUN sed -i -e 's/^UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && \
    sed -i -e 's/^#AddressFamily any/AddressFamily inet/g' /etc/ssh/sshd_config && \
    sed -i -e 's/^#X11Forwarding no/X11Forwarding yes/g' /etc/ssh/sshd_config && \
    sed -i -e 's/^#X11UseLocalhost yes/X11UseLocalhost no/g' /etc/ssh/sshd_config
EXPOSE 22
RUN /usr/bin/ssh-keygen -A

USER prismbuilder
CMD ["sudo", "/usr/sbin/sshd", "-D"]
# CMD ["bash"]
