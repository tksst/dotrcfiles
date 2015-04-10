%define install_path /usr/share/tksst/screenrc
%define source_filename screenrc.tksst

Name:		tksst-screenrc
Version:	1
Release:	1
Summary:	no summary
License:	Public Domain

Source0:	%{source_filename}
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BUildArch:	noarch


%description

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .

%build

%install
rm -rf %{buildroot}
install -Dpm 644 %{SOURCE0} %{buildroot}%{install_path}/%{source_filename}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{install_path}/%{source_filename}


%changelog

