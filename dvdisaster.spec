Summary:	Securely store data on DVD/CD media
Name:		dvdisaster
Version:	0.72.4
Release:	1
License:	GPLv2
Group:		Archiving/Backup
URL:		http://dvdisaster.net/
Source0:	http://dvdisaster.net/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	gettext-devel
BuildRequires:	libglib2-devel
BuildRequires:	pango-devel
BuildRequires:	libgtk+2.0-devel
BuildRequires:	bzip2-devel = 1.0.6-8

%description

dvdisaster is a way to securely store data on DVD/CD media.
CD, DVD and BD media keep their data only for a finite time
(typically for many years). 
After that time, data loss develops slowly with read errors
growing from the outer media region towards the inside.
dvdisaster stores data on CD/DVD/BD (supported media) in a way
that it is fully recoverable even after some read errors have
developed. This enables you to rescue the complete data to a new
medium. Data loss is prevented by using error correcting codes.
Error correction data is either added to the medium 
or kept in separate error correction files. dvdisaster works at
the image level so that the 
ecovery does not depend on the file system of the medium. 
The maximum error correction capacity is user-selectable.



%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --buildroot=%{buildroot} \
    --mandir=%{_mandir} \
    --localedir=%{_datadir}/locale \
    --docdir=%{_datadir}/doc \
    --docsubdir=%{name}
%__make CFLAGS="%{optflags}"

%install

%makeinstall_std


%files
%defattr(-,root,root)
%{_bindir}/dvdisaster*
%doc CHANGELOG COPYING CREDIT* README* TODO INSTALL documentation
%{_mandir}/man?/%{name}*
%{_mandir}/*/man?/%{name}*
%{_datadir}/locale/*/LC_MESSAGES/*

