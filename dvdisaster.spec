Summary:	Securely store data on DVD/CD media
Name:		dvdisaster
Version:	0.72.1
Release:	%mkrel 4
License:	GPLv2
Group:		Archiving/Backup
URL:		http://dvdisaster.net/
Source0:		http://dvdisaster.net/downloads/%{name}-%{version}.tar.bz2
Patch:          dvdisaster-0.72.1-fix-format-errors.patch
BuildRequires:	gettext-devel
BuildRequires:	libglib2-devel
BuildRequires:	pango-devel
BuildRequires:	libgtk+2.0-devel
BuildRequires:	libbzip2-devel
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
dvdisaster is a way to securely store data on DVD/CD media.

CD, DVD and BD media keep their data only for a finite time (typically for many years). After that time, data loss develops slowly with read errors growing from the outer media region towards the inside.

dvdisaster stores data on CD/DVD/BD (supported media) in a way that it is fully recoverable even after some read errors have developed. This enables you to rescue the complete data to a new medium.

Data loss is prevented by using error correcting codes. Error correction data is either added to the medium or kept in separate error correction files. dvdisaster works at the image level so that the recovery does not depend on the file system of the medium. The maximum error correction capacity is user-selectable.

#--------------------------------------------------------------------

%prep
%setup -q
%patch -p 1

%build
#export CFLAGS="-O2 -g -pipe -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=4 -D_LARGEFILE64_SOURCE -D_LARGEFILE_SOURCE -DFILE_OFFSET_BITS=64"
./configure \
    --prefix=%{_prefix} \
    --buildroot=%{buildroot} \
    --mandir=%{_mandir} \
    --localedir=%{_datadir}/locale \
    --docdir=%{_datadir}/doc \
    --docsubdir=%{name}
%__make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/dvdisaster*
%doc CHANGELOG COPYING CREDIT* README* TODO INSTALL documentation
%{_mandir}/man?/%{name}*
%{_mandir}/*/man?/%{name}*
%{_datadir}/locale/*/LC_MESSAGES/*
