Summary:	Free easy personal accounting for all
Name:		homebank
Version:	5.6.5
Release:	1
Group:		Office
License:	GPLv2+
Url:		http://homebank.free.fr
Source0:	http://homebank.free.fr/public/sources/%{name}-%{version}.tar.gz
Patch0:		desktop.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libofx)
BuildRequires:  pkgconfig(libsoup-2.4)

%description
HomeBank is the free software you have always wanted to manage your personal
accounts at home. The main concept is to be light, simple and very easy to use.
It brings you many features that allows you to analyze your finances in a
detailed way instantly and dynamically with powerful report tools based on
filtering and graphical charts.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install INSTALL='install -p'

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README doc/TODO
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/homebank.appdata.xml
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png
