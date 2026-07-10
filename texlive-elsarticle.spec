%global tl_name elsarticle
%global tl_revision 77318

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.5
Release:	%{tl_revision}.1
Summary:	Class for articles for submission to Elsevier journals
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/elsarticle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/elsarticle.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class for typesetting journal articles is accepted for submitted
articles both in Elsevier's electronic submission system and elsewhere.
Please note that this webpage is meant for uploading updates to the
elsarticle software itself, not for submitting articles using it .

