# TODO
# - package: http://code.google.com/p/python-twitter/
# - package for old api
# - find_chat.py, show_edited_chats.py use old api (skype_api.py)
Summary:	Command-line tools for Skype
Name:		skype-tools
Version:	0.11
Release:	0.2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.oberle.org/skype_tools-%{version}.tar.gz
# Source0-md5:	4204fa0441034c296d11b37e139e7660
URL:		http://www.oberle.org/skype_linux_tools
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
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

# for rpm autodeps
%{__sed} -i -e '1s,#!.*python,#!%{__python},' *.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
for a in *.py; do
	p=$(basename $a .py)
	install -p $a $RPM_BUILD_ROOT%{_bindir}/skype-$(echo $p | tr _ -)
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/skype-*
