Name:		texlive-fontools
Version:	61726
Release:	1
Summary:	Tools to simplify using fonts (especially TT/OTF ones)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/fontools
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontools.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-fontools.bin = %{EVRD}

%description
This package provides a few tools to ease using fonts
(especially Truetype/Opentype ones) with Latex and fontinst:
afm2afm - reencode .afm files; designed to replace fontinst's
\reencodefont for big .afm files; autoinst - simplify the use
of the LCDF TypeTools by creating a command file for otftotfm,
plus .fd and .sty files; and ot2kpx - extract all kerning pairs
from an OpenType font.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/*
%{_texmfdistdir}/fonts/enc/dvips/fontools
%{_texmfdistdir}/scripts/fontools
%doc %{_mandir}/man1/*
%doc %{_texmfdistdir}/doc/man/man1/*
%doc %{_texmfdistdir}/doc/support/fontools

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/fontools/afm2afm afm2afm
ln -sf %{_texmfdistdir}/scripts/fontools/autoinst autoinst
ln -sf %{_texmfdistdir}/scripts/fontools/ot2kpx ot2kpx
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
