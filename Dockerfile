# Usar uma imagem base leve do Ubuntu (x86_64 para rodar ferramentas do Android SDK em M1/M2)
FROM --platform=linux/amd64 ubuntu:22.04

# Evitar prompts interativos durante a instalação
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências necessárias para o Buildozer e Android SDK/NDK
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    ant \
    build-essential \
    libltdl-dev \
    libffi-dev \
    libssl-dev \
    autoconf \
    autotools-dev \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libtinfo5 \
    cmake \
    libgmp-dev \
    libmpc-dev \
    libmpfr-dev \
    ccache \
    wget \
    curl \
    patch \
    lib32stdc++6 \
    lib32z1 \
    lib32ncurses6 \
    libncurses5 \
    && rm -rf /var/lib/apt/lists/*

# Criar um usuário não-root (necessário para o Buildozer)
RUN useradd -m -s /bin/bash builder
USER builder
WORKDIR /home/builder/app

# Instalar o Buildozer e Cython via pip (Cython < 3.0 é necessário para compatibilidade com Pyjnius)
RUN pip3 install --user --upgrade buildozer "Cython<3.0" setuptools

# Adicionar o caminho do binário do usuário ao PATH
ENV PATH="/home/builder/.local/bin:${PATH}"

# O diretório de trabalho será montado como um volume
CMD ["buildozer", "android", "debug"]
