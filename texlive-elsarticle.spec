# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/elsarticle
# catalog-date 2009-09-18 14:01:48 +0200
# catalog-license lppl1.2
# catalog-version 1.20
Name:		texlive-elsarticle
Version:	1.20
Release:	1
Summary:	Class for articles for submission to Elsevier journals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/elsarticle
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The class is for typeset journal articles, is accepted for
submitted articles, both in Elsevier's electronic submission
system and elsewhere. It replaces the 10-year-old class elsart.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/elsarticle/elsarticle-harv.bst
%{_texmfdistdir}/bibtex/bst/elsarticle/elsarticle-num-names.bst
%{_texmfdistdir}/bibtex/bst/elsarticle/elsarticle-num.bst
%{_texmfdistdir}/tex/latex/elsarticle/elsarticle.cls
%doc %{_texmfdistdir}/doc/latex/elsarticle/README
%doc %{_texmfdistdir}/doc/latex/elsarticle/els-1p.pdf
%doc %{_texmfdistdir}/doc/latex/elsarticle/els-3pd.pdf
%doc %{_texmfdistdir}/doc/latex/elsarticle/els1.pdf
%doc %{_texmfdistdir}/doc/latex/elsarticle/els2.pdf
%doc %{_texmfdistdir}/doc/latex/elsarticle/elsarticle-template-harv.tex
%doc %{_texmfdistdir}/doc/latex/elsarticle/elsarticle-template-num.tex
%doc %{_texmfdistdir}/doc/latex/elsarticle/elsdoc.pdf
%doc %{_texmfdistdir}/doc/latex/elsarticle/elsdoc.tex
%doc %{_texmfdistdir}/doc/latex/elsarticle/jfigs.pdf
%doc %{_texmfdistdir}/doc/latex/elsarticle/makefile
%doc %{_texmfdistdir}/doc/latex/elsarticle/manifest.txt
%doc %{_texmfdistdir}/doc/latex/elsarticle/pdfwidgets.sty
%doc %{_texmfdistdir}/doc/latex/elsarticle/rvdtx.sty
#- source
%doc %{_texmfdistdir}/source/latex/elsarticle/elsarticle.dtx
%doc %{_texmfdistdir}/source/latex/elsarticle/elsarticle.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
