Name:		texlive-modeles-factures-belges-assocs
Version:	67840
Release:	1
Summary:	Generate invoices for Belgian non-profit organizations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/modeles-factures-belges-assocs
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modeles-factures-belges-assocs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/modeles-factures-belges-assocs.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides templates and a sty file for generating
invoices for Belgian non-profit organizations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/modeles-factures-belges-assocs
%doc %{_texmfdistdir}/doc/latex/modeles-factures-belges-assocs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
