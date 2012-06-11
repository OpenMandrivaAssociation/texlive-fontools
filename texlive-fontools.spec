# revision 25995
# category Package
# catalog-ctan /fonts/utilities/fontools
# catalog-date 2012-03-08 23:38:15 +0100
# catalog-license gpl2
# catalog-version undef
Name:		texlive-fontools
Version:	20120308
Release:	1
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
AFM2AFM - reencode .afm files; designed to replace fontinst's
\reencodefont for big .afm files; AUTOINST - simplify the use
of the LCDF TypeTools by creating a command file for otftotfm,
plus .fd and .sty files; and OT2KPX - extract all kerning pairs
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
%doc %{_texmfdistdir}/doc/support/fontools/GPLv2.txt
%doc %{_texmfdistdir}/doc/support/fontools/README
%doc %{_mandir}/man1/afm2afm.1*
%doc %{_texmfdir}/doc/man/man1/afm2afm.man1.pdf
%doc %{_mandir}/man1/autoinst.1*
%doc %{_texmfdir}/doc/man/man1/autoinst.man1.pdf
%doc %{_mandir}/man1/ot2kpx.1*
%doc %{_texmfdir}/doc/man/man1/ot2kpx.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/fontools/afm2afm afm2afm
    ln -sf %{_texmfdistdir}/scripts/fontools/autoinst autoinst
    ln -sf %{_texmfdistdir}/scripts/fontools/cmap2enc cmap2enc
    ln -sf %{_texmfdistdir}/scripts/fontools/font2afm font2afm
    ln -sf %{_texmfdistdir}/scripts/fontools/ot2kpx ot2kpx
    ln -sf %{_texmfdistdir}/scripts/fontools/pfm2kpx pfm2kpx
    ln -sf %{_texmfdistdir}/scripts/fontools/showglyphs showglyphs
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
