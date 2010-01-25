# TODO
# - package: http://code.google.com/p/python-twitter/
# - package for old api
# - find_chat.py, show_edited_chats.py use old api (skype_api.py)
# - use skype-XXX prefix for all progs in bindir?
Summary:	Command-line tools for Skype
Name:		skype-tools
Version:	0.11
Release:	0.1
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.oberle.org/skype_tools-%{version}.tar.gz
# Source0-md5:	13091fccca8160e3e51ec064f42c82fd
URL:		http://www.oberle.org/skype_linux_tools
BuildRequires:	rpm-pythonprov
Requires:	python-skype >= 1.0.31.0
Requires:	skype >= 1.4.0.64
Suggests:	python-twitter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package provided here contains a set of command-line tools for
Skype Linux to do various things that cannot be done with the user
interface.

%prep
%setup -q -n skype_linux_tools

install -d apis
# use external deps
mv skype_api.py twitter.py apis

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p *.py $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/*.py
