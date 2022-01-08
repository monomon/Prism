Name: Prism
Version: 1.3.0.82
Release: 1
Summary: Free and artist friendly Pipeline for animation and VFX projects teams
License: GPLv3
Prefix: /opt
BuildArch: noarch
Url: https://prism-pipeline.com/
Requires: python3-pyside2 python3-ruamel-yaml python3-pillow OpenImageIO

# package straight from current directory
%define _sourcedir %(pwd)
# nuke scripts have a weird shebang with the windows path to Nuke
%global __mangle_shebangs_exclude "^C:/.*"
%global __mangle_shebangs_exclude_from .git

%description
Free and artist friendly Pipeline for animation and VFX projects teams achieve their goals
by automating tasks and simplifying their workflow.

%prep
rm -Rf %{_builddir}/%{name}
mkdir -p %{_builddir}/%{name}
rsync -r --exclude '.gitignore' --exclude '.git' \
      --exclude '.github' --exclude '*~' --exclude '**/*~' \
      %{_sourcedir}/ %{_builddir}/%{name}

%install
mkdir -p %{buildroot}/opt/Prism
cp -R %{_builddir}/%{name} %{buildroot}/opt/
# install --target-directory="%{buildroot}" -m 444 %{_sourcedir}/README.md %{_sourcedir}/LICENSE

%post
ln -s /opt/Prism/Prism/Tools/PrismProjectBrowser.sh %{_bindir}/PrismProjectBrowser
ln -s /opt/Prism/Prism/Tools/PrismSettings.sh %{_bindir}/PrismSettings
ln -s /opt/Prism/Prism/Tools/PrismTray.sh %{_bindir}/PrismTray
ln -s /opt/Prism/Prism/Tools/PrismProjectBrowser.desktop /usr/share/applications/PrismProjectBrowser.desktop
ln -s /opt/Prism/Prism/Tools/PrismSettings.desktop /usr/share/applications/PrismSettings.desktop
ln -s /opt/Prism/Prism/Tools/PrismTray.desktop /usr/share/applications/PrismTray.desktop

chmod 755 /opt/Prism/Prism/Tools/PrismProjectBrowser.sh
chmod 755 /opt/Prism/Prism/Tools/PrismSettings.sh
chmod 755 /opt/Prism/Prism/Tools/PrismTray.sh

%files
/opt/Prism
%ghost %{_bindir}/PrismProjectBrowser
%ghost %{_bindir}/PrismSettings
%ghost %{_bindir}/PrismTray
%ghost /usr/share/applications/PrismProjectBrowser.desktop
%ghost /usr/share/applications/PrismSettings.desktop
%ghost /usr/share/applications/PrismTray.desktop
