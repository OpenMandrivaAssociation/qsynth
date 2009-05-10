Summary:	Qt GUI Interface for FluidSynth
Name:     	qsynth
Version:	0.3.4
Release:	%mkrel 2
License:	GPLv2+
Group:		Sound
Source0: 	http://downloads.sourceforge.net/qsynth/%name-%version.tar.gz
Patch0:		qsynth-0.3.3-fix-locale-install.patch
URL:		http://qsyth.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	fluidsynth-devel
Requires:	fluidsynth

%description
Qsynth is a fluidsynth GUI front-end application written in C++ around
the Qt4 toolkit using Qt Designer. Eventually it may evolve into a
softsynth management application allowing the user to control and manage
a variety of command line softsynth but for the moment it wraps the
excellent FluidSynth.

%prep
%setup -q
%patch0 -p0 -b .locale

%build
%configure2_5x
make CXXFLAGS="%{optflags}" LFLAGS="%{ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
