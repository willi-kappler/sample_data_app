{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = with pkgs.buildPackages; [
      autoconf
      cmake
      git
      jdk17
      libffi
      libtinfo
      libtool
      ncurses5
      openssl
      pkg-config
      unzip
      virtualenv
      zip
      zlib
      (python312.withPackages(ps: with ps; [
        cython
        kivy
        opencv4
        pip
        plyer
        uv
        ]))
    ];
}

