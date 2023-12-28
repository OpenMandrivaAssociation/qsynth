#define debug_package %{nil}
%define _empty_manifest_terminate_build 0

Name:		qsynth
Summary:        Qt GUI Interface for FluidSynth
Version:        0.9.12
Release:        1
License:	GPLv2+
Group:		Sound
Source0:	https://sourceforge.net/projects/qsynth/files/qsynth/%{version}/%{name}-%{version}.tar.gz
URL:            https://%{name}.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(vulkan)

Requires:	fluidsynth

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around
the Qt4 toolkit using Qt Designer. Eventually it may evolve into a
softsynth management application allowing the user to control and manage
a variety of command line softsynth but for the moment it wraps the
excellent FluidSynth softsynth.


%prep
%autosetup -p1

%build
%cmake \
        -DCONFIG_QT6=yes

%make_build

%install
%make_install -C build

# Fix the .desktop file by removing
# 2 non-Mdv key and 2 non-standard categories
desktop-file-install \
    --remove-key="X-SuSE-translate" \
    --add-category="Midi" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/org.rncbc.qsynth.desktop

%files
%doc AUTHORS ChangeLog README TODO TRANSLATORS
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/metainfo/org.rncbc.%{name}.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.qsynth.svg
%{_iconsdir}/*/*/*/org.rncbc.%{name}.png
%{_mandir}/man1/%org.rncbc.{name}*.1*
%{_mandir}/*/man1/qsynth.1.*

%changelog
* Mon Oct 29 2012 Giovanni Mariani <mc2374@mclink.it> 0.3.6-2
- Removed now useless BuildRoot, %%mkrel, %%defattr and %%clean section
- Revert to using %%configure2_5x because CMakeLists.txt does not correctly support
  the gold linker, while the old good configure does
- Fixed icon file path
- Fixed file list

* Sun Apr 17 2011 Frank Kober <emuse@mandriva.org> 0.3.6-1mdv2011.0
+ Revision: 654031
- new version 0.3.6
   o man page no longer distributed
   o beginning switch to cmake build environment
   o old sources and patch deleted

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.5-3mdv2011.0
+ Revision: 614680
- the mass rebuild of 2010.1 packages

* Mon May 03 2010 Frank Kober <emuse@mandriva.org> 0.3.5-2mdv2010.1
+ Revision: 541841
- fix desktop categories (Bug #59063), fix tarball permissions

* Wed Apr 28 2010 Frank Kober <emuse@mandriva.org> 0.3.5-1mdv2010.1
+ Revision: 540488
- sync sources, replace locale patch by perl script
- new version (bugfixes and enhancements) 0.3.5

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 0.3.4-3mdv2010.0
+ Revision: 433042
- rebuild

  + Frederik Himpe <fhimpe@mandriva.org>
    - Don't use parallell make
    - Update to new version 0.3.4

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 0.3.3-2mdv2009.0
+ Revision: 234223
- requries fluidsynth

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 0.3.3-1mdv2009.0
+ Revision: 234218
- New version 0.3.3
- drop old tarball

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 28 2007 Austin Acton <austin@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 138719
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 18 2007 Austin Acton <austin@mandriva.org> 0.3.1-1mdv2008.0
+ Revision: 53175
- new version
- use bundled desktop file

* Thu Jun 14 2007 Austin Acton <austin@mandriva.org> 0.2.6-1mdv2008.0
+ Revision: 39348
- new version
- fix menu categories
- Import qsynth



* Sat Sep 16 2006 Emmanuel Andry <eandry@mandriva.org> 0.2.5-5mdv2007.0
- xdg menu

* Tue Mar 28 2006 Austin Acton <austin@mandriva.org> 0.2.5-4mdk
- buildrequires ImageMagick

* Tue Mar 21 2006 Austin Acton <austin@mandriva.org> 0.2.5-3mdk
- really fix x86_64 build

* Tue Mar 21 2006 Austin Acton <austin@mandriva.org> 0.2.5-2mdk
- mkrel

* Sat Mar 18 2006 Pedro Lopez-Cabanillas <plcl@users.sourceforge.net> 0.2.5-1mdk
- Spec change to build on x86_64
- 0.2.5

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.4-2mdk
- Fix BuildRequires

* Mon Oct 03 2005 Lenny Cartier <lenny@mandriva.com> 0.2.4-1mdk
- 0.2.4

* Tue May 24 2005 Austin Acton <austin@mandriva.org> 0.2.3-1mdk
- 0.2.3
- source URL

* Fri Oct 8 2004 Austin Acton <austin@mandrake.org> 0.2.2-1mdk
- 0.2.2
- configure 2.5

* Sat Jun 5 2004 Austin Acton <austin@mandrake.org> 0.2.1-1mdk
- 0.2.1

* Mon Mar 1 2004 Austin Acton <austin@mandrake.org> 0.1.3-1mdk
- 0.1.3

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org) 0.1.2-1mdk
- 0.1.2

* Tue Dec 30 2003 Austin Acton <austin@linux.ca> 0.1.0-1mdk
- 0.1.0

* Sat Dec 27 2003 Austin Acton <aacton@yorku.ca> 0.0.3-1mdk
- initial package

