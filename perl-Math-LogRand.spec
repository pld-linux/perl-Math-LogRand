#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	LogRand
Summary:	Math::LogRand - returns a random number with log weighting
Summary(pl):	Math::LogRand - liczby losowe z rozk�adem logarytmicznym
Name:		perl-Math-LogRand
Version:	0.01
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1179c6b07d72505a00b5b73a89610b4c
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accepts arguments: the floor of distribution, and the ceilling of
distribution. Returns a 'random' integer produced by the Perl rand()
function, between input parameters, with weighting to low integers by
log distribution.

%description -l pl
Funkcja LogRand jako argumenty przyjmuje pocz�tek i koniec przedzia�u.
Zwraca ca�kowit� liczb� "losow�" wyprodukowan� przez perlow� funkcj�
rand() z podanego przedzia�u o rozk�adzie logarytmicznym.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Math/LogRand.pm
%{_mandir}/man3/*
