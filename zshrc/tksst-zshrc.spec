%define install_path /usr/share/tksst/zshrc
%define source_filename1 zshrc.tksst
%define source_filename2 zprofile.tksst


Name:		tksst-zshrc
Version:	2
Release:	1
Summary:	no summary
License:	Public Domain

Source0:	%{source_filename1}
Source1:	%{source_filename2}
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BUildArch:	noarch


%description

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .

%build

%install
rm -rf %{buildroot}
install -Dpm 644 %{SOURCE0} %{buildroot}%{install_path}/%{source_filename1}
install -Dpm 644 %{SOURCE1} %{buildroot}%{install_path}/%{source_filename2}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{install_path}/%{source_filename1}
%{install_path}/%{source_filename2}


%changelog
