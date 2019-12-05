#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pyro4
Version  : 4.77
Release  : 9
URL      : https://files.pythonhosted.org/packages/01/02/27c48986d0bf2e42ef42591e796261d4dbb6466da81957071479d99017ed/Pyro4-4.77.tar.gz
Source0  : https://files.pythonhosted.org/packages/01/02/27c48986d0bf2e42ef42591e796261d4dbb6466da81957071479d99017ed/Pyro4-4.77.tar.gz
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
It is a library that enables you to build applications in which
        objects can talk to eachother over the network, with minimal programming effort.
        You can just use normal Python method calls, with almost every possible parameter
        and return value type, and Pyro takes care of locating the right object on the right
        computer to execute the method. It is designed to be very easy to use, and to
        generally stay out of your way. But it also provides a set of powerful features that
        enables you to build distributed applications rapidly and effortlessly.
        Pyro is a pure Python library and runs on many different platforms and Python versions.

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

%description python3
python3 components for the Pyro4 package.


%prep
%setup -q -n Pyro4-4.77

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570062332
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Pyro4
cp LICENSE %{buildroot}/usr/share/package-licenses/Pyro4/LICENSE
cp docs/source/license.rst %{buildroot}/usr/share/package-licenses/Pyro4/docs_source_license.rst
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
/usr/share/package-licenses/Pyro4/LICENSE
/usr/share/package-licenses/Pyro4/docs_source_license.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
