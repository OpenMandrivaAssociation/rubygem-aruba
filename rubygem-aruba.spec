%define oname aruba

Name:       rubygem-%{oname}
Version:    0.2.6
Release:    %mkrel 1
Summary:    CLI Steps for Cucumber, hand-crafted for you in Aruba
Group:      Development/Ruby
License:    MIT
URL:        http://github.com/aslakhellesoy/aruba
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   rubygem(cucumber) >= 0.9.4
Requires:   rubygem(background_process)
Requires:   rubygem(rspec) >= 2.0.1
BuildRequires: rubygems
BuildArch: noarch
Provides: rubygem(%{oname}) = %{version}

%description
CLI Steps for Cucumber, hand-crafted for you in Aruba


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

# clean vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.git*
%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/.bundle/
%{ruby_gemdir}/gems/%{oname}-%{version}/.rvmrc
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/config/
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.rdoc
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
