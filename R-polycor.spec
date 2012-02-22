%global packname  polycor
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          0.7_8
Release:          1
Summary:          Polychoric and Polyserial Correlations
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-8.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-mvtnorm R-sfsmisc
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-mvtnorm R-sfsmisc

%description
Computes polychoric and polyserial correlations by quick "two-step"
methods or ML, optionally with standard errors; tetrachoric and biserial
correlations are special cases.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
