Name:		homebank
Version:	4.4
Release:	6
Summary:	Free easy personal accounting for all

Group:		Office
License:	GPLv2+
URL:		http://homebank.free.fr
Source0:	http://homebank.free.fr/public/%{name}-%{version}.tar.gz
Patch0:		desktop.patch

BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	desktop-file-utils
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig(libofx)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(atk)
BuildRequires:	intltool

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
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/application-registry/%{name}.applications


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4.4-2mdv2011.0
+ Revision: 665414
- mass rebuild

* Sat Feb 26 2011 Funda Wang <fwang@mandriva.org> 4.4-1
+ Revision: 639886
- update to new version 4.4

* Tue Aug 24 2010 Sandro Cazzaniga <kharec@mandriva.org> 4.3-1mdv2011.0
+ Revision: 572637
- update to 4.3

* Tue Feb 16 2010 Funda Wang <fwang@mandriva.org> 4.2.1-1mdv2010.1
+ Revision: 506588
- update to new version 4.2.1

* Fri Feb 12 2010 Frederik Himpe <fhimpe@mandriva.org> 4.2-1mdv2010.1
+ Revision: 505055
- update to new version 4.2

* Sun Nov 08 2009 Frederik Himpe <fhimpe@mandriva.org> 4.1-1mdv2010.1
+ Revision: 463069
- Update to new version 4.1

* Sun Aug 23 2009 Frederik Himpe <fhimpe@mandriva.org> 4.0.4-1mdv2010.0
+ Revision: 420198
- update to new version 4.0.4

* Sun May 03 2009 Funda Wang <fwang@mandriva.org> 4.0.3-1mdv2010.0
+ Revision: 370848
- New version 4.0.3

* Thu Apr 09 2009 Anne Nicolas <ennael@mandriva.org> 4.0.2-2mdv2009.1
+ Revision: 365407
- fix menu for KDE

* Sun Feb 01 2009 Frederik Himpe <fhimpe@mandriva.org> 4.0.2-1mdv2009.1
+ Revision: 335927
- update to new version 4.0.2

* Fri Dec 05 2008 Funda Wang <fwang@mandriva.org> 4.0.1-1mdv2009.1
+ Revision: 310167
- new version 4.0.1

* Mon Nov 24 2008 Funda Wang <fwang@mandriva.org> 4.0-1mdv2009.1
+ Revision: 306160
- BR intltool
- new version 4.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)
    - fix no-buildroot-tag

  + Frederik Himpe <fhimpe@mandriva.org>
    - New upstream version

* Tue Jan 29 2008 Austin Acton <austin@mandriva.org> 3.6-1mdv2008.1
+ Revision: 159621
- import homebank


