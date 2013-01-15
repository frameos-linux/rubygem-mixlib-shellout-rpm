# Generated from mixlib-shellout-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%define rbname mixlib-shellout

Summary: Run external commands on Unix or Windows
Name: rubygem-%{rbname}

Version: 1.1.0
Release: 5
Group: Development/Ruby
License: Distributable
URL: http://wiki.opscode.com/
Source0: http://rubygems.org/gems/%{rbname}-%{version}.gem
Source1: %{rbname}-%{version}.gemspec
# Make sure the spec template is included in the SRPM
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby 
Requires: rubygems 
BuildRequires: ruby 
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(mixlib-shellout) = %{version}

%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gembuilddir %{buildroot}%{gemdir}

%description
Run external commands on Unix or Windows


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}
%{__rm} -rf %{gembuilddir}/cache
rm -f %{buildroot}%{gemdir}/specifications/%{rbname}-%{version}.gemspec
cp %{SOURCE1} %{buildroot}%{gemdir}/specifications/%{rbname}-%{version}.gemspec

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%doc %{gemdir}/gems/mixlib-shellout-1.1.0/LICENSE
%doc %{gemdir}/gems/mixlib-shellout-1.1.0/README.md
%{gemdir}/gems/mixlib-shellout-1.1.0/lib/mixlib/shellout.rb
%{gemdir}/gems/mixlib-shellout-1.1.0/lib/mixlib/shellout/windows/core_ext.rb
%{gemdir}/gems/mixlib-shellout-1.1.0/lib/mixlib/shellout/exceptions.rb
%{gemdir}/gems/mixlib-shellout-1.1.0/lib/mixlib/shellout/version.rb
%{gemdir}/gems/mixlib-shellout-1.1.0/lib/mixlib/shellout/unix.rb
%{gemdir}/gems/mixlib-shellout-1.1.0/lib/mixlib/shellout/windows.rb


%doc %{gemdir}/doc/mixlib-shellout-1.1.0
%{gemdir}/specifications/%{rbname}-%{version}.gemspec

%changelog
* Tue Jan 08 2013 Sean P. Kane <spkane00@gmail.com> - 1.1.0-4
- Include compatible gemspec

* Tue Sep 11 2012 Sergio Rubio <rubiojr@frameos.org> - 1.1.0-1
- initial release
