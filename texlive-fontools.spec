# revision 23329
# category Package
# catalog-ctan /fonts/utilities/fontools
# catalog-date 2011-06-19 14:02:49 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-fontools
Version:	20110619
Release:	2
Summary:	Tools to simplify using fonts (especially TT/OTF ones)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/utilities/fontools
License:	GPL
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
plus .fd and .sty files; CMAP2ENC - convert glyph indices in
TrueType fonts without glyph names (such as Linotype Palatino)
to Adobe glyph names; FONT2AFM - create font metrics; this is
just a wrapper script around tools such as pf2afm, ttf2afm,
pfm2kpx and ot2kpx; OT2KPX - extract all kerning pairs from an
OpenType font; PFM2KPX - extract all kerning pairs from buggy
.pfm files (the ones where pf2afm complains ".notdef character
occurred among kern pairs"); and SHOWGLYPHS - create a pdf file
that shows all glyphs in a font. Please see the documentation
of the individual programs for further information.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/cmap2enc
%{_bindir}/font2afm
%{_bindir}/ot2kpx
%{_bindir}/pfm2kpx
%{_bindir}/showglyphs
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ly1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_t1.enc
%{_texmfdistdir}/fonts/enc/dvips/fontools/fontools_ts1.enc
%{_texmfdistdir}/scripts/fontools/afm2afm
%{_texmfdistdir}/scripts/fontools/autoinst
%{_texmfdistdir}/scripts/fontools/cmap2enc
%{_texmfdistdir}/scripts/fontools/font2afm
%{_texmfdistdir}/scripts/fontools/ot2kpx
%{_texmfdistdir}/scripts/fontools/pfm2kpx
%{_texmfdistdir}/scripts/fontools/showglyphs
%doc %{_texmfdistdir}/doc/support/fontools/GPLv2.txt
%doc %{_texmfdistdir}/doc/support/fontools/README
%doc %{_texmfdistdir}/doc/support/fontools/examples/berling/berling.sty
%doc %{_texmfdistdir}/doc/support/fontools/examples/berling/berling.sub
%doc %{_texmfdistdir}/doc/support/fontools/examples/berling/makeberling
%doc %{_texmfdistdir}/doc/support/fontools/examples/berling/mbr_fnst.tex
%doc %{_texmfdistdir}/doc/support/fontools/examples/frutiger/frutiger.sty
%doc %{_texmfdistdir}/doc/support/fontools/examples/frutiger/frutiger.sub
%doc %{_texmfdistdir}/doc/support/fontools/examples/frutiger/lfr_fnst.tex
%doc %{_texmfdistdir}/doc/support/fontools/examples/frutiger/makefrutiger
%doc %{_texmfdistdir}/doc/support/fontools/examples/palatinox/Palatino_fnst.tex
%doc %{_texmfdistdir}/doc/support/fontools/examples/palatinox/make_Palatino
%doc %{_texmfdistdir}/doc/support/fontools/examples/palatinox/pala.sub
%doc %{_texmfdistdir}/doc/support/fontools/examples/palatinox/palatinox.sty
%doc %{_texmfdistdir}/doc/support/fontools/examples/palatinox/unsetSCaps.mtx
%doc %{_mandir}/man1/afm2afm.1*
%doc %{_texmfdir}/doc/man/man1/afm2afm.man1.pdf
%doc %{_mandir}/man1/autoinst.1*
%doc %{_texmfdir}/doc/man/man1/autoinst.man1.pdf
%doc %{_mandir}/man1/cmap2enc.1*
%doc %{_texmfdir}/doc/man/man1/cmap2enc.man1.pdf
%doc %{_mandir}/man1/font2afm.1*
%doc %{_texmfdir}/doc/man/man1/font2afm.man1.pdf
%doc %{_mandir}/man1/ot2kpx.1*
%doc %{_texmfdir}/doc/man/man1/ot2kpx.man1.pdf
%doc %{_mandir}/man1/pfm2kpx.1*
%doc %{_texmfdir}/doc/man/man1/pfm2kpx.man1.pdf
%doc %{_mandir}/man1/showglyphs.1*
%doc %{_texmfdir}/doc/man/man1/showglyphs.man1.pdf

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
