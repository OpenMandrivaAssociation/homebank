Summary:	Free easy personal accounting for all
Name:		homebank
Version:	4.5
Release:	10
Group:		Office
License:	GPLv2+
Url:		http://homebank.free.fr
Source0:	http://homebank.free.fr/public/%{name}-%{version}.tar.gz
Patch0:		desktop.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libofx)

%description
HomeBank is the free software you have always wanted to manage your personal
accounts at home. The main concept is to be light, simple and very easy to use.
It brings you many features that allows you to analyze your finances in a
detailed way instantly and dynamically with powerful report tools based on
filtering and graphical charts.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING NEWS README doc/TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mime-info/%{name}.*
%{_iconsdir}/hicolor/*/apps/%{name}.*

