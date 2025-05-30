#define debug_package %%{nil}
#define _empty_manifest_terminate_build 0

Summary:		Qt GUI Interface for FluidSynth
Name:		qsynth
Version:		1.0.3
Release:		1
License:		GPLv2+
Group:		Sound
Url:		https://%{name}.sourceforge.net/
Source0:	https://sourceforge.net/projects/qsynth/files/qsynth/%{version}/%{name}-%{version}.tar.gz
BuildRequires:		cmake >= 3.15
BuildRequires:		desktop-file-utils
BuildRequires:		git
BuildRequires:		qmake-qt6
BuildRequires:		qt6-qtbase-theme-gtk3
BuildRequires:		cmake(Qt6)
BuildRequires:		cmake(Qt6Core)
BuildRequires:		cmake(Qt6LinguistTools)
BuildRequires:		cmake(Qt6Network)
BuildRequires:		cmake(Qt6Svg)
BuildRequires:		cmake(Qt6Widgets)
BuildRequires:		pkgconfig(fluidsynth)
BuildRequires:		pkgconfig(libpipewire-0.3)
BuildRequires:		pkgconfig(xkbcommon-x11)
BuildRequires:		pkgconfig(vulkan)
Requires:	fluidsynth

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around
the Qt toolkit using Qt Designer. Eventually it may evolve into a
softsynth management application allowing the user to control and manage
a variety of command line softsynth but for the moment it wraps the
excellent fluidSynth softsynth.

%files
%license LICENSE
%doc ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/org.rncbc.%{name}.desktop
%{_datadir}/metainfo/org.rncbc.%{name}.metainfo.xml
%{_iconsdir}/hicolor/scalable/apps/org.rncbc.%{name}.svg
%{_iconsdir}/*/*/*/org.rncbc.%{name}.png
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/%{name}.1.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DCONFIG_QT6=yes
%make_build


%install
%make_install -C build

# Fix the .desktop
desktop-file-edit \
	--remove-key="X-SuSE-translate" \
	--add-category="Midi" \
	--add-category="X-MandrivaLinux-Sound" \
	%{buildroot}%{_datadir}/applications/org.rncbc.%{name}.desktop
