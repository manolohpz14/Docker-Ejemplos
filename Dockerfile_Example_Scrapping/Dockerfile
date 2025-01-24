FROM ubuntu



RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    libxi6 \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libindicator7 \
    ca-certificates \
    fonts-liberation \
    libgbm1 \
    python3 \
    python3-pip \
    curl \
    alsa-topology-conf \
    alsa-ucm-conf \
    libasound2-data \
    libasound2t64 \
    libauthen-sasl-perl \
    libclone-perl \
    libdata-dump-perl \
    libdrm-amdgpu1 \
    libdrm-intel1 \
    libdrm-nouveau2 \
    libdrm-radeon1 \
    libegl-mesa0 \
    libegl1 \
    libelf1t64 \
    libencode-locale-perl \
    libfile-basedir-perl \
    libfile-desktopentry-perl \
    libfile-listing-perl \
    libfile-mimeinfo-perl \
    libfont-afm-perl \
    libgl1 \
    libgl1-amber-dri \
    libgl1-mesa-dri \
    libglapi-mesa \
    libgles2 \
    libglvnd0 \
    libglx-mesa0 \
    libglx0 \
    libhtml-form-perl \
    libhtml-format-perl \
    libhtml-parser-perl \
    libhtml-tagset-perl \
    libhtml-tree-perl \
    libhttp-cookies-perl \
    libhttp-daemon-perl \
    libhttp-date-perl \
    libhttp-message-perl \
    libhttp-negotiate-perl \
    libice6 \
    libio-html-perl \
    libio-socket-ssl-perl \
    libio-stringy-perl \
    libipc-system-simple-perl \
    libllvm17t64 \
    liblwp-mediatypes-perl \
    liblwp-protocol-https-perl \
    libmailtools-perl \
    libnet-dbus-perl \
    libnet-http-perl \
    libnet-smtp-ssl-perl \
    libnet-ssleay-perl \
    libpciaccess0 \
    libsensors-config \
    libsensors5 \
    libsm6 \
    libtext-iconv-perl \
    libtie-ixhash-perl \
    libtimedate-perl \
    libtry-tiny-perl \
    liburi-perl \
    libvulkan1 \
    libwww-perl \
    libwww-robotrules-perl \
    libx11-protocol-perl \
    libx11-xcb1 \
    libxaw7 \
    libxcb-dri2-0 \
    libxcb-dri3-0 \
    libxcb-glx0 \
    libxcb-present0 \
    libxcb-shape0 \
    libxcb-sync1 \
    libxcb-xfixes0 \
    libxft2 \
    libxkbfile1 \
    libxml-parser-perl \
    libxml-twig-perl \
    libxml-xpathengine-perl \
    libxmu6 \
    libxshmfence1 \
    libxt6t64 \
    libxv1 \
    libxxf86dga1 \
    libxxf86vm1 \
    mesa-vulkan-drivers \
    perl-openssl-defaults \
    x11-utils \
    x11-xserver-utils \
    xdg-utils \
    zutty


RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb && \
    apt-get install -f -y


RUN apt install python3.12-venv -y

RUN python3 -m venv /venv

# Activar el entorno virtual e instalar las dependencias
RUN /venv/bin/pip install --upgrade pip

COPY requirements.txt .

RUN /venv/bin/pip install -r requirements.txt

COPY script.py .
# Usar el entorno virtual para ejecutar el script de Python
CMD ["/venv/bin/python", "script.py"]









