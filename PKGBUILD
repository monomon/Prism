# Maintainer: Mois Moshev <mois@monomon.me>
pkgname=prism
pkgver=1.3.0.82
pkgrel=1
pkgdesc="Free and artist friendly Pipeline for animation and VFX projects teams achieve their goals by automating tasks and simplifying their workflow."
depends=(pyside2 python-ruamel-yaml ffmpeg python-pillow openimageio)
url=https://prism-pipeline.com/
arch=("any")

package() {
          cd "${startdir}"
          mkdir -p "${pkgdir}/opt/Prism"
          cp -R Prism "${pkgdir}/opt/Prism/"
          cp -R  Documentation "${pkgdir}/opt/Prism/"
          install --target-directory="${pkgdir}/opt/Prism/" -m 444 README.md LICENSE

          mkdir -p ${pkgdir}/usr/bin
          mkdir -p ${pkgdir}/usr/share/applications
          ln -s /opt/Prism/Prism/Tools/PrismProjectBrowser.sh ${pkgdir}/usr/bin/PrismProjectBrowser
          ln -s /opt/Prism/Prism/Tools/PrismSettings.sh ${pkgdir}/usr/bin/PrismSettings
          ln -s /opt/Prism/Prism/Tools/PrismTray.sh ${pkgdir}/usr/bin/PrismTray
          ln -s /opt/Prism/Prism/Tools/PrismProjectBrowser.desktop ${pkgdir}/usr/share/applications/PrismProjectBrowser.desktop
          ln -s /opt/Prism/Prism/Tools/PrismSettings.desktop ${pkgdir}/usr/share/applications/PrismSettings.desktop
          ln -s /opt/Prism/Prism/Tools/PrismTray.desktop ${pkgdir}/usr/share/applications/PrismTray.desktop

          chmod 755 "${pkgdir}/opt/Prism"
          chmod 755 ${pkgdir}/usr/bin/PrismProjectBrowser
          chmod 755 ${pkgdir}/usr/bin/PrismSettings
          chmod 755 ${pkgdir}/usr/bin/PrismTray
}