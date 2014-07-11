# revision 32749
# category Package
# catalog-ctan /fonts/utilities/fontools
# catalog-date 2014-01-21 20:21:36 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-fontools
Version:	20140121
Release:	3
Summary:	Tools to simplify using fonts (especially TT/OTF ones)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/fontools
License:	GPL2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fontools.doc.tar.xz
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
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ly1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ts1.enc
%{_texmfdistdir}/scripts/fontools/afm2afm
%{_texmfdistdir}/scripts/fontools/autoinst
%{_texmfdistdir}/scripts/fontools/ot2kpx
%doc %{_mandir}/man1/afm2afm.1*
%doc %{_texmfdistdir}/doc/man/man1/afm2afm.man1.pdf
%doc %{_mandir}/man1/autoinst.1*
%doc %{_texmfdistdir}/doc/man/man1/autoinst.man1.pdf
%doc %{_mandir}/man1/ot2kpx.1*
%doc %{_texmfdistdir}/doc/man/man1/ot2kpx.man1.pdf
%doc %{_texmfdistdir}/doc/support/fontools/GPLv2.txt
%doc %{_texmfdistdir}/doc/support/fontools/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

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
