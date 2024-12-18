Name:		texlive-elsarticle
Version:	73084
Release:	1
Summary:	Class for articles for submission to Elsevier journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elsarticle
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class is for typeset journal articles, is accepted for
submitted articles, both in Elsevier's electronic submission
system and elsewhere. It replaces the 10-year-old class elsart.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/elsarticle
%{_texmfdistdir}/tex/latex/elsarticle
%doc %{_texmfdistdir}/doc/latex/elsarticle
#- source
%doc %{_texmfdistdir}/source/latex/elsarticle

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
