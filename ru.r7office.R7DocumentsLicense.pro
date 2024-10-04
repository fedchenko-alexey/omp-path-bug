TARGET = ru.r7office.R7DocumentsLicense

CONFIG += \
    auroraapp_qml

DISTFILES += \
    license/*.lickey \
    qml/main.qml \
    rpm/ru.r7office.R7DocumentsLicense.spec \
    ru.r7office.R7DocumentsLicense.desktop \
    AUTHORS.md

license.extra = cp $${PWD}/license/*.lickey $${OUT_PWD}/license.lickey
license.files = license/*
license.path = /usr/share/common/ru.r7office/R7DocumentsLicense/
license.CONFIG = no_check_install

INSTALLS += license

AURORAAPP_ICONS = 86x86 108x108 128x128 172x172
