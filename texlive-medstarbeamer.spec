Name:		texlive-medstarbeamer
Version:	38828
Release:	1
Summary:	Beamer document class for MedStar Health Research Institute
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/medstarbeamer
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/medstarbeamer.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/medstarbeamer.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a beamer template for MedStar Health presentations. It
includes sample presentations using both .tex files and .rnw
files. The document class is obviously compatible with both.
The advantage of the .rnw file is that it can be used with
knitr such that you can weave your R code with your
presentation.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/medstarbeamer
%doc %{_texmfdistdir}/doc/latex/medstarbeamer

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
