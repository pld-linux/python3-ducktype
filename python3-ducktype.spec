Summary:	Parse Ducktype files and convert them to Mallard
Summary(pl.UTF-8):	Analiza plików Ducktype i konwersja do formatu Mallard
Name:		python3-ducktype
Version:	0.1
Release:	10
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/duck/
Source0:	https://files.pythonhosted.org/packages/source/d/duck/duck-%{version}.tar.gz
# Source0-md5:	057200b029695f44fd4c518d7f0cd385
URL:		https://pypi.org/project/duck/
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parse Ducktype files and convert them to Mallard.

%description -l pl.UTF-8
Analiza plików Ducktype i konwersja do formatu Mallard.

%prep
%setup -q -n duck-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ducktype
%{py3_sitescriptdir}/ducktype
%{py3_sitescriptdir}/duck-%{version}-py*.egg-info
