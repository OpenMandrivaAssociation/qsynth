%define name	qsynth
%define version	0.3.2
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	GUI for fluidsynth soundfont softward synthesizer
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://qsynth.sourceforge.net/
License:	GPL
Group:		Sound
BuildRequires:	ImageMagick
BuildRequires:	qt4-devel fluidsynth-devel
Requires:	fluidsynth

%description
QSynth is a fluidsynth GUI front-end application written in C++ around the Qt3
toolkit using Qt Designer. Eventually it may evolve into a softsynth
management application allowing the user to control and manage a variety of
command line softsynth but for the moment it wraps the excellent FluidSynth.
FluidSynth is a command line software synthesiser based on the Soundfont
specification.

%prep
%setup -q

%build
export QTDIR=/usr/lib/qt3
export PATH=/usr/lib/qt3/bin:$PATH
perl -pi -e 's/\$QTDIR\/lib/\$QTDIR\/%{_lib}/' configure
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="QSynth" longtitle="Soft Synth GUI" section="Multimedia/Sound" xdg="true"
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 icons/%name.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 icons/%name.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 icons/%name.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO README
%{_bindir}/%name
%{_menudir}/%name
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_iconsdir}/*.png
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
