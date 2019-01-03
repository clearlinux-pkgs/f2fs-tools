#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : f2fs-tools
Version  : 1.11.0
Release  : 2
URL      : https://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/f2fs-tools-1.11.0.tar.gz
Source0  : https://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/f2fs-tools-1.11.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: f2fs-tools-bin
Requires: f2fs-tools-lib
Requires: f2fs-tools-license
Requires: f2fs-tools-man
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(uuid)

%description
F2FS format utilility
---------------------
To use f2fs filesystem, you should format the storage partition
with this utilility. Otherwise, you cannot mount f2fs.

%package bin
Summary: bin components for the f2fs-tools package.
Group: Binaries
Requires: f2fs-tools-license
Requires: f2fs-tools-man

%description bin
bin components for the f2fs-tools package.


%package dev
Summary: dev components for the f2fs-tools package.
Group: Development
Requires: f2fs-tools-lib
Requires: f2fs-tools-bin
Provides: f2fs-tools-devel

%description dev
dev components for the f2fs-tools package.


%package lib
Summary: lib components for the f2fs-tools package.
Group: Libraries
Requires: f2fs-tools-license

%description lib
lib components for the f2fs-tools package.


%package license
Summary: license components for the f2fs-tools package.
Group: Default

%description license
license components for the f2fs-tools package.


%package man
Summary: man components for the f2fs-tools package.
Group: Default

%description man
man components for the f2fs-tools package.


%prep
%setup -q -n f2fs-tools-1.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534298031
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1534298031
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/f2fs-tools
cp COPYING %{buildroot}/usr/share/doc/f2fs-tools/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/defrag.f2fs
/usr/bin/dump.f2fs
/usr/bin/f2fscrypt
/usr/bin/f2fstat
/usr/bin/fibmap.f2fs
/usr/bin/fsck.f2fs
/usr/bin/mkfs.f2fs
/usr/bin/parse.f2fs
/usr/bin/resize.f2fs
/usr/bin/sg_write_buffer
/usr/bin/sload.f2fs

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libf2fs.so
/usr/lib64/libf2fs_format.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libf2fs.so.5
/usr/lib64/libf2fs.so.5.0.0
/usr/lib64/libf2fs_format.so.4
/usr/lib64/libf2fs_format.so.4.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/f2fs-tools/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man8/defrag.f2fs.8
/usr/share/man/man8/dump.f2fs.8
/usr/share/man/man8/f2fscrypt.8
/usr/share/man/man8/fsck.f2fs.8
/usr/share/man/man8/mkfs.f2fs.8
/usr/share/man/man8/resize.f2fs.8
/usr/share/man/man8/sload.f2fs.8
