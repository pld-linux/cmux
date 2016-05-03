Summary:	Enables GSM 0710 multiplexing using linux n_gsm line dicipline
Name:		cmux
Version:	0.8
Release:	1
License:	CC
Group:		Applications/Communications
Source0:	https://github.com/mwarning/cmux/archive/v%{version}.tar.gz
# Source0-md5:	eede5deeac18e20d1cea59e034573d39
# NOTE: fork of original; fork has more features
URL:		https://github.com/mwarning/cmux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program enables GSM 0710 multiplexing using linux n_gsm line
dicipline. Supported are also SIM900 and Telit modules.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} %{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -p cmux $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755, root, root) %{_bindir}/cmux
