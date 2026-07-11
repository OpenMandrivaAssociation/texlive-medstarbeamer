%global tl_name medstarbeamer
%global tl_revision 38828

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Beamer document class for MedStar Health Research Institute
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/medstarbeamer
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/medstarbeamer.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/medstarbeamer.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a beamer template for MedStar Health presentations. It includes
sample presentations using both .tex files and .rnw files. The document
class is obviously compatible with both. The advantage of the .rnw file
is that it can be used with knitr such that you can weave your R code
with your presentation.

