Summary:	Securely store data on DVD/CD media
Name:		dvdisaster
Version:	0.72.4
Release:	1
License:	GPLv2
Group:		Archiving/Backup
URL:		http://dvdisaster.net/
Source0:	http://dvdisaster.net/downloads/%{name}-%{version}.tar.bz2
Patch0:          dvdisaster-0.72.1-fix-format-errors.patch
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	pango-devel
BuildRequires:	libgtk+2.0-devel
BuildRequires:	libbzip2-devel

%description
dvdisaster is a way to securely store data on DVD/CD media.

#--------------------------------------------------------------------

%prep
%setup -q
#%patch0 -p 1

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
%makeinstall_std

%files
%{_bindir}/dvdisaster*
%doc CHANGELOG COPYING CREDIT* README* TODO INSTALL documentation
%{_mandir}/man?/%{name}*
%{_mandir}/*/man?/%{name}*
%{_datadir}/locale/*/LC_MESSAGES/*
