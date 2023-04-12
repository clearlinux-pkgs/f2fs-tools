#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: autogen
#
Name     : f2fs-tools
Version  : 1.16.0
Release  : 6
URL      : https://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/f2fs-tools-1.16.0.tar.gz
Source0  : https://git.kernel.org/pub/scm/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/f2fs-tools-1.16.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: f2fs-tools-bin = %{version}-%{release}
Requires: f2fs-tools-lib = %{version}-%{release}
Requires: f2fs-tools-license = %{version}-%{release}
Requires: f2fs-tools-man = %{version}-%{release}
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : util-linux-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
F2FS format utility
---------------------
To use the f2fs filesystem, you should format the storage partition
with this utility. Otherwise, you cannot mount f2fs.

%package bin
Summary: bin components for the f2fs-tools package.
Group: Binaries
Requires: f2fs-tools-license = %{version}-%{release}

%description bin
bin components for the f2fs-tools package.


%package dev
Summary: dev components for the f2fs-tools package.
Group: Development
Requires: f2fs-tools-lib = %{version}-%{release}
Requires: f2fs-tools-bin = %{version}-%{release}
Provides: f2fs-tools-devel = %{version}-%{release}
Requires: f2fs-tools = %{version}-%{release}

%description dev
dev components for the f2fs-tools package.


%package lib
Summary: lib components for the f2fs-tools package.
Group: Libraries
Requires: f2fs-tools-license = %{version}-%{release}

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
%setup -q -n f2fs-tools-1.16.0
cd %{_builddir}/f2fs-tools-1.16.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681309646
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1681309646
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/f2fs-tools
cp %{_builddir}/f2fs-tools-%{version}/COPYING %{buildroot}/usr/share/package-licenses/f2fs-tools/a55afe19b58d728b586547acb09862752d4f1b76 || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/defrag.f2fs
/usr/bin/dump.f2fs
/usr/bin/f2fs_io
/usr/bin/f2fscrypt
/usr/bin/f2fslabel
/usr/bin/fibmap.f2fs
/usr/bin/fsck.f2fs
/usr/bin/mkfs.f2fs
/usr/bin/parse.f2fs
/usr/bin/resize.f2fs
/usr/bin/sload.f2fs

%files dev
%defattr(-,root,root,-)
/usr/include/f2fs_fs.h
/usr/include/quota.h
/usr/lib64/libf2fs.so
/usr/lib64/libf2fs_format.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libf2fs.so.10
/usr/lib64/libf2fs.so.10.0.0
/usr/lib64/libf2fs_format.so.9
/usr/lib64/libf2fs_format.so.9.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/f2fs-tools/a55afe19b58d728b586547acb09862752d4f1b76

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/defrag.f2fs.8
/usr/share/man/man8/dump.f2fs.8
/usr/share/man/man8/f2fs_io.8
/usr/share/man/man8/f2fscrypt.8
/usr/share/man/man8/f2fslabel.8
/usr/share/man/man8/fsck.f2fs.8
/usr/share/man/man8/mkfs.f2fs.8
/usr/share/man/man8/resize.f2fs.8
/usr/share/man/man8/sload.f2fs.8
