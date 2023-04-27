%global octpkg octclip

Summary:	Functions for boolean operations with polygons in Octave
Name:		octave-octclip
Version:	2.0.3
Release:	1
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/octclip/
Url:		https://bitbucket.org/jgpallero/octclip/src/master/
Source0:	https://bitbucket.org/jgpallero/octclip/downloads/octclip-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?61483
#Patch0:		honor-cflags-cxxflags.patch
# https://savannah.gnu.org/bugs/index.php?61484
#Patch1:		format-security-error.patch
# https://savannah.gnu.org/bugs/index.php?55343
Patch2:		do-not-strip-debugging-symbols.patch

BuildRequires:  octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
This package allows to do boolean operations with polygons using the
Greiner-Hormann algorithm.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
#{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

