%define name    qsynth
%define version 0.3.6
%define release %mkrel 1

Name:           %{name}
Summary:        Qt GUI Interface for FluidSynth
Version:        %{version}
Release:        %{release}

License:        GPLv2+
Group:          Sound
Source0:        http://downloads.sourceforge.net/qsynth/%name-%version.tar.gz
URL:            http://%name.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  qt4-devel
BuildRequires:  qt4-linguist
BuildRequires:  fluidsynth-devel
BuildRequires:  desktop-file-utils
Requires:       fluidsynth

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around
the Qt4 toolkit using Qt Designer. Eventually it may evolve into a
softsynth management application allowing the user to control and manage
a variety of command line softsynth but for the moment it wraps the
excellent FluidSynth.

%prep
%setup -q


%build
# Fix locale installation path
perl -pi -e 's/share\/locale/share\/qsynth\/locale/g' src/CMakeLists.txt
perl -pi -e 's/share\/locale/share\/qsynth\/locale/g' src/qsynth.cpp
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
%make

%install
rm -rf %{buildroot}
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

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/qsynth.png
