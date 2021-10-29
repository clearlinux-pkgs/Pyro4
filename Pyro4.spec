#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pyro4
Version  : 4.81
Release  : 30
URL      : https://files.pythonhosted.org/packages/04/7f/85dca0acb3018c03f53e81f9edb0fb300a9faef0c31d5eeeebfa717acd1d/Pyro4-4.81.tar.gz
Source0  : https://files.pythonhosted.org/packages/04/7f/85dca0acb3018c03f53e81f9edb0fb300a9faef0c31d5eeeebfa717acd1d/Pyro4-4.81.tar.gz
Summary  : distributed object middleware for Python (RPC)
Group    : Development/Tools
License  : MIT
Requires: Pyro4-bin = %{version}-%{release}
Requires: Pyro4-license = %{version}-%{release}
Requires: Pyro4-python = %{version}-%{release}
Requires: Pyro4-python3 = %{version}-%{release}
Requires: serpent
BuildRequires : buildreq-distutils3
BuildRequires : serpent

%description
[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://saythanks.io/to/irmen)
[![Build Status](https://travis-ci.org/irmen/Pyro4.svg?branch=master)](https://travis-ci.org/irmen/Pyro4)
[![Latest Version](https://img.shields.io/pypi/v/Pyro4.svg)](https://pypi.python.org/pypi/Pyro4/)
[![Anaconda-Server Badge](https://anaconda.org/conda-forge/pyro4/badges/version.svg)](https://anaconda.org/conda-forge/pyro4)
[![Code Quality: Python](https://img.shields.io/lgtm/grade/python/g/irmen/Pyro4.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/irmen/Pyro4/context:python)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/irmen/Pyro4.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/irmen/Pyro4/alerts)

%package bin
Summary: bin components for the Pyro4 package.
Group: Binaries
Requires: Pyro4-license = %{version}-%{release}

%description bin
bin components for the Pyro4 package.


%package license
Summary: license components for the Pyro4 package.
Group: Default

%description license
license components for the Pyro4 package.


%package python
Summary: python components for the Pyro4 package.
Group: Default
Requires: Pyro4-python3 = %{version}-%{release}
Provides: pyro4-python

%description python
python components for the Pyro4 package.


%package python3
Summary: python3 components for the Pyro4 package.
Group: Default
Requires: python3-core
Provides: pypi(pyro4)
Requires: pypi(serpent)

%description python3
python3 components for the Pyro4 package.


%prep
%setup -q -n Pyro4-4.81
cd %{_builddir}/Pyro4-4.81

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631630594
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Pyro4
cp %{_builddir}/Pyro4-4.81/LICENSE %{buildroot}/usr/share/package-licenses/Pyro4/28687233f8a681dc4d5979e85b98d6231a800839
cp %{_builddir}/Pyro4-4.81/docs/source/license.rst %{buildroot}/usr/share/package-licenses/Pyro4/d4c0c8299052f2e2089f956acbbb99f2a6ea77c1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pyro4-check-config
/usr/bin/pyro4-flameserver
/usr/bin/pyro4-httpgateway
/usr/bin/pyro4-ns
/usr/bin/pyro4-nsc
/usr/bin/pyro4-test-echoserver

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Pyro4/28687233f8a681dc4d5979e85b98d6231a800839
/usr/share/package-licenses/Pyro4/d4c0c8299052f2e2089f956acbbb99f2a6ea77c1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
