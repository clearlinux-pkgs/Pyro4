#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Pyro4
Version  : 4.79
Release  : 13
URL      : https://files.pythonhosted.org/packages/ff/38/b842c05c6842c54cf2677e8b382299e606163d03268221d6aab54459047b/Pyro4-4.79.tar.gz
Source0  : https://files.pythonhosted.org/packages/ff/38/b842c05c6842c54cf2677e8b382299e606163d03268221d6aab54459047b/Pyro4-4.79.tar.gz
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
This is an example that more or less presents an online multiplayer game.
The game is a robot destruction derby.
It is played on a grid. There are some obstructing walls on the grid that
hurt when you collide into them. If you collide into another robot, the
other robot takes damage. All robots start with a certain amount of health.
If it reaches zero, the robot dies.  The last man standing wins!

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
%setup -q -n Pyro4-4.79
cd %{_builddir}/Pyro4-4.79

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1581992753
# -Werror is for werrorists
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
cp %{_builddir}/Pyro4-4.79/LICENSE %{buildroot}/usr/share/package-licenses/Pyro4/28687233f8a681dc4d5979e85b98d6231a800839
cp %{_builddir}/Pyro4-4.79/docs/source/license.rst %{buildroot}/usr/share/package-licenses/Pyro4/d4c0c8299052f2e2089f956acbbb99f2a6ea77c1
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
