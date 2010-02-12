Name:           homebank
Version:        4.2
Release:        %mkrel 1
Summary:        Free easy personal accounting for all  

Group:          Office
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:        GPLv2+
URL:            http://homebank.free.fr
Source0:        http://homebank.free.fr/public/%{name}-%{version}.tar.gz
Patch0:		desktop.patch

BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  perl-XML-Parser
BuildRequires:  libofx-devel
BuildRequires:  cairo-devel
BuildRequires:  atk-devel
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
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-mime-database %{_datadir}/mime &> /dev/null || :
update-desktop-database &> /dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README doc/TODO
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/images
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/%{name}
%{_datadir}/mime-info/%{name}.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/%{name}/help
