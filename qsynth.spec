%define debug_package %{nil}

Name:		qsynth
Summary:        Qt GUI Interface for FluidSynth
Version:		0.3.9
Release:		1
License:		GPLv2+
Group:		Sound
Source0:		http://downloads.sourceforge.net/qsynth/%{name}-%{version}.tar.gz
URL:            http://%{name}.sourceforge.net/
BuildRequires:	qt4-devel >= 4.2.0
BuildRequires:	qt4-linguist
BuildRequires:	pkgconfig(x11)
BuildRequires:	fluidsynth-devel
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
Requires:	fluidsynth

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around
the Qt4 toolkit using Qt Designer. Eventually it may evolve into a
softsynth management application allowing the user to control and manage
a variety of command line softsynth but for the moment it wraps the
excellent FluidSynth softsynth.


%prep
%setup -q


%build
# Fix locale installation path
perl -pi -e 's/share\/locale/share\/qsynth\/locale/g' src/CMakeLists.txt
perl -pi -e 's/share\/locale/share\/qsynth\/locale/g' src/qsynth.cpp
%configure2_5x
#cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
# (gvm) To avoid random build errors with translation files
make


%install
%makeinstall_std

# Fix the .desktop file by removing
# 2 non-Mdv key and 2 non-standard categories
desktop-file-install \
    --remove-key="X-SuSE-translate" \
    --remove-key="Version" \
    --remove-category="MIDI" \
    --remove-category="ALSA" \
    --remove-category="JACK" \
    --add-category="Midi" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%{_bindir}/%{name}
%{_datadir}/locale/*.qm
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
#{_datadir}/pixmaps/%%{name}.png
