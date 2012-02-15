%define oname aruba

Name:       rubygem-%{oname}
Version:    0.4.11
Release:	2
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
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

# clean vcs files
rm -f %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/.git*
%clean

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/spec/%{oname}
#% {ruby_gemdir}/gems/% {oname}-% {version}/.bundle/
%{ruby_gemdir}/gems/%{oname}-%{version}/.rvmrc
%{ruby_gemdir}/gems/%{oname}-%{version}/.rspec
%{ruby_gemdir}/gems/%{oname}-%{version}/.travis.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/.document
%{ruby_gemdir}/gems/%{oname}-%{version}/config/

%{ruby_gemdir}/gems/%{oname}-%{version}/templates/
%{ruby_gemdir}/gems/%{oname}-%{version}/cucumber.yml
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{oname}-%{version}/features/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/*.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/%{oname}/*.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/History.md
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/%{oname}.gemspec
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
